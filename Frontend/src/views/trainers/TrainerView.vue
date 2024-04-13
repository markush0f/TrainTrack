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
        <!-- Últimas notificaciones -->
        <ListNotificationsTrainerComponent class="border-b-4" />
        <!-- Mensajes a los padres -->
        <div class="flex flex-col p-4">
          <div v-if="playerStore.player != null">
            <PlayerInfoComponent />
            <SendSessionComponentTrainer />
            <PlayerStatsComponent />
          </div>
          <div v-else>
            <p class="text-center text-gray-400 text-2xl">Seleccione un jugador para acceder a sus características</p>
          </div>
        </div>
      </div>
      <!-- División derecha: Lista de jugadores y padres no verificados -->
      <div class="w-full md:w-1/4 p-4">
        <ListPlayersComponent />
        <br>
        <ListUnverifiedParents />
      </div>
    </div>
    <div>
    </div>
  </div>
</template>
<script setup>


import NavbarComponent from '@/components/layouts/NavbarComponent.vue';
import ClassificationTableComponent from '@/components/teams/ClassificationTableComponent.vue';
import ListNotificationsTrainerComponent from '@/components/trainers/ListNotificationTrainerComponent.vue'
import ListPlayersComponent from '@/components/players/ListPlayersComponent.vue';
import SendSessionComponentTrainer from '@/components/trainers/SendSessionComponent.vue'
import ListUnverifiedParents from '@/components/parents/ListUnverifiedParents.vue'
import { listParentsByTrainer } from "@/services/parentsAPI";
import PlayerInfoComponent from '@/components/players/PlayerInfoComponent.vue';
import PlayerStatsComponent from '@/components/players/PlayerStatsComponent.vue'
import { onMounted } from 'vue'
import { usePlayerStore } from '@/stores/players';
const playerStore = usePlayerStore();

onMounted(async () => {
  await listParentsByTrainer()
  console.log(playerStore.player);
})

</script>
<style scoped>
.logo {
  width: 200px;
}
</style>