<template>
  <!-- CREAR UNA TABLA CON LA INFORMACIÓN DE CADA JUGADOR, ESTA INFORMACIÓN LA PONDRÁ EL ENTRENADOR -->
  <h2 class="text-lg font-bold mb-4">Jugadores</h2>
  <ul class="w-full">
    <li class="flex items-center justify-between border-b border-gray-300 py-2">
      <span>Jugador 1</span>
      <span>Nº 1</span>
    </li>
    <li v-for="player in players" class="flex items-center justify-between border-b border-gray-300 py-2">
      <span>Nombre: {{ player.name }}</span>
      <span>Apellidos: {{ player.surname }}</span>
    </li>
  </ul>

</template>

<script setup>
import { listPlayers } from '@/services/playersAPI';
import { onMounted, ref } from 'vue';
const players = ref([])
const playerById = ref(0)
onMounted(async () => {
  players = listPlayers();
});
function showPlayer(id) {
  playerById = id
} 
</script>