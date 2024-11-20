# Use Node.js base image
FROM node:16-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json /app/
RUN npm install

# Copy the rest of the frontend code
COPY . /app/

# Expose the port Vue runs on
EXPOSE 8081

# Run the Vue development server
CMD ["npm", "run", "serve"]
