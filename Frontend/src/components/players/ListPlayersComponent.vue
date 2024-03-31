<template>
  <div>
    <h2 class="text-lg font-bold mb-4">Jugadores</h2>
    <ul class="w-full overflow-y-auto max-h-80">
      <li v-for="player in playerStore.players" :key="player.id"
        class="flex items-center justify-between border-b border-gray-300 py-1">
        <span class="flex-grow">{{ player.name }} {{ player.surname }}</span>

        <i class="fi fi-rr-envelope cursor-pointer flex-shrink-0 mr-2 text-main-green text-lg w-8 h-8 hover:text-green-700"
          @click="selectMessagePlayer(player)"></i>

        <i class="fi-rr-file-user cursor-pointer flex-shrink-0 text-main-green text-lg w-8 h-8 hover:text-green-700"
          @click="selectPlayer(player)"></i>
      </li>
    </ul>

    <button @click="storeShowPlayer.showInsertPlayer = true"
      class="w-full bg-gray-400 hover:bg-gray-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline mt-2 ">
      Nuevo jugador
    </button>

    <div v-if="storeShowPlayer.showInsertPlayer" @close="storeShowPlayer.showInsertPlayer = false"
      class="fixed top-0 left-0 flex items-center justify-center w-full h-full bg-black bg-opacity-50">
      <InsertPlayerComponent />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import InsertPlayerComponent from './InsertPlayerComponent.vue';
import { listPlayers } from '@/services/playersAPI';
import { useShowInsertPlayerStore, usePlayerStore } from '@/stores/players';

const playerStore = usePlayerStore();
const storeShowPlayer = useShowInsertPlayerStore();
const player = ref({});

function selectMessagePlayer(newPlayer) {
  console.log(newPlayer);
  playerStore.playerMsg = newPlayer;
  player.value = newPlayer;
}

function selectPlayer(newPlayer) {
  console.log("Player seleccionado: ", newPlayer);
  playerStore.player = newPlayer;
}


onMounted(async () => {
  await listPlayers()
});


</script>
