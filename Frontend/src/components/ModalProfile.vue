<template>
  <div
    class="fixed top-0 left-0 flex items-center justify-center w-full h-full bg-black bg-opacity-50 z-50"
  >
    <ProfileComponent />
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";

import ProfileComponent from "./ProfileComponent.vue";

onMounted(async () => {});
</script>
