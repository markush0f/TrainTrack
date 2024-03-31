<template>
  <div class="min-h-screen">
    <NavbarComponent />
    <div class="flex flex-col md:flex-row mt-16">
      <!-- División izquierda: Escudo del equipo y Clasificación -->
      <div class="flex flex-col gap-4 md:w-1/4 h-full p-6">
        <!-- Escudo del equipo -->
        <!-- <div class="justify-center p-4 border border-gray-400">
          aquí va el escudo del equipo
        </div> -->
        <!-- Clasificación -->
        <div>
          <ClassificationTableComponent />
        </div>
      </div>
      <!-- División central: Calendario de entrenamiento, últimas notificaciones y mensajes -->
      <div class="flex-grow justify-center p-4">
        <!-- Calendario de entrenamiento -->
        <CalendarComponent />
        <!-- Últimas notificaciones -->
        <NotificationComponent class="border-b-4" />
        <!-- Mensajes a los padres -->
        <div class="flex p-4 border">
          <SendSessionComponentTrainer />
        </div>
        <p class="text-center text-gray-400 text-2xl">Seleccione un jugador para acceder a sus características</p>
      </div>
      <!-- División derecha: Lista de jugadores y padres no verificados -->
      <div class="w-full md:w-1/4 p-4">
        <ListPlayersComponent />
        <br>
        <ListUnverifiedParents />
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
import ListUnverifiedParents from '@/components/parents/ListUnverifiedParents.vue'
import { listParentsByTrainer, getUnverifiedParents } from "@/services/parentsAPI";
import { onMounted, ref } from 'vue'


onMounted(async () => {
  listParentsByTrainer()
})
</script>
<style scoped>
.logo {
  width: 200px;
}
</style>