<template>
  <div class="fixed top-0 left-0 flex items-center justify-center w-full h-full bg-black bg-opacity-50">
    <div class="max-w-lg mx-auto bg-white rounded-lg shadow-lg overflow-hidden z-10 ">
      <!-- <div class="flex justify-end  mt-4">
        <button class="mr-4" @click="profileStore.show = false"><i class="material-icons">close</i></button>
      </div> -->
      <ProfileComponent />
    </div>
  </div>
</template>

<script setup>
import ProfileComponent from './ProfileComponent.vue'
</script>