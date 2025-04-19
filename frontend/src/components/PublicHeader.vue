<template>
    <header class="public-header">
      <div class="container">
        <RouterLink to="/" class="logo">EchoBudget</RouterLink>
        <nav class="nav">
          <RouterLink to="/" exact>Главная</RouterLink>
          <RouterLink to="/login">Вход</RouterLink>
          <RouterLink to="/register">Регистрация</RouterLink>
        </nav>
      </div>
    </header>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router'
  </script>
  
  <style scoped>
  .public-header {
    background: #0f0f0f;
    border-bottom: 1px solid #222;
    padding: 1rem 2rem;
    position: sticky;
    top: 0;
    z-index: 100;
  }
  
  .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: auto;
  }
  
  .logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: #4faaff;
    text-decoration: none;
  }
  
  .nav {
    display: flex;
    gap: 1.5rem;
  }
  
  .nav a {
    color: #ccc;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s ease;
  }
  
  .nav a.router-link-exact-active,
  .nav a:hover {
    color: #ffffff;
  }
  </style>
  