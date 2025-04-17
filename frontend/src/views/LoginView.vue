<template>
    <section class="auth-page">
        <div class="form-box">
            <h2 class="title">Добро пожаловать</h2>
            <p class="subtitle">Войдите в свой аккаунт</p>

            <el-form :model="form" class="form" label-position="top">
                <el-form-item label="Email">
                    <el-input v-model="form.email" placeholder="example@mail.com" />
                </el-form-item>

                <el-form-item label="Пароль">
                    <el-input v-model="form.password" placeholder="••••••••" show-password />
                </el-form-item>

                <el-button type="primary" @click="login">Войти</el-button>
            </el-form>

            <p class="alt">
                Нет аккаунта?
                <a @click="$router.push('/register')">Зарегистрируйтесь</a>
            </p>
        </div>
    </section>
</template>

<script setup>
import { ref } from 'vue'

const form = ref({
    email: '',
    password: ''
})

function login() {
    // TODO: логика логина
    console.log(form.value)
}
</script>

<style scoped>
.auth-page {
    display: flex;
    align-items: center;
    justify-content: center;

    min-height: 100dvh;
    background: linear-gradient(135deg, #0f0f0f, #262f98);
    padding: 2rem 2rem 2rem;
    width: 100vw;
    box-sizing: border-box;
}

.form-box {
    background: #1c1c1c;
    padding: 2rem 2.5rem;
    border-radius: 12px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
    width: 100%;
    max-width: 400px;
    color: #fff;
}

.title {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 0.5rem;
}

.subtitle {
    color: #aaa;
    margin-bottom: 1.5rem;
}

.alt {
    margin-top: 1.5rem;
    font-size: 0.9rem;
    color: #aaa;
}

.alt a {
    color: #4faaff;
    cursor: pointer;
}
</style>