# Use an official Node.js runtime as a parent image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files to the working directory
COPY . .

# Build the React app
RUN npm run build

# Install serve to serve the static files
# RUN npm install -g serve

# Expose the port the app runs on
EXPOSE 3000

# Start the app (prod build)
# CMD ["serve", "-s", "dist", "-l", "3000"]

# start react dev server
CMD ["npm", "run", "dev"]