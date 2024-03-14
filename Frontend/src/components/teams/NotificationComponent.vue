<template>
  <div class="justify-center p-3 border border-main-green">
    <h2 class="text-center font-bold mb-4">Notificaciones recientes</h2>
    <div class="w-full p-2 max-h-60 overflow-y-auto">
      <div class="b p-4 rounded-lg ">
        <div class="mb-3">
          <div class="border border-main-green p-4 rounded-lg">
            <h3 class="font-bold text-lg mb-1">Título de la notificación 1</h3>
            <p>Descripción de la notificación 1</p>
          </div>
        </div>
        <div class="mb-8">
          <div class="border border-main-green p-4 rounded-lg">
            <h3 class="font-bold text-lg mb-2">Título de la notificación 2</h3>
            <p>Descripción de la notificación 2</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue';
import { listNotifications } from '@/services/trainerAPI';
const notifications = ref([]);


</script>