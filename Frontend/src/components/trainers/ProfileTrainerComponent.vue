<template>
  <div class="container mx-auto px-4 py-8">
    <div class="max-w-lg mx-auto bg-white rounded-lg shadow-lg overflow-hidden">
      <!-- Encabezado del perfil -->
      <div class="bg-main-green text-white px-6 py-4">
        <div class="flex items-center justify-between">
          <h1 class="text-2xl ">Perfil de Entrenador</h1>
          <button class="mr-4" @click="profileStore.show = false"><i class="material-icons">close</i></button>
        </div>
      </div>

      <div class="p-6">

        <div class="flex items-center justify-center mb-6">
          <img src="" alt="" class="w-24 h-24 rounded-full">
        </div>
        <div class="mb-6 p-5">
          <p class="text-lg font-semibold p-2 pr-3">Nombre y apellidos: {{ profileData.name }} {{ profileData.surname }}
          </p>
          <p class="text-gray-600 p-2 pr-3">Correo electrónico: {{ profileData.email }}</p>
          <p class="text-gray-600 p-2 pr-3">Ubicación: {{ profileData.address1 }}, {{ profileData.address2 }}</p>
          <p class="text-gray-600 p-2 pr-3">Equipo: {{ profileData.team }}</p>
          
        </div>
        <div>
        </div>

      </div>
    </div>
  </div>
</template>
<script setup>

import { useProfileStore } from '@/stores/profile';
// Cambiar la solicitud a app para que no realize una peticion cada vez que pulse en el perfil
const profileStore = useProfileStore();
const profileData = profileStore.data

</script>
<style scoped></style>