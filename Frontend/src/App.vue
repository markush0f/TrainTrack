<template>
  <!-- <NavBar/> -->
  <RouterView />

</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import { ref, onMounted } from "vue";
import { profile } from '@/services/userAPI';
import { useCookiesStore } from "./stores/cookies";
import { useProfileStore } from "./stores/profile";
const cookie = useCookiesStore()
const token = cookie.getCookie('token')
if (token) {
  onMounted(() => {
    console.log("Cargando perfil...");
    profile()
  });
}
</script>

<style scoped></style>
