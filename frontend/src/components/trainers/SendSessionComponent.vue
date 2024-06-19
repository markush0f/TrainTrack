<template>
  <div class="border-solid border-2 border-gray-100 rounded-md overflow-hidden p-2" v-if="playerStore.player != null">
    <form @submit.prevent="submitForm">
      <h3 v-if="playerStore.player != null">Enviar mensaje a {{ playerStore.player.name }} {{
    playerStore.player.surname }}</h3>
      <div class="pt-2">
        <input type="text" v-model="data.title"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5 dark:placeholder-gray-400"
          placeholder="Asunto..." required />
      </div>
      <div class="pb-2 pt-2">
        <input type="text" v-model="data.session"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5 dark:placeholder-gray-400"
          placeholder="Sesión..." required />
      </div>
      <div class="pb-2 pt-2 flex justify-center">
        <button type="submit"
          class="px-5 py-2.5 font-medium bg-green-200 hover:bg-green-300 hover:text-green-600 text-green-500 rounded-lg text-xs mr-4">Enviar</button>
        <!-- Cambia el tipo de botón de "submit" a "button" -->
        <button type="button" @click="cancelSession"
          class="px-5 py-2.5 font-medium bg-red-200 hover:bg-red-300 hover:text-red-600 text-red-500 rounded-lg text-xs">Cancelar</button>
      </div>
    </form>
  </div>
  <div v-else>
    <SendGlobalEvent />
  </div>
</template>

<script setup>
// MOSTRAR EN EL MENSAJE A QUIEN VA ENVIADO EL MENSAJE, PULSANDO EN LA LISTA DE JUGADORES
import { ref } from 'vue'
import { sendSession } from '@/services/trainerAPI';
import { usePlayerStore } from '@/stores/players';
import SendGlobalEvent from '@/components/trainers/SendGlobalEvent.vue'
const playerStore = usePlayerStore()
const data = ref({
  'title': '',
  'session': '',
  'player_id': ''
});


const submitForm = async () => {
  data.value.player_id = playerStore.player.id
  console.log("Data:", data.value);
  sendSession(data.value)
};

const cancelSession = () => {
  playerStore.player = null
  data.value.title = '';
  data.value.session = '';
};

</script>