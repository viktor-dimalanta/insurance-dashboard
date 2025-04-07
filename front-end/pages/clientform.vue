<template>
    <div class="form-container">
      <h2>Create Client and Add First Quote</h2>
      <form @submit.prevent="submitForm">
        <!-- Client Information -->
        <div>
          <label for="name">Name</label>
          <input v-model="newClient.name" id="name" type="text" required />
        </div>
        <div>
          <label for="email">Email</label>
          <input v-model="newClient.email" id="email" type="email" required />
        </div>
  
        <!-- Quote Information -->
        <div>
          <label for="quote_text">Quote Text</label>
          <input v-model="newQuote.quote_text" id="quote_text" type="text" required />
        </div>
        <div>
          <label for="amount">Amount</label>
          <input v-model="newQuote.amount" id="amount" type="number" required />
        </div>
  
        <!-- Submit Button -->
        <button type="submit">Create Client and Add Quote</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const newClient = ref({
    name: '',
    email: ''
  });
  
  const newQuote = ref({
    quote_text: '',
    amount: '',
    client_id: null // This will be set after client creation
  });
  
  const submitForm = async () => {
    try {
      // Step 1: Create the client
      const clientResponse = await fetch('http://localhost:8000/clients', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newClient.value)
      });
      const clientData = await clientResponse.json();
  
      if (clientResponse.ok) {
        // Step 2: Add the first quote for the newly created client
        newQuote.value.client_id = clientData.client.id; // Set client_id to the created client's ID
  
        const quoteResponse = await fetch('http://localhost:8000/quotes/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(newQuote.value)
        });
        const quoteData = await quoteResponse.json();
  
        if (quoteResponse.ok) {
          alert(`Client and first quote created successfully! Client ID: ${clientData.client.id}`);
          // Optionally reset form data or navigate to a different page
        } else {
          alert(`Error adding quote: ${quoteData.message}`);
        }
      } else {
        alert(`Error creating client: ${clientData.message}`);
      }
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    }
  };
  </script>
  
  <style scoped>
  .form-container {
    width: 300px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f7f7f7;
    border-radius: 8px;
  }
  form div {
    margin-bottom: 10px;
  }
  label {
    font-size: 14px;
    margin-bottom: 5px;
    display: block;
  }
  input {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  button {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  button:hover {
    background-color: #45a049;
  }
  </style>
  