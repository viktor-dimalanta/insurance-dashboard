# Use the official Node.js runtime as a base image
FROM node:lts-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock/pnpm-lock.yaml)
COPY package*.json ./
# If using Yarn: COPY yarn.lock ./
# If using pnpm: COPY pnpm-lock.yaml ./

# Install dependencies
RUN npm install --frozen-lockfile
# If using Yarn: RUN yarn install --frozen-lockfile
# If using pnpm: RUN pnpm install --frozen-lockfile

# Copy the rest of the application code
COPY . .

# Build the Nuxt application
RUN npm run build
# If using Yarn: RUN yarn build
# If using pnpm: RUN pnpm build

# Expose the port the Nuxt app runs on (default is 3000)
EXPOSE 3000

# Command to run the Nuxt application in production
CMD ["node", ".output/server/index.mjs"]