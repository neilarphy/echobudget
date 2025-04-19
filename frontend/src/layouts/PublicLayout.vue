<template>
    <div>
      <PublicHeader />
      <main>
        <RouterView />
      </main>
    </div>
  </template>
  
  <script setup>
  import { RouterView } from 'vue-router'
  import PublicHeader from '@/components/PublicHeader.vue'
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
    text-decoration: none;
  }
  
  .nav a.router-link-exact-active {
    color: #4faaff;
  }
  </style>
  