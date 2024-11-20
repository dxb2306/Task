const { defineConfig } = require('@vue/cli-service');
module.exports = defineConfig({
  devServer: {
    port: 8081,
    proxy: {
      '/api': {
        target: 'http://backend:8080', // Reference backend service name from Docker Compose
        changeOrigin: true,
        pathRewrite: { '^/api': '' },
      },
    },
  },
});
