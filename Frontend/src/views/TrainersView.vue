<template>
  <div>
    <table>
      <tr>
        <td>Nombre</td>
        <td>Apellidos</td>
      </tr>
      <tr v-for="trainer in trainers" :key="trainer.id">
        <td>{{trainer.name}}</td>
        <td>{{trainer.surname}}</td>
      </tr>
    </table>
  </div>
</template>
<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
const trainers = ref([]);
onMounted(() => {
  axios.get('http://127.0.0.1:8000/api/trainers/')
    .then(res => {
      console.log(res.data);
      trainers.value = res.data;
    })
    .catch(error => {
      console.log('Error al obtener los datos de los entrenadores:', error);
    });
});
</script>