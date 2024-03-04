<template>
  <nav>
    <RouterLink to="/login">Go to Login</RouterLink>-
    <RouterLink to="/">Go to Home</RouterLink>-
    <RouterLink to="/signup">Register</RouterLink>-
    <RouterLink to="/about">Go to About</RouterLink>-
    <RouterLink to="/trainers">Go to Trainers</RouterLink>
    
    <form action="" method="POST">
      <input type="submit" value="Test">
    </form>
  </nav>
</template>

<script setup>
import axios from 'axios';
import URL_API from "../../App.vue";

const data = {
  "Respuesta": "recibida"
}
axios.post(`http://127.0.0.1:8000/api/createtrainer`, data)
  .then(res => {
    console.log("Respuesta del backend: ", res.data);
  })
  .catch(error => {
    console.log("Error: ", error);
  })

</script>
