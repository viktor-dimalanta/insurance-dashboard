<template>
    <div class="p-6">
      <h1 class="text-2xl font-bold mb-4">Clients & Quotes</h1>
  
      <!-- Loading state -->
      <div v-if="loading" class="text-gray-500">Loading clients...</div>
  
      <!-- No clients found -->
      <div v-else-if="clients.length === 0" class="text-gray-500">No clients found...</div>
  
      <!-- Display clients and their quotes -->
      <div v-else>
        <ul class="space-y-2">
          <li
            v-for="client in clients"
            :key="client.id"
            class="p-4 bg-white shadow rounded-md"
          >
            <p class="font-semibold">{{ client.name }} ({{ client.email }})</p>
            
            <!-- Displaying client quotes -->
            <div v-if="client.quotes && client.quotes.length > 0">
              <ul class="space-y-2 mt-2">
                <li
                  v-for="quote in client.quotes"
                  :key="quote.id"
                  class="p-2 bg-gray-50 rounded-md"
                >
                  <p class="text-sm font-semibold">{{ quote.quote_text }}</p>
                  <p class="text-xs text-gray-500">Amount: {{ quote.amount }}</p>
                </li>
              </ul>
            </div>
            <div v-else class="text-sm text-gray-400">No quotes available</div>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue'
  
  const clients = ref<any[]>([])
  const loading = ref(true)
  
  const fetchClients = async () => {
    try {
        console.log('Fetching clients...')
        
        // Use the mock token from the store or localStorage
        const token = useAuthStore().getToken()
        
        if (!token) {
        console.error('No authentication token found')
        return
        }
        
        // Fetch clients data using the mock token
        const clientsData = await $fetch('http://localhost:8000/clients', {
        headers: {
            Authorization: `Bearer ${token}`  // Include the mock token in the request
        }
        })
        
        console.log('Clients data:', clientsData)

        // Fetch quotes for each client
        for (const client of clientsData) {
        const quotes = await $fetch(`http://localhost:8000/clients/${client.id}/quotes`, {
            headers: {
            Authorization: `Bearer ${token}`  // Add the mock token for quotes request
            }
        })
        client.quotes = quotes // Add quotes to client data
        }
        
        clients.value = clientsData
    } catch (error) {
        console.error('Failed to fetch data:', error)
    } finally {
        loading.value = false
    }
    }

  onMounted(fetchClients)
  </script>
  
  <style scoped>
  /* You can add your styles here */
  </style>
  