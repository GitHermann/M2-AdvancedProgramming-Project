import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host: '0.0.0.0',
    proxy: {
      '/internships': {
        target: 'http://localhost:5001',
        changeOrigin: true
      },
      '/internship_spaces': {
        target: 'http://localhost:5002',
        changeOrigin: true
      },
      '/user': {
        target: 'http://localhost:5003',
        changeOrigin: true
      },
      '/documents': {
        target: 'http://localhost:5004',
        changeOrigin: true
      }
    },
    port: 8082
  },
})
