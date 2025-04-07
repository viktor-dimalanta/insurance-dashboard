<template>
    <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; align-items: center; justify-content: center; min-height: 100vh; background-color: #f4f4f4;">
      <div style="background-color: #fff; padding: 32px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); width: 384px;">
        <h2 style="font-size: 24px; font-weight: bold; color: #333; margin-bottom: 24px; text-align: center;">Login</h2>
  
        <form @submit.prevent="login">
          <div style="margin-bottom: 16px;">
            <label for="email" style="display: block; font-size: 14px; font-weight: 600; color: #555; margin-bottom: 8px;">Email</label>
            <input v-model="email" type="email" id="email" placeholder="Email"
              style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; font-size: 16px; color: #333; outline: none;"
              required />
          </div>
  
          <div style="margin-bottom: 24px;">
            <label for="password" style="display: block; font-size: 14px; font-weight: 600; color: #555; margin-bottom: 8px;">Password</label>
            <input v-model="password" type="password" id="password" placeholder="Password"
              style="width: 100%; padding: 12px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; font-size: 16px; color: #333; outline: none;"
              required />
          </div>
  
          <button type="submit"
            style="width: 100%; background-color: #007bff; color: #fff; padding: 12px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; transition: background-color 0.3s ease;">
            Login
          </button>
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useAuthStore } from '../stores/auth'  // Assuming you're using Pinia for state management
  
  const email = ref('')
  const password = ref('')
  
  const login = () => {
    // Simulate a successful login by setting a mock token
    const authStore = useAuthStore()
  
    // You can replace the below token with a real one after integrating real auth
    const mockToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRob3IiLCJzdWIiOiJ0aG9yIn0.wEHWg1bzg8dfNDNIWFQzWK6QZckQZomDv8q6upHmxXM'
  
    // Store the token in the auth store and localStorage
    authStore.setToken(mockToken)
  
    console.log('User logged in with token:', mockToken)
    
    // Redirect to the dashboard after a successful login
    // This could be done with a redirect or using Nuxt router
    useRouter().push('/dashboard')
  }
  </script>
  
  <style scoped>
  /* Add any additional styling you need */
  </style>
  