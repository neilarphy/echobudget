import { createRouter, createWebHistory } from 'vue-router'

import PublicLayout from '@/layouts/PublicLayout.vue'
import PrivateLayout from '@/layouts/PrivateLayout.vue'

import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'

import DashboardView from '@/views/app/DashboardView.vue'
// import BalanceView from '@/views/app/BalanceView.vue'
// import HistoryView from '@/views/app/HistoryView.vue'

const routes = [
  {
    path: '/',
    component: PublicLayout,
    children: [
      { path: '', name: 'Home', component: HomeView },
      { path: 'login', name: 'Login', component: LoginView },
      { path: 'register', name: 'Register', component: RegisterView }
    ]
  },
  {
    path: '/',
    component: PrivateLayout,
    children: [
      { path: 'dashboard', name: 'Dashboard', component: DashboardView },
      // { path: 'balance', name: 'Balance', component: BalanceView },
      // { path: 'history', name: 'History', component: HistoryView }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
