<template>
  <nav class="bg-white shadow dark:bg-gray-800 text-black">

    <div class="max-w-7x mx-auto px-4 py-3 flex items-center justify-between">
      <div class="flex items-center">
        <span class="text-3xl font-Blacker">Logo</span>
      </div>
      <!-- Links -->
      <div class="flex-1 flex justify-center">
        <!-- Rutas de prueba -->
        <router-link to="/" class="text-3xl px-3 py-2 hover:bg-green-300">Home</router-link>
        <router-link to="/trainer" class="text-3xl px-3 py-2 hover:bg-green-300">Trainer</router-link>
        <router-link to="/parent" class="text-3xl px-3 py-2 hover:bg-green-300">Parent</router-link>

        <button @click="logout" class="text-3xl px-3 py-2">Logout</button>
      </div>
    </div>
  </nav>
  <nav class="bg-gray-800 shadow dark:bg-gray-800">
    <div class="flex items-center">
      <span class="text-xl font-Blacker">

      </span>
    </div>
  </nav>
  <CodeTeamComponent />
</template>
<script setup>
import axios from 'axios';
import { ref } from 'vue'
import { useTokenUserStore } from '@/stores/JWT';
import { useUrlAPIStore } from '@/stores/URL';
import CodeTeamComponent from "./CodeTeamComponent.vue"

const logout = async () => {
  try {
    const res = await axios.post("http://127.0.0.1:8000/api/logout")
    headers: {
      Authorization: `Bearer ${useTokenUserStore.getToken}`
    }
    console.log("Respuesta del servidor", res.data);
  } catch (e) {
    console.log("Error: ", e);
  }

}

</script>