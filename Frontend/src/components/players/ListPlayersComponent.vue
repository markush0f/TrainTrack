<template>
  <div>
    <h2 class="text-lg font-bold mb-4">Jugadores</h2>
    <ul class="w-full">
      <li v-for="player in playerStore.players" :key="player.id"
        class="flex items-center justify-between border-b border-gray-300 py-2">
        <span> {{ player.name }} {{ player.surname }}</span>
        <button>
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
            stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M15 9h3.75M15 12h3.75M15 15h3.75M4.5 19.5h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Zm6-10.125a1.875 1.875 0 1 1-3.75 0 1.875 1.875 0 0 1 3.75 0Zm1.294 6.336a6.721 6.721 0 0 1-3.17.789 6.721 6.721 0 0 1-3.168-.789 3.376 3.376 0 0 1 6.338 0Z" />
          </svg>
        </button>
        <button @click="selectMessagePlayer(player)">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
            stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 0 1 .865-.501 48.172 48.172 0 0 0 3.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z" />
          </svg>
        </button>
      </li>
      <li class="flex items-center justify-between border-b border-gray-300 py-2">
        <button @click="storeShowPlayer.showInsertPlayer = true"
          class="flex-grow bg-gray-400 hover:bg-gray-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Nuevo
          jugador</button>
      </li>
    </ul>

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

onMounted(async () => {
  await listPlayers()
});


</script>