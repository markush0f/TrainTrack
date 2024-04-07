<template>
  <div class="container mx-auto px-4 py-8">
    <div class="max-w-lg mx-auto bg-white rounded-lg shadow-lg overflow-hidden">
      <!-- Encabezado del perfil -->
      <div class="bg-main-green text-white px-6 py-4">
        <div class="flex items-center justify-between">
          <h1 class="text-2xl ">Perfil de Padre</h1>
          <button class="mr-4" @click="profileStore.show = false"><i class="material-icons">close</i></button>
        </div>
      </div>

      <div class="p-6">

        <div class="flex items-center justify-center mb-6">
          <img src="" alt="" class="w-24 h-24 rounded-full">
        </div>
        <div class="mb-6">
          <p class="text-lg font-semibold">Nombre y apellidos</p>
          <p class="text-lg font-semibold"> </p>
          <p class="text-gray-600">Correo electrónico: </p>
          <p class="text-gray-600">Ubicación: </p>
          <p class="text-gray-600">Equipo: </p>
        </div>
        <div class="mb-6">
          <p class="text-lg font-semibold">Hijos</p>
          <p class="text-gray-600">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent
            libero. Sed cursus ante dapibus diam.</p>
        </div>

      </div>
    </div>
  </div>
</template>
<script setup>
import { useProfileStore } from '@/stores/profile';
import axios from 'axios';
import { onMounted } from 'vue';
const profileStore = useProfileStore();
import { profile } from '@/services/userAPI';
onMounted(async () => {
  profile()
});
</script>
<style scoped></style>