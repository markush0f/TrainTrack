<template>
  <div>
    <h2 class="text-center font-bold mb-4 text-lg">Jugadores</h2>
    <ul class="w-full overflow-y-auto max-h-80">
      <li
        v-for="player in playerStore.players"
        :key="player.id"
        class="flex items-center justify-between border-b border-gray-300 py-1"
      >
        <span
          class="flex-grow"
          :class="{
            playerSelected:
              playerStore &&
              playerStore.player &&
              playerStore.player.id === player.id,
          }"
        >
          {{ player.name }} {{ player.surname }}
        </span>
        <i
          class="gg-user-remove cursor-pointer flex-shrink-0 text-main-green text-lg w-8 h-7 hover:text-green-500 mr-4"
          @click="removePlayerById(player)"
        >
        </i>
        <i
          class="fi-rr-file-user cursor-pointer flex-shrink-0 text-main-green text-lg w-8 h-8 hover:text-green-500"
          @click="selectPlayer(player)"
        ></i>
      </li>
    </ul>

    <button
      @click="storeShowPlayer.showInsertPlayer = true"
      class="w-full bg-gray-400 hover:bg-gray-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline mt-2"
    >
      Nuevo jugador
    </button>

    <div
      v-if="storeShowPlayer.showInsertPlayer"
      @close="storeShowPlayer.showInsertPlayer = false"
      class="fixed top-0 left-0 flex items-center justify-center w-full h-full bg-black bg-opacity-50"
    >
      <InsertPlayerComponent />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import InsertPlayerComponent from "./InsertPlayerComponent.vue";
import { listPlayers, removePlayer } from "@/services/playersAPI";
import {
  useShowInsertPlayerStore,
  usePlayerStore,
  useRemovePlayerStore,
} from "@/stores/players";

const playerStore = usePlayerStore();
const storeShowPlayer = useShowInsertPlayerStore();
const player = ref({});
const removePlayerStore = useRemovePlayerStore();
function selectPlayer(newPlayer) {
  playerStore.player = newPlayer;
  console.log(playerStore.player);
  player.value = newPlayer;
}

async function removePlayerById(player) {
  playerStore.playerToRemove = player;
  console.log(playerStore.playerToRemove);
  removePlayerStore.showRemovePlayer = true;
}

onMounted(async () => {
  await listPlayers();
  console.log("Jugadores: ", playerStore.players);
});
</script>

<style scoped lang="css">
.playerSelected {
  color: rgb(23, 149, 23);
  font-weight: bold;
}
</style>
