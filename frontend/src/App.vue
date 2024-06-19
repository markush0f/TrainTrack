<template>
  <!-- <NavBar/> -->

  <RouterView />

</template>

<script setup>
import { RouterView } from "vue-router";
import { onMounted } from "vue";
import { profile } from '@/services/userAPI';
import { useCookiesStore } from "./stores/cookies";
import { useCategoryStore } from "./stores/category";
import { useProfileStore } from "./stores/profile";
import { usePlayerStore } from "./stores/players";
import { loadEvents } from "./services/calendarAPI";


const cookie = useCookiesStore();
const token = cookie.getCookie('token');
const categoryStore = useCategoryStore();
const profileStore =  useProfileStore();
const playerStore = usePlayerStore()

onMounted(async () => {
  if (token) {
    categoryStore.setCategory('prebenjamin')
    await profile()
    await loadEvents()
    if (profileStore.data.childrens) {
      console.log(profileStore.data);
      if (profileStore.data.rol === 'parent') {
        playerStore.player = profileStore.data.childrens
        console.log(await playerStore.player);
      }
    }
  }
});

</script>

<style scoped></style>
