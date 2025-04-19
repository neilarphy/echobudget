import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'

import PublicLayout from '@/layouts/PublicLayout.vue'
import PrivateLayout from '@/layouts/PrivateLayout.vue'

import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'

import DashboardView from '@/views/app/DashboardView.vue'
import AnalyticsView from '@/views/app/AnalyticsView.vue'
import HistoryView from '@/views/app/HistoryView.vue'
import ProfileView from '@/views/app/ProfileView.vue'

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
      {
        path: 'dashboard',
        name: 'Dashboard',
        component: DashboardView,
        meta: { requireAuth: true }
      },
      {
        path: 'analytics',
        name: 'AnalyticsView',
        component: AnalyticsView,
        meta: { requireAuth: true }
      },
      {
        path: 'history',
        name: 'History',
        component: HistoryView,
        meta: { requireAuth: true }
      },
      {
        path: 'profile',
        name: 'profile',
        component: ProfileView,
        meta: { requireAuth: true }
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  if (to.meta.requireAuth && !authStore.isAuthenticated) {
    return next('/login')
  }

  next()
})

export default router
