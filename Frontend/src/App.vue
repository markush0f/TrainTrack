<template>
  <!-- <NavBar/> -->
  
  <RouterView />

</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import { ref, onMounted } from "vue";
import { profile } from '@/services/userAPI';
// import { useCookiesStore } from "./stores/cookies";
import { useProfileStore } from "./stores/profile";
import { listTeams } from "./services/teamAPI";
// const cookie = useProfileStore();
// const token = cookie.getCookie('token');
// const category = "alevin";
// if (token) {
onMounted(() => {
  console.log("Cargando perfil...");
  // profile()
  listTeams(category)
});
// }

</script>

<style scoped></style>
