<template>
    <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f8f8f8; padding: 30px;">
      <h1 style="font-size: 28px; font-weight: 500; color: #333; margin-bottom: 30px; text-align: left;">
        Clients & Quotes
      </h1>
  
      <div v-if="loading" style="color: #777; font-style: italic;">
        Loading clients...
      </div>
  
      <div v-else-if="clients.length === 0" style="color: #777; font-style: italic;">
        No clients found.
      </div>
  
      <div v-else style="overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; background-color: #fff; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05); border-radius: 8px; overflow: hidden;">
          <thead style="background-color: #f2f2f2;">
            <tr>
              <th style="padding: 15px; text-align: left; font-weight: 600; color: #555; border-bottom: 1px solid #ddd;">Client</th>
              <th style="padding: 15px; text-align: left; font-weight: 600; color: #555; border-bottom: 1px solid #ddd;">Email</th>
              <th style="padding: 15px; text-align: left; font-weight: 600; color: #555; border-bottom: 1px solid #ddd;">Quotes</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="client in clients" :key="client.id" style="transition: background-color 0.2s ease;">
              <td style="padding: 15px; color: #333;">
                <div style="font-weight: 500;">{{ client.name }}</div>
              </td>
              <td style="padding: 15px; color: #777;">{{ client.email }}</td>
              <td style="padding: 15px;">
                <div v-if="client.quotes && client.quotes.length > 0">
                  <ul style="list-style: none; padding: 0; margin: 0;">
                    <li v-for="quote in client.quotes" :key="quote.id"
                      style="background-color: #f9f9f9; border-radius: 6px; padding: 10px; margin-bottom: 8px; border: 1px solid #eee;">
                      <p style="font-size: 15px; font-weight: 500; color: #444; margin-bottom: 5px;">{{ quote.quote_text }}</p>
                      <p style="font-size: 13px; color: #888;">Amount: <span style="font-weight: 600; color: #555;">{{ quote.amount }}</span></p>
                    </li>
                  </ul>
                </div>
                <div v-else style="color: #999; font-style: italic; font-size: 14px;">No quotes available</div>
              </td>
            </tr>
          </tbody>
        </table>
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
  