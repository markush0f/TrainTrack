<template>
  <br>
  <div>
    <p>Registro de equipo: </p>
    <br>
    <form @submit.prevent="submitForm">
      <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputName">Codigo</label>
        <input
          class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
          type="text" name="name" id="inputName" placeholder="Insert your name..." v-model="formData.password">
        <p class="text-red-500 text-xs italic">Error.</p>
      </div>
      <br>
      <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
          for="inputPassword">Contraseña</label>
        <input
          class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
          name="password" id="inputPassword" type="password" placeholder="******************"
          v-model="formData.codeTeam">

      </div>
      <input type="submit"  @onclick="submitForm" value="Entrar"
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
const formData = ref({
  codeTeam: '',
  password: '',
})
const submitForm = async () => {
  console.log(formData.value);
  try {
    const res = await axios.post("http://127.0.0.1:8000/api/checkcodeteam", formData.value);
    console.log("Datos enviados", res.data);
    // Comprobamos si la res tieen una redireccion
    if (res.data.redirect) {
      console.log("Hay redireccion");
      window.location.href = res.data.redirect
    } else {
      console.log("No hay redireccion");
    }
  } catch (e) {
    console.log("ERROR", e);
  }
}

</script>