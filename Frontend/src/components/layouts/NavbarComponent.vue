<template>
  <nav class="bg-white w-full z-20 top-0 start-0 border-b border-main-green">
    <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
      <a href="" class="flex items-center space-x-3 rtl:space-x-reverse">
        <span class="self-center text-2xl font-semibold whitespace-nowrap text-black">Train Track</span>
      </a>
      <div class="flex md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">

        <button @click=" profileStore.show = true" v-if="token" class="block py-2 px-3 md:p-0 text-main-green rounded 
          hover:bg-transparent md:hover:text-main-green">
          PERFIL
        </button>
        <Modal v-if="profileStore.show" @close="profileStore.show = false" />
      </div>
      <div class="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-sticky">
        <ul
          class="flex flex-col p-4 md:p-0 mt-4 font-medium border border-main-green rounded-lg md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0  ">
          <li>
            <router-link to="/" class="block py-2 px-3 md:p-0 text-main-green text-xl rounded 
            hover:bg-transparent md:hover:text-dark-green">INICIO</router-link>
          </li>
          <li>
            <router-link to="/" class="block py-2 px-3 md:p-0 text-main-green text-xl rounded 
            hover:bg-transparent md:hover:text-dark-green">Competiciones</router-link>
          </li>
          <li>
            <router-link to="/" class="block py-2 px-3 md:p-0 text-main-green text-xl rounded 
            hover:bg-transparent md:hover:text-dark-green">AYUDA</router-link>
          </li>
          <li>
            <router-link to="/" class="block py-2 px-3 md:p-0 text-main-green text-xl rounded 
            hover:bg-transparent md:hover:text-dark-green">CONTACTO</router-link>
          </li>

        </ul>
      </div>
    </div>
  </nav>


</template>
<script setup>

import axios from 'axios';
import { ref } from 'vue'
import Modal from '@/components/ModalProfile.vue';

const profileStore = useProfileStore();
import { useProfileStore } from '@/stores/profile';
import { useCookies } from "vue3-cookies";
const { cookies } = useCookies();
const token = cookies.get('token')

</script>