<template>
  <nav>
    <RouterLink to="/login">Go to Login</RouterLink>-
    <RouterLink to="/">Go to Home</RouterLink>-
    <RouterLink to="/signup">Register</RouterLink>-
    <RouterLink to="/about">Go to About</RouterLink>-
    <RouterLink to="/trainers">Go to Trainers</RouterLink>
<<<<<<< HEAD
    
    <form action="" method="POST">
      <input type="submit" value="Test">
    </form>
=======
    <div>

      <input type="text" data-bs-theme="dark" name="name" v-model="name">
      <button @click="sendName">Enviar</button>
    </div>
>>>>>>> main
  </nav>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue'
// import URL_API from "../../variables";
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
const name = ref("");

function sendName() {
  const data = {
    "Name": name.value
  }
  axios.post(`http://127.0.0.1:8000/api/createuser`, data)
    .then(res => {
      console.log(data.Name)
      console.log("Respuesta del servidor: ", res.data);
    })
    .catch(error => {
      console.log("Error: ", error);
    })
}
</script>
