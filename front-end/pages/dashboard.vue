<template>
    <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f8f8f8; padding: 30px;">
      <h1 style="font-size: 28px; font-weight: 500; color: #333; margin-bottom: 20px;">
        Clients & Quotes
      </h1>
  
      <!-- Add Client Button -->
      <UButton color="neutral" variant="outline">Button</UButton>
  
      <!-- Add Client Form -->
      <div v-if="showForm" style="background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); margin-bottom: 30px;">
        <div style="margin-bottom: 15px;">
          <label style="display: block; font-weight: 600; margin-bottom: 5px;">Name</label>
          <input v-model="newClient.name" type="text" style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px;" />
        </div>
  
        <div style="margin-bottom: 15px;">
          <label style="display: block; font-weight: 600; margin-bottom: 5px;">Email</label>
          <input v-model="newClient.email" type="email" style="width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px;" />
        </div>
  
        <div>
          <label style="display: block; font-weight: 600; margin-bottom: 5px;">Quotes</label>
          <div v-for="(quote, index) in newClient.quotes" :key="index" style="margin-bottom: 10px;">
            <input v-model="quote.quote_text" type="text" placeholder="Quote text"
              style="width: 65%; padding: 8px; margin-right: 5px; border: 1px solid #ccc; border-radius: 6px;" />
            <input v-model="quote.amount" type="number" placeholder="Amount"
              style="width: 30%; padding: 8px; border: 1px solid #ccc; border-radius: 6px;" />
          </div>
          <button @click="addQuoteField" style="margin-top: 8px; font-size: 14px; color: #2563eb;">+ Add another quote</button>
        </div>
  
        <button @click="submitClient"
          style="margin-top: 20px; background-color: #10b981; color: white; padding: 10px 20px; border: none; border-radius: 6px; cursor: pointer;">
          Submit Client
        </button>
      </div>
  
      <!-- Loading -->
      <div v-if="loading" style="color: #777; font-style: italic;">
        Loading clients...
      </div>
  
      <!-- Empty -->
      <div v-else-if="clients.length === 0" style="color: #777; font-style: italic;">
        No clients found.
      </div>
  
      <!-- Clients Table -->
      <div v-else style="overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; background-color: #fff; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05); border-radius: 8px; overflow: hidden;">
          <thead style="background-color: #f2f2f2;">
            <tr>
              <th style="padding: 15px; text-align: left;">Client</th>
              <th style="padding: 15px; text-align: left;">Email</th>
              <th style="padding: 15px; text-align: left;">Quotes</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="client in clients" :key="client.id">
              <td style="padding: 15px;">{{ client.name }}</td>
              <td style="padding: 15px;">{{ client.email }}</td>
              <td style="padding: 15px;">
                <ul v-if="client.quotes && client.quotes.length" style="list-style: none; padding: 0;">
                  <li v-for="quote in client.quotes" :key="quote.id" style="margin-bottom: 8px;">
                    <strong>{{ quote.quote_text }}</strong><br />
                    <small>Amount: {{ quote.amount }}</small>
                  </li>
                </ul>
                <div v-else style="color: #999; font-style: italic;">No quotes available</div>
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
  