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
import { listTeams } from "./services/teamAPI";
const cookie = useCookiesStore()
const token = cookie.getCookie('token')
// if (token) {
onMounted(() => {
  console.log("Cargando perfil...");
});
// }
</script>

<style scoped></style>
