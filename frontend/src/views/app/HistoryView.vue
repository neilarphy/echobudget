<template>
    <section class="history">
      <h1 class="title">🧾 История транзакций</h1>
  
      <div v-if="loading">Загрузка...</div>
      <div v-else-if="error" class="error">Ошибка: {{ error }}</div>
      <div v-else>
        <el-table
          :data="paginated"
          border
          stripe
          height="auto"
          class="transaction-table"
        >
          <el-table-column prop="id" label="ID" width="60" align="center" />
          <el-table-column prop="raw" label="Исходный ввод" />
          <el-table-column prop="parsed" label="Распознанная транзакция" />
          <el-table-column prop="cost" label="Стоимость" width="100" align="center" />
        </el-table>
  
        <div class="pagination">
          <el-pagination
            layout="prev, pager, next"
            :current-page="page"
            :page-size="10"
            :total="history.length"
            @current-change="changePage"
            background
          />
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

const modelCosts = {
  entry_classifier: 1,
  speech_to_text: 2,
}
const page = ref(1)
const history = ref([])

const fetchHistory = async () => {
  try {
    const res = await axios.get('/api/history/')
    history.value = res.data.history.reverse().map((item) => ({
      id: item.entry.id,
      raw: item.entry.data,
      parsed: item.parsed
        ? `Категория: ${item.parsed.category}, Сумма: ${item.parsed.amount}₽`
        : '—',
      cost: item.parsed
        ? `${modelCosts[item.parsed.model_name] || 5} ток`
        : '—',
    }))
  } catch (err) {
    console.error('Ошибка при получении истории:', err)
  }
}

onMounted(fetchHistory)

const paginated = computed(() =>
  history.value.slice((page.value - 1) * 10, page.value * 10)
)

const changePage = (newPage) => {
  page.value = newPage
}
</script>

  
  <style scoped>
  .history {
    padding: 2rem;
    max-width: 1200px;
    margin: auto;
    color: white;
  }
  
  .title {
    font-size: 2.2rem;
    font-weight: bold;
    text-align: center;
    margin-bottom: 2rem;
  }
  
  .transaction-table {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.3);
    background: #1c1c1c;
  }
  
  .el-table th,
  .el-table td {
    background-color: transparent !important;
    color: white;
    font-size: 0.95rem;
  }
  
  .el-table tbody tr:hover > td {
    background-color: #2a2a2a !important;
    transition: background 0.3s;
  }
  
  .pagination {
    margin-top: 2rem;
    text-align: center;
  }
  
  .error {
    color: red;
    text-align: center;
    margin-bottom: 2rem;
  }
  </style>
  