<template>
  <div class="fixed top-0 left-0 flex items-center justify-center w-full h-full bg-black bg-opacity-50">
    <ProfileTrainerComponent v-if="rol == 'trainer'" />
    <ProfileParentComponent v-if="rol == 'parent'" />
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
  rol.value = rolStore.getRol();
});
</script>