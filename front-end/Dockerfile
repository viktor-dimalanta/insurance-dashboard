# Use official Node.js LTS image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy only package files first for caching
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy rest of the project
COPY . .

# Build the Nuxt app for production
RUN npm run build

# Expose the default Nuxt port
EXPOSE 3000

# Start the Nuxt server
CMD ["npm", "run", "start"]
