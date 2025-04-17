<template>
    <div>
      <header class="header">
        <div class="logo">EchoBudget</div>
        <nav class="nav">
          <RouterLink to="/">Главная</RouterLink>
          <RouterLink to="/login">Вход</RouterLink>
          <RouterLink to="/register">Регистрация</RouterLink>
        </nav>
      </header>
      <main>
        <RouterView />
      </main>
    </div>
  </template>
  
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
  </style>
  