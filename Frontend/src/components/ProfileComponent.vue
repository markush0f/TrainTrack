<template>
  <div class="container mx-auto px-4 py-8">
    <div class="max-w-lg mx-auto bg-white rounded-lg shadow-lg overflow-hidden">
      <div class="bg-main-green text-white px-6 py-4">
        <div class="flex items-center justify-between">
          <h1 class="text-2xl">Perfil</h1>
          <button class="mr-4" @click="profileStore.show = false">
            <i class="material-icons">close</i>
          </button>
        </div>
      </div>

      <div class="p-6">
        <div class="mb-6 p-5">
          <p class="text-lg font-semibold p-2 pr-3">
            Nombre y apellidos: {{ profileData.name }} {{ profileData.surname }}
          </p>
          <p class="text-gray-600 p-2 pr-3">
            Correo electrónico: {{ profileData.email }}
          </p>
          <p class="text-gray-600 p-2 pr-3">
            Ubicación: {{ profileData.address1 }}, {{ profileData.address2 }}
          </p>
          <p class="text-gray-600 p-2 pr-3">Equipo: {{ profileData.team }}</p>
          <div v-if="profileData.childrens > 0">
            <p class="text-gray-600 p-2 pr-3">
              Hijo/s: {{ profileData.childrens.name }}
            </p>
          </div>
        </div>
        <button
          @click="logout()"
          type="button"
          class="focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2"
        >
          Cerrar sesión
        </button>
      </div>
    </div>
  </div>
</template>
<script setup>
import { useProfileStore } from "@/stores/profile";
import { onMounted } from "vue";
import { useCookies } from "vue3-cookies";
const { cookies } = useCookies();
const profileStore = useProfileStore();
const profileData = profileStore.data;

async function logout() {
  cookies.remove("token");
  window.location.reload();
}

onMounted(() => {
  console.log(profileData);
});
</script>
<style scoped></style>
