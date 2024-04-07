<template>
  <div v-if="notificationsStore.notifications && notificationsStore.notifications.length > 0"
    class="justify-center p-3">
    <h2 class="text-center font-bold mb-4">Notificaciones recientes</h2>
    <div class="w-full p-2 max-h-60 overflow-y-auto">
      <div class="b p-4 rounded-lg">
        <div class="mb-3">
          <div v-for="(notification, i) in notificationsStore.notifications" :key="i">
            <div v-if="i % 2 === 0" class="flex mb-3 items-center justify-center">
              <div class="w-5/12 border border-main-green p-4 rounded-lg mr-3" :key="notification.id">
                <div class="relative">
                  <h3 class="font-bold text-base mb-1">{{ notification.title }}</h3>
                  <button @click="deleteNotification(notification.id)"
                    class="absolute text-lg font-bold top-0 right-0 -mt-3 -mr-1 text-gray-300 hover:text-red-500 focus:outline-none">
                    X
                  </button>
                </div>
                <p class="text-sm">{{ notification.notification }}.</p>
                <span class="text-xs">{{ notification.created_at }}</span>
              </div>

              <div class="w-5/12 border border-main-green p-4 rounded-lg mr-3"
                v-if="notificationsStore.notifications[i + 1]" :key="notificationsStore.notifications[i + 1].id">
                <div class="relative">
                  <h3 class="font-bold text-base mb-1">{{ notificationsStore.notifications[i + 1].title }}</h3>
                  <button @click="deleteNotification(notificationsStore.notifications[i + 1].id)"
                    class="absolute text-lg font-semibold top-0 right-0 -mt-3 -mr-1 text-gray-300 hover:text-red-500 focus:outline-none">
                    X
                  </button>
                </div>
                <p class="text-sm">{{ notificationsStore.notifications[i + 1].notification }}</p>
                <span class="text-xs">{{ notificationsStore.notifications[i + 1].created_at }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <h2 class="text-center font-bold mb-4">No hay notificaciones recientes</h2>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { listNotifications, removeNotification } from '@/services/trainerAPI';
import { useNotificationsStore } from '@/stores/notifications.js'

const notificationsStore = useNotificationsStore()

async function deleteNotification(id) {
  console.log("Eliminando notificación con id: ", id);
  try {
    const success = await removeNotification(id);
    if (success) {
      notificationsStore.notifications = notificationsStore.notifications.filter(notification => notification.id !== id);
    } else {
      console.error("No se pudo eliminar la notificación con ID ", id);
    }
  } catch (error) {
    console.error("Error al eliminar la notificación:", error);
  }
}

onMounted(async () => {
  await listNotifications();
  console.log(notificationsStore.notifications);
});

</script>