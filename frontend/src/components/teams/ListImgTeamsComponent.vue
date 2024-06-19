<template>
  <div>
    <img v-for="shield in shields" :src="shield" alt="">
    <!-- MANUALMENTE SI SE VE -->
    <!-- <img src="../../img/Shields/Atalaya.png" alt=""> -->
  </div>
</template>



<script setup>

import { ref } from 'vue';
const route = "../img/Shields/"
const shields = [
  "../../img/Shields/Atalaya.png"

];


</script>