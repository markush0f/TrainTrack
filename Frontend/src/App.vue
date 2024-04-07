<template>
  <!-- <NavBar/> -->

  <RouterView />

</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import { ref, onMounted } from "vue";
import { profile } from '@/services/userAPI';
// import { decodeJWT } from "@/services/userAPI";
import { useCookiesStore } from "./stores/cookies";
import { useCategoryStore } from "./stores/category";
import { useProfileStore } from "./stores/profile";
import { usePlayerStore } from "./stores/players";
// import { playersByCategory } from '@/services/playersAPI';

const cookie = useCookiesStore();
const token = cookie.getCookie('token');
const categoryStore = useCategoryStore();
const profileStore = useProfileStore();
const playerStore = usePlayerStore()

onMounted(async () => {
  if (token) {
    categoryStore.setCategory('prebenjamin')
    await profile()
    if (profileStore.data.childrens) {
      console.log(profileStore.data);
      playerStore.player = profileStore.data.childrens
      console.log(playerStore.player);
    }
  }
});

</script>

<style scoped></style>
