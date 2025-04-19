<template>
    <section class="auth-page">
        <div class="form-box">
            <h2 class="title">Регистрация</h2>
            <p class="subtitle">Создайте новый аккаунт</p>

            <el-form :model="form" class="form" label-position="top">
                <el-form-item label="Имя пользователя">
                    <el-input v-model="form.username" placeholder="username" />
                </el-form-item>

                <el-form-item label="Email">
                    <el-input v-model="form.email" placeholder="example@mail.com" />
                </el-form-item>

                <el-form-item label="Пароль">
                    <el-input v-model="form.password" placeholder="••••••••" show-password />
                </el-form-item>

                <el-form-item label="Подтверждение пароля">
                    <el-input v-model="form.confirm" placeholder="••••••••" show-password />
                </el-form-item>

                <el-button type="primary" @click="register">Зарегистрироваться</el-button>
            </el-form>

            <p class="alt">
                Уже есть аккаунт?
                <a @click="$router.push('/login')">Войти</a>
            </p>
        </div>
    </section>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { ElMessage } from 'element-plus'
import { useAuthStore } from '@/stores/authStore'

const router = useRouter()
const authStore = useAuthStore()

const form = ref({
  username: '',
  email: '',
  password: '',
  confirm: ''
})

async function register() {
  if (form.value.password !== form.value.confirm) {
    ElMessage.error('Пароли не совпадают')
    return
  }

  try {
    const res = await axios.post('/api/auth/register', {
      username: form.value.username,
      email: form.value.email,
      password: form.value.password
    })

    authStore.setAuth({
      token: res.data.token,
      username: res.data.username
    })

    ElMessage.success('Регистрация прошла успешно')
    router.push('/dashboard')
  } catch (err) {
    ElMessage.error(err.response?.data?.detail || 'Ошибка регистрации')
  }
}
</script>



<style scoped>
.auth-page {
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #0f0f0f, #262f98);
    padding: 2rem 2rem 2rem;
    width: 100vw;
    min-height: 100vh;
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