import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    username: localStorage.getItem('username') || null,
    email: localStorage.getItem('email') || null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.token,
  },

  actions: {
    setAuth({ token, username, email }) {
      this.email = email
      this.token = token
      this.username = username
      localStorage.setItem('email', email)
      localStorage.setItem('token', token)
      localStorage.setItem('username', username)
    },

    logout() {
      this.email = null
      this.token = null
      this.username = null
      localStorage.removeItem('email')
      localStorage.removeItem('token')
      localStorage.removeItem('username')
    },
  },
})
