<template>
    <header class="app-header">
        <div class="container">
            <div class="left">
                <RouterLink to="/dashboard" class="logo">EchoBudget</RouterLink>
                <nav class="nav">
                    <RouterLink to="/dashboard">📊 Дашборд</RouterLink>
                    <RouterLink to="/analytics">📈 Аналитика</RouterLink>
                    <RouterLink to="/history">📖 История</RouterLink>
                </nav>
            </div>
            <div class="right">
                <span class="user">👤 {{ userName }}</span>
            </div>
        </div>
    </header>
</template>

<script setup>
import { computed } from 'vue'
// Заглушка: позже можно будет взять из Pinia/Store
const userName = computed(() => 'Алексей') // заменить на inject/useStore при необходимости
</script>

<style scoped>
.app-header {
    height: 64px;
    width: 100%;
    background: #101010;
    border-bottom: 1px solid #222;
    display: flex;
    align-items: center;
    z-index: 100;
    position: sticky;
    top: 0;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
}

.logo {
    color: #4faaff;
    font-weight: bold;
    font-size: 1.3rem;
    text-decoration: none;
}

.nav {
    display: flex;
    gap: 1.5rem;
    margin-left: 2rem;
}

.nav a {
    color: #ccc;
    text-decoration: none;
    font-weight: 500;
    font-size: 1rem;
    transition: color 0.2s;
}

.nav a.router-link-active,
.nav a:hover {
    color: white;
}

.right {
    font-size: 1rem;
    color: #ccc;
}
</style>