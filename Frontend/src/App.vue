<template>
  <NavBar/>
  <!-- En RouterView se mostrará la vista según la ruta actual-->
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import NavBar from "./components/layouts/NavbarComponent.vue"
const URL_API = "http://127.0.0.1:8000/api";
</script>

<style scoped>

</style>
