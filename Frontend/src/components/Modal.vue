<template>
  <div class="fixed top-0 left-0 flex items-center justify-center w-full h-full bg-black bg-opacity-50">
    <div class="max-w-lg mx-auto bg-white rounded-lg shadow-lg overflow-hidden z-10 ">
      <ProfileTrainerComponent v-if="rol == 'trainer'" />
      <ProfileParentComponent v-if="rol == 'parent'" />
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import ProfileComponent from './ProfileComponent.vue';
import ProfileTrainerComponent from './trainers/ProfileTrainerComponent.vue';
import ProfileParentComponent from './parents/ProfileParentComponent.vue';
import { decodeJWT } from '@/services/userAPI';
import { useRolStore } from '@/stores/profile';

const rolStore = useRolStore()
const rol = ref('')
onMounted(async () => {
  console.log("Carga el token");
  rol.value = rolStore.getRol();
  console.log("Rol:", rol.value);
});
</script>