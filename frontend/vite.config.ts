import { fileURLToPath, URL } from 'node:url'

import { defineConfig, loadEnv } from 'vite';
import vue from '@vitejs/plugin-vue';
const env = loadEnv(process.cwd(), '');


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host: env.VITE_SERVER_HOST || "localhost",
    port: Number(env.VITE_SERVER_PORT || "3000"),
  },
});
