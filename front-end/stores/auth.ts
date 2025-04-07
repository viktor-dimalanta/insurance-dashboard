// stores/auth.ts
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRob3IiLCJzdWIiOiJ0aG9yIn0.wEHWg1bzg8dfNDNIWFQzWK6QZckQZomDv8q6upHmxXM',  // Mocked token
  }),

  actions: {
    setToken(token: string) {
      this.token = token
      localStorage.setItem('auth_token', token)  // Store token in localStorage
    },
    getToken() {
      return this.token || localStorage.getItem('auth_token') || ''
    }
  }
})

