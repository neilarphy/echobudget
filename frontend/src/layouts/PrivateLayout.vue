<template>
    <div class="private-layout">
      <AppHeader />
      <main class="content">
        <RouterView />
      </main>
    </div>
  </template>
  
  <script setup>
  import { provide, ref, onMounted } from 'vue'
  import AppHeader from '@/components/AppHeader.vue'
  import axios from 'axios'
  
  const balance = ref(0)
  provide('balance', balance)
  
  async function loadBalance() {
    try {
      const res = await axios.get('/api/balance/')
      balance.value = res.data.balance || 0
    } catch (err) {
      console.error('Ошибка при загрузке баланса в layout:', err)
    }
  }
  
  onMounted(() => {
    loadBalance()
  })
  
  provide('loadBalance', loadBalance)
  </script>
  
  <style scoped>
  .content {
    padding-top: 64px;
  }
  </style>
  