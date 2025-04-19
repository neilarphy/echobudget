<template>
    <section class="dashboard">
      <h1 class="greeting">👋 Добро пожаловать, {{ userName }}!</h1>

      <div class="grid">
        <!-- 🎙 Ввод транзакции: голос и текст -->
        <div class="card span-3 input-card">
          <h2><el-icon><Mic /></el-icon> Ввод транзакции</h2>
          <p class="description">Выберите способ: голос или текст</p>
  
          <div class="input-columns">
            <!-- 🎙 Голос -->
            <div class="input-block voice">
              <h4>🎙 Голосом</h4>
              <button class="voice-button" @click="toggleRecording" :class="{ recording: isRecording }">
                <el-icon v-if="!isRecording"><Mic /></el-icon>
                <el-icon v-else><VideoPause /></el-icon>
              </button>
              <p v-if="audioBlob" class="recorded-label">🎧 Запись готова</p>
            </div>
  
            <!-- ⌨️ Текст -->
            <div class="input-block text">
              <h4>⌨️ Вручную</h4>
              <el-input v-model="manualText" placeholder="Например: Купил кофе за 250₽" />
              <el-button type="primary" class="send-button" @click="sendText">Отправить</el-button>
            </div>
          </div>
        </div>
  
        <!-- Последние транзакции -->
        <div class="card last-transactions span-2">
          <h3><el-icon><ShoppingCart /></el-icon> Последние транзакции</h3>
          <ul class="transaction-list">
            <li><span>Amazon</span><span class="minus">-150$</span></li>
            <li><span>Salary</span><span class="plus">+2500$</span></li>
            <li><span>Groceries</span><span class="minus">-75$</span></li>
          </ul>
        </div>
  
        <!-- Советы от ИИ -->
        <div class="card ai">
          <h3><el-icon><MagicStick /></el-icon> Советы от ИИ</h3>
          <ul class="ai-tips">
            <li>✅ Используйте депозиты для целей</li>
            <li>✅ Проверяйте подписки</li>
            <li>✅ Оптимизируйте расходы через планировщик</li>
          </ul>
        </div>
  
        <!-- Финансовая игра -->
        <div class="card game span-3">
          <h3>🎮 Финансовая игра</h3>
          <div class="game-grid">
            <div class="game-card investor">🏠 Инвестор</div>
            <div class="game-card challenge">📋 Челлендж</div>
            <div class="game-card quiz">❓ Викторина</div>
          </div>
          <el-button type="danger" round class="play-button">Играть</el-button>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref, computed, inject } from 'vue'
  import RecordRTC from 'recordrtc'
  import { ElMessage } from 'element-plus'
  import { Mic, VideoPause, ShoppingCart, MagicStick } from '@element-plus/icons-vue'
  import axios from 'axios'
  import { useAuthStore } from '@/stores/authStore'
  const auth = useAuthStore()

  const userName = computed(() => auth.username || 'Гость')

  const balance = inject('balance')
  const loadBalance = inject('loadBalance')
  
  const isRecording = ref(false)
  const audioBlob = ref(null)
  const manualText = ref('')
  
  let recorder = null
  let stream = null
  
  function toggleRecording() {
    isRecording.value ? stopRecording() : startRecording()
  }
  
  function startRecording() {
    isRecording.value = true
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then((_stream) => {
        stream = _stream
        recorder = new RecordRTC(stream, {
          type: 'audio',
          mimeType: 'audio/wav'
        })
        recorder.startRecording()
      })
      .catch(() => {
        ElMessage.error('Ошибка доступа к микрофону')
        isRecording.value = false
      })
  }
  
  function stopRecording() {
    recorder.stopRecording(() => {
      audioBlob.value = recorder.getBlob()
      isRecording.value = false
      recorder = null
      stream?.getTracks().forEach((t) => t.stop())
      stream = null
      sendVoice(audioBlob.value)
    })
  }
  
  async function pollBalanceUntilChanged(timeoutMs = 10000, intervalMs = 1000) {
    const startBalance = balance.value
    const startedAt = Date.now()
  
    while (Date.now() - startedAt < timeoutMs) {
      await loadBalance()
      if (balance.value !== startBalance) {
        console.log(' Баланс обновился:', balance.value)
        return
      }
      await new Promise(resolve => setTimeout(resolve, intervalMs))
    }
  
    console.warn(' Баланс не обновился в течение таймаута')
  }
  
  async function sendVoice(blob) {
    try {
      const formData = new FormData()
      formData.append('model_type', 'speech_to_text')
      formData.append('file', blob, 'voice.wav')
  
      await axios.post('/api/entry/', formData)
      ElMessage.success('Голосовая транзакция отправлена!')
      await pollBalanceUntilChanged()
    } catch (err) {
      ElMessage.error('Ошибка при отправке голоса')
      console.error('Voice error:', err)
    }
  }
  
  async function sendText() {
    if (!manualText.value.trim()) {
      ElMessage.warning('Введите текст транзакции')
      return
    }
  
    try {
      const formData = new FormData()
      formData.append('model_type', 'entry_classifier')
      formData.append('text', manualText.value)
  
      await axios.post('/api/entry/', formData)
      ElMessage.success('Текстовая транзакция отправлена!')
      manualText.value = ''
      await pollBalanceUntilChanged()
    } catch (err) {
      ElMessage.error('Ошибка при отправке текста')
      console.error('Text error:', err)
    }
  }
  </script>
  
  <style scoped>
  .dashboard {
    padding: 2rem;
    max-width: 1400px;
    margin: auto;
    color: white;
  }
  .greeting {
    font-size: 2.4rem;
    font-weight: bold;
    text-align: center;
    margin-bottom: 2.5rem;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
  }
  .card {
    background: #1a1a1a;
    border-radius: 14px;
    box-shadow: 0 0 25px rgba(0, 0, 0, 0.4);
    padding: 2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  .card.ai {
    align-items: flex-start;
    text-align: left;
  }
  .span-2 { grid-column: span 2; }
  .span-3 { grid-column: span 3; }
  
  .input-columns {
    display: flex;
    gap: 2rem;
    width: 100%;
    margin-top: 1.5rem;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  .input-block {
    flex: 1 1 45%;
    background: #141414;
    border-radius: 12px;
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }
  .input-block.text :deep(.el-input) {
    width: 100%;
  }
  .input-block.text .send-button {
    align-self: flex-end;
  }
  .input-block h4 {
    margin: 0;
    font-size: 1.1rem;
    font-weight: 500;
  }
  .voice-button {
    background: #409eff;
    width: 80px;
    height: 80px;
    border-radius: 50%;
    border: none;
    font-size: 2rem;
    color: white;
    transition: background 0.3s;
    box-shadow: 0 0 10px rgba(0, 128, 255, 0.5);
  }
  .voice-button.recording {
    background: red;
    animation: pulse 1.5s infinite;
  }
  @keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(255, 0, 0, 0.5); }
    70% { box-shadow: 0 0 0 16px rgba(255, 0, 0, 0); }
    100% { box-shadow: 0 0 0 0 rgba(255, 0, 0, 0); }
  }
  .transaction-list {
    list-style: none;
    padding: 0;
    margin-top: 1rem;
  }
  .transaction-list li {
    display: flex;
    justify-content: space-between;
    padding: 0.6rem 0;
    border-bottom: 1px solid #333;
    gap: 0.5rem;
    align-items: center;
  }
  .plus { color: #3cff84; }
  .minus { color: #ff4d4d; }
  .ai-tips {
    margin-top: 1rem;
    padding-left: 1.2rem;
    list-style: disc;
  }
  .game-grid {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
    flex-wrap: wrap;
  }
  .game-card {
    flex: 1 1 30%;
    border-radius: 10px;
    text-align: center;
    font-weight: 500;
    padding: 1rem;
    color: white;
  }
  .investor { background: #2e6032; }
  .challenge { background: #325060; }
  .quiz { background: #60324e; }
  .play-button {
    margin-top: 1rem;
  }
  </style>