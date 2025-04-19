<template>
    <section class="profile-page">
      <h1>💼 Личный кабинет</h1>
  
      <div class="user-info">
        <p><strong>Имя:</strong> {{ userName }}</p>
        <p><strong>Email:</strong> {{ userEmail }}</p>
      </div>
  
      <el-table
        v-loading="loading"
        :data="paginatedTransactions"
        style="width: 100%; background: #1e1e1e"
        stripe
        border
      >
        <el-table-column prop="id" label="ID" width="60" />
        <el-table-column prop="source" label="Источник" />
        <el-table-column label="Сумма">
          <template #default="{ row }">
            <span :class="row.type === 'credit' ? 'plus' : 'minus'">
              {{ row.type === 'credit' ? '+' : '-' }}{{ row.amount }} токенов
            </span>
          </template>
        </el-table-column>
      </el-table>
  
      <div class="pagination-container">
        <el-pagination
          background
          layout="prev, pager, next"
          :page-size="pageSize"
          :total="transactions.length"
          @current-change="handlePageChange"
        />
      </div>
  
      <div class="logout-container">
        <el-button type="danger" @click="logout">🚪 Выйти из аккаунта</el-button>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue'
  import axios from 'axios'
  import { ElMessage, ElMessageBox } from 'element-plus'
  import { useAuthStore } from '@/stores/authStore'
  import { useRouter } from 'vue-router'
  
  const router = useRouter()
  const authStore = useAuthStore()
  
  const userName = computed(() => authStore.username || 'Гость')
  const userEmail = computed(() => authStore.email || 'не указано')
  
  function logout() {
    ElMessageBox.confirm(
      'Вы уверены, что хотите выйти из аккаунта?',
      'Подтверждение',
      {
        confirmButtonText: 'Да',
        cancelButtonText: 'Отмена',
        type: 'warning',
      }
    ).then(() => {
      authStore.logout()
      router.push('/')
    }).catch(() => {
      // Отмена выхода
    })
  }
  
  const transactions = ref([])
  const loading = ref(false)
  
  const currentPage = ref(1)
  const pageSize = 10
  
  const paginatedTransactions = computed(() => {
    const start = (currentPage.value - 1) * pageSize
    return transactions.value.slice(start, start + pageSize)
  })
  
  function handlePageChange(val) {
    currentPage.value = val
  }
  
  async function loadHistory() {
    loading.value = true
    try {
      const res = await axios.get('/api/balance/history')
      if (Array.isArray(res.data)) {
        transactions.value = res.data.reverse()
      } else {
        throw new Error('Некорректный формат истории')
      }
    } catch (err) {
      ElMessage.error('Ошибка при загрузке истории')
      console.error(err)
    } finally {
      loading.value = false
    }
  }
  
  onMounted(loadHistory)
  </script>
  
  <style scoped>
  .profile-page {
    padding: 2rem;
    max-width: 1000px;
    margin: auto;
    color: white;
  }
  
  h1 {
    font-size: 2rem;
    margin-bottom: 1.5rem;
  }
  
  .user-info {
    background: #2a2a2a;
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 1.5rem;
  }
  
  .user-info p {
    margin: 0.5rem 0;
  }
  
  .plus {
    color: #3cff84;
  }
  
  .minus {
    color: #ff4d4d;
  }
  
  .pagination-container {
    margin-top: 1rem;
    text-align: center;
  }
  
  .logout-container {
    margin-top: 2rem;
    display: flex;
    justify-content: center;
  }
  </style>
  