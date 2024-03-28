<template>
  <div class="min-h-screen">
    <NavbarComponent />
    <div class="flex mt-16"> <!-- Ajuste el margin-top según sea necesario -->
      <!-- div que recoge el escudo y la clasificacion -->
      <div class="flex flex-col gap-4 h-screen p-6">
        <!-- div del Escudo del equipo -->
        <!-- <div class="justify-center p-4 border border-gray-400">
          aquí va el escudo del equipo
        </div> -->
        <!-- div de la clasificacion -->
        <div>
          <ClassificationTableComponent />
        </div>
      </div>
      <!-- div que recoge horarios de entrenamiento, ultimas noticias y mensajes a los padres -->
      <div class="flex-grow justify-center p-4">
        <!-- Calendario de entrenamiento-->
        <CalendarComponent />
        <!-- div de ultimas notificaciones -->
        <NotificationComponent class="border-b-4" />
        <!-- div de mensajes a los padres -->
        <div class="flex">
          <div class="flex p-4 border">
            <SendSessionComponentTrainer />
          </div>
          <div class="flex p-4 border">
            <RequestParentsComponents />
          </div>
        </div>
      </div>
      <div class="w-1/4 p-4">
        <ListPlayersComponent />
      </div>
    </div>
  </div>
</template>

<script setup>
import NavbarComponent from '@/components/layouts/NavbarComponent.vue';
import ClassificationTableComponent from '@/components/teams/ClassificationTableComponent.vue';
import NotificationComponent from '@/components/teams/NotificationComponent.vue';
import CalendarComponent from '@/components/teams/CalendarComponent.vue';
import ListPlayersComponent from '@/components/players/ListPlayersComponent.vue';
import SendSessionComponentTrainer from '@/components/trainers/SendSessionComponent.vue'
import RequestParentsComponents from '@/components/trainers/RequestsParentsComponent.vue';
import { listParentsByTrainer } from "@/services/parentsAPI";
import { onMounted, ref } from 'vue'

onMounted(() => {
  listParentsByTrainer()
})
</script>
<style scoped>
.logo {
  width: 200px;
}
</style>