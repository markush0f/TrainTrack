<template>
  <div>
    <h2 class="text-lg font-bold text-center p-1">Enviar aviso al entrenador</h2>
    <form @submit.prevent="submitFormNotices">
      <select @change="selectNotice($event)">
        <option readonly class="text-gray-50">Enviar aviso</option>
        <option value="notNextTrain">No asisto al próximo entrenamieto</option>
        <option value="lateNextTrain">Llego tarde al próximo entrenamiento</option>
        <option value="notNextMatch">No asisto al próximo partido</option>
        <option value="lateNextMatch">Llego tarde al próximo partifo</option>
      </select><br><br>
      <input type="submit" value="Enviar"
        class="bg-main-green hover:bg-green-700 text-white font-bold py-2 w-full rounded-full" />
    </form>
  </div>
</template>

<script setup>
// ESTABLECER LA CANTIDAD DE TIEMPO QUE LLEGARÁ TARDE
import { ref } from 'vue';
const notice = ref('')

const selectNotice = (event) => {
  notice.value = event.target.value;
};

function submitFormNotices() {

}
</script>