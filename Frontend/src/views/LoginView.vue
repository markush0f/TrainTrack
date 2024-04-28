<template lang="html">
  <div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8">
    <div class="mx-auto max-w-lg">
      <h1 class="text-center text-2xl font-bold text-main-green sm:text-3xl">
        Iniciar sesión
      </h1>
      <form
        @submit.prevent="submitForm"
        class="mb-0 mt-6 space-y-4 rounded-lg p-4 shadow-lg sm:p-6 lg:p-8"
      >
        <p class="mx-auto mt-4 max-w-md text-center text-gray-500">
          Bienvenido de nuevo a Train Track, introduzca sus datos para acceder a
          las funciones de su hijo/s
        </p>
        <p class="text-center text-lg font-medium"></p>

        <div>
          <label for="email" class="sr-only">Email</label>
          <div class="relative">
            <input
              type="text"
              required
              v-model="data.email"
              class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm shadow-light-gray"
              placeholder="Introduzca su email"
            />
          </div>
        </div>

        <div>
          <label for="password" class="sr-only">Password</label>
          <div class="relative">
            <input
              type="password"
              required
              v-model="data.password"
              class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm shadow-light-gray"
              placeholder="Introduza su contraseña"
            />
          </div>
        </div>

        <div class="flex justify-between space-x-4">
          <button
            type="submit"
            class="w-1/2 rounded-lg bg-main-green px-4 py-2 text-sm font-medium text-white"
          >
            Iniciar sesión
          </button>
          <router-link
            to="/"
            class="flex items-center justify-center w-1/2 rounded-lg bg-white px-4 py-2 text-sm font-medium text-main-green border-2"
          >
            Volver
          </router-link>
        </div>

        <p class="text-center text-sm text-gray-500">
          <router-link class="underline" to="/signup"
            >Pulse aquí para registrarse</router-link
          >
        </p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { login } from "@/services/userAPI";
import { useCookies } from "vue3-cookies";

const { cookies } = useCookies();
const data = ref({
  email: "",
  password: "",
  JWT: cookies.get("token"),
});
const errors = {
  email: "El email debe ser necesario",
};
const submitForm = async () => {
  await login(data.value);
};
</script>

<style lang="css" scoped></style>
