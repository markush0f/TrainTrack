<template>

  <!-- <NavBar/> -->
  <!-- En RouterView se mostrará la vista según la ruta actual-->
  <RouterView />
  
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import { ref } from "vue";
// import NavBar from "./components/layouts/NavbarComponent.vue"
import CodeTeamComponent from "./components/layouts/CodeTeamComponent.vue";
const URL_API = "http://127.0.0.1:8000/api";
const login = ref(false)

</script>

<style scoped></style>
