<template>
  <NavbarComponent />
  <div class="flex h-full">
    <!-- div que recoge el escudo y la clasificacion -->
    <div class="flex flex-col gap-4 h-screen p-6 ">
      <!-- div del Escudo del equipo -->
      <div class="justify-center p-4 border border-gray-400">
        <img src="https://www.dyntra.org/new/wp-content/uploads/2018/07/federacion-canaria-futbol.jpg" alt="Federacion"
          class="logo">
      </div>
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
      <NotificationComponent />
      <!-- div de mensajes a los padres -->
      <div class="flex p-4 border border-gray-400">
        <SendSessionComponent/>
      </div>
    </div>
    <div class="w-1/4 p-4">
      <ListPlayersComponent />
    </div>
  </div>



</template>
<script setup>
import NavbarComponent from '@/components/layouts/NavbarComponent.vue';
import ClassificationTableComponent from '@/components/teams/ClassificationTableComponent.vue';
import NotificationComponent from '@/components/teams/NotificationComponent.vue';
import CalendarComponent from '@/components/teams/CalendarComponent.vue';
import ListPlayersComponent from '@/components/players/ListPlayersComponent.vue';

import SendSessionComponent from '@/components/trainers/SendSessionComponent.vue'
import ProfileTrainerComponent from '@/components/trainers/ProfileTrainerComponent.vue';
import { onMounted, ref } from 'vue'


</script>
<style scoped>
.logo {
  width: 200px;
}
</style>