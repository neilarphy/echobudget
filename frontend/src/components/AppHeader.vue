<template>
  <header class="header">
    <div class="logo">EchoBudget</div>

    <nav class="nav">
      <router-link to="/dashboard">Дашборд</router-link>
      <router-link to="/analytics">Аналитика</router-link>
      <router-link to="/history">История</router-link>
    </nav>

    <div class="actions">
      <div class="balance">
        💰 {{ balance }} токенов
        <el-button type="success" size="small" @click="showTopup = true">Пополнить</el-button>
      </div>
      <router-link to="/profile" class="profile">
        👤 {{ userName }}
      </router-link>

    </div>

    <el-dialog v-model="showTopup" title="Пополнение баланса" width="30%">
      <el-input v-model="topupAmount" placeholder="Введите сумму" />
      <template #footer>
        <el-button @click="showTopup = false">Отмена</el-button>
        <el-button type="primary" @click="confirmTopup">Пополнить</el-button>
      </template>
    </el-dialog>
  </header>
</template>

<script setup>
import { inject, ref, computed } from 'vue'
import axios from 'axios'
import { ElMessage } from 'element-plus'
import { useAuthStore } from '@/stores/authStore'
const auth = useAuthStore()

const userName = computed(() => auth.username || 'Гость')

const balance = inject('balance')
const loadBalance = inject('loadBalance')

const showTopup = ref(false)
const topupAmount = ref('')

async function confirmTopup() {
  const amount = parseInt(topupAmount.value)
  if (isNaN(amount) || amount <= 0) {
    ElMessage.error('Введите корректную сумму')
    return
  }

  try {
    await axios.post('/api/balance/topup', {
      amount,
      source: 'topup'
    })
    ElMessage.success(`Баланс пополнен на ${amount}₽`)
    await loadBalance() 
  } catch (err) {
    ElMessage.error('Ошибка пополнения')
    console.error('Ошибка:', err)
  } finally {
    showTopup.value = false
    topupAmount.value = ''
  }
}
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background: #0f0f0f;
  border-bottom: 1px solid #333;
}

.logo {
  color: #4faaff;
  font-weight: bold;
  font-size: 1.5rem;
}

.nav a {
  margin-left: 1rem;
  color: #ccc;
}

.nav a.router-link-exact-active {
  color: #4faaff;
}

.actions {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.balance {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #aaffaa;
  font-weight: 500;
}

.profile {
  color: #eee;
}
</style>
