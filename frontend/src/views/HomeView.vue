<template>
  <section class="hero">
    <div class="content">
      <h1 class="title">EchoBudget</h1>
      <p class="subtitle">
        Управляй личными финансами с помощью AI.<br>
        Загружай голосовые или текстовые транзакции, отслеживай расходы, достигай целей.
      </p>
      <div class="cta">
        <el-button type="primary" size="large" @click="$router.push('/login')">Войти</el-button>
        <el-button size="large" plain @click="$router.push('/register')">Регистрация</el-button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  width: 100vw;
  min-height: 100vh;
  padding: 2rem 2rem 2rem;

  background: linear-gradient(135deg, #0f0f0f, #262f98);
  color: white;
  text-align: center;
}


.content {
  max-width: 700px;
}

.title {
  font-size: 3.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.subtitle {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  color: #ccc;
}

.cta>*:not(:last-child) {
  margin-right: 1rem;
}
</style>
