<template>
  <br>
  <div>
    <p>Registro de equipo: </p>
    <form @submit.prevent="submitForm">
      <p>
        <label for="">Código de equipo</label>
        <input type="text" v-model="formData.codeTeam">
      </p>
      <p>
        <label for="">Contraseña</label>
        <input type="text" v-model="formData.password">
      </p>
      <input type="submit" value="Enviar" class="btn btn-primary" @onclick="submitForm" />
    </form>
    <button>Volver</button>
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