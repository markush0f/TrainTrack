<template>
  <div>
    <h2 class="text-lg font-bold mb-4">Jugadores</h2>
    <ul class="w-full">
      <li class="flex items-center justify-between border-b border-gray-300 py-2">
        <span>Jugador 1</span>
        <span>Nº 1</span>
      </li>
      <li v-for="player in players" :key="player.id"
        class="flex items-center justify-between border-b border-gray-300 py-2">
        <span> {{ player.name }} {{ player.surname }}</span>
      </li>
      <li class="flex items-center justify-between border-b border-gray-300 py-2">
        <button @click="storePlayer.showInsertPlayer = true"
          class="flex-grow bg-gray-400 hover:bg-gray-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Nuevo
          jugador</button>
      </li>
    </ul>

    <div v-if="storePlayer.showInsertPlayer" @close="storePlayer.showInsertPlayer = false"
      class="fixed top-0 left-0 flex items-center justify-center w-full h-full bg-black bg-opacity-50">
      <InsertPlayerComponent />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import InsertPlayerComponent from './InsertPlayerComponent.vue';
import { listPlayers, loadListPlayer } from '@/services/playersAPI';
import { useShowInsertPlayerStore } from '@/stores/players';
 
const storePlayer = useShowInsertPlayerStore();
const players = ref([]);



onMounted( async () => {
  players.value = await listPlayers()
  // console.log(players.value);
});


</script>