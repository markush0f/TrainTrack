<template>
  <!-- <NavBar/> -->

  <RouterView />

</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import { ref, onMounted } from "vue";
import { profile } from '@/services/userAPI';
import { useProfileStore } from "./stores/profile";
import { listTeams } from "./services/teamAPI";
import { decodeJWT } from "@/services/userAPI";
import { useCookiesStore } from "./stores/cookies";
import { useRolStore } from "./stores/profile";
import { listNotifications } from "./services/trainerAPI";
import { listPlayers, playersByCategory } from '@/services/playersAPI';
const cookie = useCookiesStore()
const token = cookie.getCookie('token')
const rolStore = useRolStore()
import { useCategoryStore } from '@/stores/team';

const categoryStore = useCategoryStore();
const rol = ref('')
rol.value = rolStore.getRol();
onMounted(() => {
  if (token) {
    // console.log("Hay token");
    decodeJWT()
    // listNotifications()
    categoryStore.setCategory('prebenjamin')
    playersByCategory()
  }
  profile()
});

</script>

<style scoped></style>
