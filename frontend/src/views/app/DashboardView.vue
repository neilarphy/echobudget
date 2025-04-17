<template>
    <section class="dashboard">
        <h1 class="greeting">Добро пожаловать, Иван!</h1>

        <div class="grid">
            <!-- Блок голосового ввода -->
            <div class="card full">
                <h2>Ввод транзакции голосом</h2>
                <p class="description">Нажмите на микрофон, чтобы добавить транзакцию</p>
                <button class="voice-button" @click="toggleRecording" :class="{ recording: isRecording }">
                    <i v-if="!isRecording" class="el-icon-microphone" />
                    <i v-else class="el-icon-video-pause" />
                </button>
                <p v-if="audioBlob" class="recorded-label">🎧 Запись готова</p>
            </div>

            <!-- Последние транзакции -->
            <div class="card">
                <h3>Последние транзакции</h3>
                <ul class="transaction-list">
                    <li><span>Amazon</span><span class="minus">-150$</span></li>
                    <li><span>Salary</span><span class="plus">+2500$</span></li>
                    <li><span>Groceries</span><span class="minus">-75$</span></li>
                </ul>
            </div>

            <!-- Советы от ИИ -->
            <div class="card">
                <h3>Советы от ИИ</h3>
                <ul class="ai-tips">
                    <li>📌 Используйте депозиты для ускорения целей</li>
                    <li>📌 Проверяйте подписки</li>
                    <li>📌 Оптимизируйте расходы через планировщик</li>
                </ul>
            </div>

            <!-- Финансовая игра -->
            <div class="card wide green">
                <h3>Финансовая игра</h3>
                <div class="game-grid">
                    <div class="game-card">Инвестор 💹</div>
                    <div class="game-card">Бюджетный челлендж 🧮</div>
                    <div class="game-card">Финансовая викторина ❓</div>
                </div>
                <el-button type="danger" round style="margin-top: 1rem">
                    Играть
                </el-button>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref } from 'vue'
import RecordRTC from 'recordrtc'
import { ElMessage } from 'element-plus'

const isRecording = ref(false)
const audioBlob = ref(null)

let recorder = null
let stream = null

function toggleRecording() {
    isRecording.value ? stopRecording() : startRecording()
}

function startRecording() {
    isRecording.value = true
    navigator.mediaDevices.getUserMedia({ audio: true }).then((_stream) => {
        stream = _stream
        recorder = new RecordRTC(stream, {
            type: 'audio',
            mimeType: 'audio/wav'
        })
        recorder.startRecording()
    }).catch(() => {
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
        ElMessage.success('Запись завершена')
    })
}
</script>

<style scoped>
.dashboard {
    padding: 2rem;
    max-width: 1200px;
    margin: auto;
    color: white;
}

.greeting {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 2rem;
    text-align: center;
}

.grid {
    display: grid;
    gap: 2rem;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
}

.card {
    background: #1a1a1a;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
}

.card.full {
    grid-column: span 2;
    text-align: center;
}

.card.wide {
    grid-column: span 3;
}

.card.green {
    background: #1e3622;
}

.voice-button {
    margin-top: 1rem;
    background: #409eff;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    border: none;
    font-size: 1.5rem;
    color: white;
    transition: background 0.3s;
}

.voice-button.recording {
    background: red;
}

.recorded-label {
    margin-top: 1rem;
    color: #8ff58f;
}

.transaction-list {
    margin: 1rem 0;
    list-style: none;
    padding: 0;
}

.transaction-list li {
    display: flex;
    justify-content: space-between;
    padding: 0.4rem 0;
    border-bottom: 1px solid #333;
}

.plus {
    color: #5aff5a;
}

.minus {
    color: #ff5a5a;
}

.ai-tips {
    list-style: none;
    padding: 0;
    margin: 1rem 0 0;
}

.ai-tips li {
    margin-bottom: 0.5rem;
    font-size: 0.95rem;
    line-height: 1.4;
}

.game-grid {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
}

.game-card {
    flex: 1;
    background: #2f5732;
    padding: 1rem;
    border-radius: 8px;
    text-align: center;
    color: #d7ffd7;
    font-weight: 500;
}
</style>