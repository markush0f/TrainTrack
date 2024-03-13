import './assets/style.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import VueCookies from 'vue3-cookies'
import App from './App.vue'
import router from './router'
import axios from 'axios'
//import { useCSRFStore } from './stores/CSRF'


axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)
app.use(createPinia())
  .use(router, axios)
  .use(VueCookies, {
    expires: '7d'
  })

app.mount('#app')

