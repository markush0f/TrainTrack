<template>
  <nav class="bg-white shadow dark:bg-white-800 text-black ">
    <div class="max-w-7x mx-auto px-4 py-1 flex items-center justify-between">
      <div class="flex items-center">
        <span class="text-3xl font-Blacker">Logo</span>
      </div>
      <!-- Links -->
      <div class="flex-1 flex justify-center">
        <!-- Rutas de prueba -->
        <router-link to="/" class="text-base px-3 py-2 hover:text-main-green">INICIO</router-link>
        <!-- <button @click="logout" class="text-base px-3 py-2 hover:text-main-green">Logout</button> -->
        <!-- CONDICION PARA SI ESTÁ REGISTRADO MOSTRAR SU PERFIL -->
      </div>
      <button @click=" profileStore.show = true" class="text-xl px-3 py-2 hover:text-main-green text-rigth">
        Perfil
    </button>
      <Modal v-if="profileStore.show" @close="profileStore.show = false" />
    </div>

  </nav>
</template>
<script setup>

import axios from 'axios';
import { ref } from 'vue'
import Modal from '@/components/Modal.vue';
const profileStore = useProfileStore();
import { useProfileStore } from '@/stores/profile';


</script>