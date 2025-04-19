<template>
    <div class="api-test">
      <el-card>
        <h3> Тест API-запроса к /api/history</h3>
        <el-button type="primary" @click="fetchHistory">Запросить /api/history</el-button>
        <div v-if="loading">Загрузка...</div>
        <div v-if="error" class="error">Ошибка: {{ error }}</div>
        <ul v-if="history.length">
          <li v-for="(entry, index) in history" :key="index">
            {{ entry.id }} — {{ entry.original }} → {{ entry.parsed }} ({{ entry.cost }}₽)
          </li>
        </ul>
      </el-card>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { ref } from 'vue'
  
  const loading = ref(false)
  const error = ref('')
  const history = ref([])
  
  const fetchHistory = async () => {
    loading.value = true
    error.value = ''
    try {
      const res = await axios.get('/api/history/')  
      history.value = res.data  
    } catch (err) {
      error.value = err.message || 'Неизвестная ошибка'
      console.error(' Ошибка:', err)
    } finally {
      loading.value = false
    }
  }
  </script>
  
  <style scoped>
  .api-test {
    max-width: 600px;
    margin: 2rem auto;
    padding: 1rem;
  }
  .error {
    color: red;
  }
  </style>
  