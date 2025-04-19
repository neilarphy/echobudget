<template>
    <section class="analytics">
      <h1 class="title">📈 Аналитика расходов и доходов</h1>
      <p class="subtitle">Эта секция в разработке, но вот пара заглушек:</p>
  
      <div class="charts">
        <div class="chart-card">
          <h3>Доходы vs Расходы</h3>
          <img src="https://placehold.co/400x200/222/fff?text=Mock+Bar+Chart" alt="Bar chart" />
        </div>
        <div class="chart-card">
          <h3>Распределение категорий</h3>
          <img src="https://placehold.co/200x200/333/fff?text=Mock+Pie" alt="Pie chart" />
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  // Пока нет логики, только заглушка
  </script>
  
  <style scoped>
  .analytics {
    padding: 2rem;
    max-width: 1200px;
    margin: auto;
    color: white;
    text-align: center;
  }
  
  .title {
    font-size: 2.4rem;
    margin-bottom: 0.5rem;
  }
  
  .subtitle {
    font-size: 1.2rem;
    color: #aaa;
    margin-bottom: 2rem;
  }
  
  .charts {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2rem;
  }
  
  .chart-card {
    background: #1a1a1a;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.4);
    width: 100%;
    max-width: 450px;
  }
  
  .chart-card h3 {
    margin-bottom: 1rem;
    color: #4faaff;
  }
  </style>
  