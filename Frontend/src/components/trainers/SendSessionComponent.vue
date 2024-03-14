<template>
  <form @submit.prevent="submitForm">
    <div class="p-2">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="Asunto">Asunto</label>
      <input type="text" name="Asunto" id="inputAsunto" cols="70" placeholder="Introduce el asunto..."
        v-model="data.title">
    </div>

    <div class="p-2">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="Motivo">Sesión</label>
      <input type="text"
        class="appearance-none block w-full bg-gray-200 text-gray-700 border border-black-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
        name="Sesion" id="inputSesion" placeholder="Introduce la sesión..." v-model="data.session">
    </div>
    <div class="p-2">
      <input type="submit" value="Enviar"
        class="bg-main-green hover:bg-green-700 text-white font-bold py-2 px-4 rounded-full" />
    </div>
  </form>
</template>
<script setup>
// MOSTRAR EN EL MENSAJE A QUIEN VA ENVIADO EL MENSAJE, PULSANDO EN LA LISTA DE JUGADORES
import { ref } from 'vue'
import { sendSession } from '@/services/trainerAPI';

const data = ref({
  'title': '',
  'session': '',
  'player_id': ''
})
const submitForm = async () => {
  sendSession(data.value)

};

</script>