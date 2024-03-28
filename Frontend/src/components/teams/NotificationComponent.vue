<template>
  <div class="justify-center p-3">
    <h2 class="text-center font-bold mb-4">Notificaciones recientes</h2>
    <div class="w-full p-2 max-h-60 overflow-y-auto">
      <div class="b p-4 rounded-lg">
        <div class="mb-3">
          <template v-for="(notification, i) in notifications" :key="i">
            <div v-if="i % 2 === 0" class="flex mb-3 items-center justify-center">
              <div class="w-5/12 border border-main-green p-4 rounded-lg mr-3" :key="notification.id">
                <h3 class="font-bold text-base mb-1">{{ notification.title }}</h3>
                <p class="text-sm">{{ notification.notification }}.</p>
                <span class="text-xs">{{notification.created_at}}</span>
              </div>

              <div class="w-5/12 border border-main-green p-4 rounded-lg mr-3" v-if="notifications[i + 1]" :key="notifications[i + 1].id">
                <h3 class="font-bold text-base mb-1">{{ notification.title }}</h3>
                <p class="text-sm">{{ notification.notification }}.</p>
                <span class="text-sm">{{notification.created_at}}</span>
              </div>
            </div>
          </template>
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
});
</script>