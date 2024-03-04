<template>
  <nav>
    <RouterLink to="/">Go to Home</RouterLink>-
    <RouterLink to="/signup">Register</RouterLink>-
    <RouterLink to="/about">Go to About</RouterLink>
    <RouterLink to="/trainers">Go to Trainers</RouterLink>
    <form action="" method="POST">
      <input type="submit" value="Test">
    </form>
  </nav>
</template>

<script setup>
import axios from 'axios';
// import URL_API from "../../variables";
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const data = {
  "Respuesta": "recibida"
}
axios.post(`http://127.0.0.1:8000/api/createuser`, data)
  .then(res => {
    console.log(res.data);
  })
  .catch(error => {
    console.log("Error: ", error);
  })

</script>
