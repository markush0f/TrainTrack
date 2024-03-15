<template>
  <div class="justify-center p-3  ">
    <h2 class="text-center font-bold mb-4">Notificaciones recientes</h2>
    <div class="w-full p-2 max-h-60 overflow-y-auto">
      <div class="b p-4 rounded-lg ">
        <div class="mb-3">
          <div v-for="notification in notifications" class="border border-main-green p-4 rounded-lg mb-3">
            <h3 class="font-bold text-lg mb-1">{{ notification.title }}</h3>
            <p>{{ notification.notification }}</p>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>
<script setup>
import { onMounted, ref } from 'vue'
import { listNotifications } from '@/services/trainerAPI';
const notifications = ref([])
onMounted(async () => {
  notifications.value = await listNotifications()
  console.log("Notificaciones del entrenador: ",notifications.value);
});



</script>