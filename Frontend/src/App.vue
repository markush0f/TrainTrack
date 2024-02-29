<template>
  <NavBar/>
  <!-- En RouterView se mostrará la vista según la ruta actual-->
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import NavBar from "./components/layouts/NavbarComponent.vue"
</script>

<style scoped></style>
