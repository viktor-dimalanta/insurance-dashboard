<template>
    <div class="flex items-center justify-center min-h-screen">
      <div class="bg-white p-8 rounded-lg shadow-lg w-96">
        <h2 class="text-2xl font-bold mb-6">Login</h2>
        
        <form @submit.prevent="login">
          <div class="mb-4">
            <label for="email" class="block text-sm font-semibold">Email</label>
            <input v-model="email" type="email" id="email" placeholder="Email" class="w-full p-2 border rounded" required />
          </div>
  
          <div class="mb-6">
            <label for="password" class="block text-sm font-semibold">Password</label>
            <input v-model="password" type="password" id="password" placeholder="Password" class="w-full p-2 border rounded" required />
          </div>
  
          <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600">Login</button>
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
  