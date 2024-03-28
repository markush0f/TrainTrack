<template>
  <div class="border-solid border-2 border-third-green rounded-md overflow-hidden p-2"
    v-if="playerStore.playerMsg != null">
    <form @submit.prevent="submitForm">
      <h3 v-if="playerStore.playerMsg != null">Enviar mensaje a {{ playerStore.playerMsg.name }} {{
      playerStore.playerMsg.surname }}</h3>
      <div class="pt-2">
        <input type="text" id="title" v-model="data.title"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5  dark:placeholder-gray-400 "
          placeholder="Asunto..." required />
      </div>
      <div class="pb-2 pt-2">
        <input type="text" id="title" v-model="data.session"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5  dark:placeholder-gray-400 "
          placeholder="Sesión..." required />
      </div>
      <div class="pb-2 pt-2 ">
        <button
          class="px-5 py-2.5 font-medium bg-green-200 hover:bg-green-300 hover:text-green-600 text-green-500 rounded-lg text-xs">
          Enviar
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
// MOSTRAR EN EL MENSAJE A QUIEN VA ENVIADO EL MENSAJE, PULSANDO EN LA LISTA DE JUGADORES
import { ref } from 'vue'
import { sendSession } from '@/services/trainerAPI';
import { usePlayerStore } from '@/stores/players';
const playerStore = usePlayerStore()
const data = ref({
  'title': '',
  'session': '',
  'player_id': ''
});

const submitForm = async () => {
  sendSession(data.value)
};

</script>