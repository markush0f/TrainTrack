<template>
  <div>
    <transition name="fade">
      <div
        v-if="removePlayerStore.showRemovePlayer"
        class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50"
      >
        <div class="bg-white p-6 rounded-md shadow-lg">
          <p class="text-lg font-semibold mb-4">
            ¿Estás seguro de eliminar al jugador?
          </p>
          <div class="flex justify-end">
            <button
              @click="removePlayerStore.showRemovePlayer = false"
              class="text-gray-500 hover:text-gray-700"
            >
              Cancelar
            </button>
            <button
              @click="removePlayerModal()"
              class="ml-4 bg-red-500 text-white px-4 py-2 rounded-md"
            >
              Eliminar
            </button>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { useRemovePlayerStore, usePlayerStore } from "@/stores/players";
import { removePlayer } from "@/services/playersAPI";
const playerStore = usePlayerStore();
const removePlayerStore = useRemovePlayerStore();

async function removePlayerModal() {
  removePlayerStore.showRemovePlayer = false
  const data = {
    id: playerStore.playerToRemove.id,
  };
  console.log(data);
  await removePlayer(data);
}

</script>
