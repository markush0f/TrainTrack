<template lang="">

<div class="mx-auto max-w-screen-xl px-4 py-16 sm:px-6 lg:px-8">
  <div class="mx-auto max-w-lg">
    <h1 class="text-center text-2xl font-bold text-main-green sm:text-3xl">Mandar solicitud</h1>
    <form @submit.prevent="submitForm" class="mb-0 mt-6 space-y-4 rounded-lg p-4 shadow-lg sm:p-6 lg:p-8">
      <p class="mx-auto mt-4 max-w-md text-center text-gray-500">
        Bienvenido a Train Track, introduzca sus datos para registrarse y acceder a las funciones de su hijo/s
      </p>
      <p class="text-center text-lg font-medium"></p>

      <div class="flex">
        <div class="mr-4">
          <div class="relative">
            <input type="text" v-model="data.name"
              class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm shadow-light-gray"
              placeholder="Nombre" />
          </div>
        </div>
      
        <div>
          <div class="relative">
            <input type="text" v-model="data.surname"
              class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm shadow-light-gray"
              placeholder="Apellidos" />
          </div>
        </div>
      </div>

      
        <div class="mr-4">
          <label for="email" class="sr-only">Email</label>
          <div class="relative">
            <input type="text" v-model="data.email"
              class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm shadow-light-gray"
              placeholder="Email" />
          </div>
        </div>
      
        <div>
          <div class="relative">
            <input type="text" v-model="data.password"
              class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm shadow-light-gray"
              placeholder="Contraseña" />
          </div>
      </div>

      <div class="flex ">
        <div class="mr-4">
          <input type="text" v-model="data.phone"
            class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm shadow-light-gray"
            placeholder="Numero de teléfono" />
        </div>
        <div class="mr-4">
          <input type="text" v-model="data.DNI"
            class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm shadow-light-gray"
            placeholder="DNI" />
        </div>
      </div>
      <div class="mr-4">
        <input type="date" v-model="data.birth"
          class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm shadow-light-gray" />
      </div>
        <div class="mr-4">
          <input type="text" v-model="data.address1"
            class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm shadow-light-gray"
            placeholder="Primera dirección" />
        </div>
        <div class="mr-4">
          <input type="text" v-model="data.address2"
            class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm shadow-light-gray"
            placeholder="Segunda dirección (opcional)" />
      </div>
      Equipo: 
      <div class="mr-4">
        <input type="text" v-model="data.teamCode"
          class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm shadow-light-gray"
          placeholder="Codigo de equipo" />
    </div> 
    <div class="mr-4">
      <input type="text" v-model="data.teamPassword"
        class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm shadow-light-gray"
        placeholder="Contraseña de equipo" />
  </div>
  <p class="text-sm text-gray-500">
    <router-link class="underline" to="/login">Ayuda sobre el equipo</router-link>
  </p>
    
      

      <div class="flex justify-between space-x-4">
        <button type="submit" class="w-1/2 rounded-lg bg-main-green px-4 py-2 text-sm font-medium text-white">
          Registrarse
        </button>
        <router-link to="/"
          class="flex items-center justify-center w-1/2 rounded-lg bg-white px-4 py-2 text-sm font-medium text-main-green border-2">
          Volver
        </router-link>
      </div>

      <p class="text-center text-sm text-gray-500">
        <router-link class="underline" to="/login">Pulse aquí si ya tiene cuenta</router-link>
      </p>
    </form>
  </div>
</div>

</template>

<script setup>
import { ref } from 'vue';
import { signup } from '../services/userAPI'
import axios from 'axios';

const data = ref({
  "name": "",
  "surname": "",
  "email": "",
  "password": "",
  "birth": "",
  "phone": "",
  "address1": "",
  "address2": "",
  "DNI": "",
  "teamCode": "",
  "teamPassword": ""
});

const submitForm = async () => {
  signup(data.value)
};

</script>
