<template lang="html">
  <div class="flex items-center justify-center h-screen bg-green-100">
    <div>
      <!-- <img src="https://cdn-icons-png.flaticon.com/512/1039/1039328.png" class="logo "> -->
      <div class="divForm ">
        <h1 class="mr-10 ml-10">Introduzca sus datos para iniciar sesión</h1>
        <form @submit.prevent="submitForm" class="bg-white px-8 pt-6 pb-8 mb-4">
          <div class=" mb-5 ">
            <div class="grid-flow-row sm:grid-flow-col gap-3">
              <div class="flex justify-start items-center mb-2">
                <label class="text-black-700 text-sm font-semibold mr-10" for="inputEmail">Email</label>
                <input v-model="data.email"
                  class="shadow apperance-none border rounded w-full py-2 px-3 text-grey-700 leading-tight focus:outline-none focus:shadow-outline"
                  type="text" name="email" id="inputEmail" placeholder="Escriba su email..." required>
              </div>
            </div>
          </div>
          <div class=" mb-4 ">
            <div class="grid-flow-row sm:grid-flow-col gap-3">
              <div class="sm:col-span-4 justify-self-start">
                <label class="block text-black-700 text-sm font-bold mb-2" for="inputPassword">Password</label>
                <input v-model="data.password"
                  class="shadow apperance-none border rounded w-full py-2 px-3 text-grey-700 leading-tight focus:outline-none focus:shadow-outline"
                  type="password" name="password" id="inputPassword" placeholder="************" required></input>
              </div>
            </div>
          </div>
          <div class="flex items-center justify-center">
            <input type="submit" value="Entrar"
              class="bg-green-700 hover:bg-green-900 text-white font-bold py-2 px-4 rounded-full mr-4" />
            <router-link to="/"
              class="bg-white-500 hover:bg-green-200 text-green-700 font-bold py-2 px-4 rounded-full">Volver</router-link>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

import { login } from '@/services/userAPI';

// import { useTokenUserStore } from '@/stores/JWT';
import { useCookies } from "vue3-cookies";
const { cookies } = useCookies();

const data = ref({
  email: '',
  password: '',
  JWT: cookies.get('token'),
});

const submitForm = async () => {
  await login(data.value);
};
</script>

<style lang="css" scoped>
.divForm {
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-width: 1000px;
  height: 300px;
  width: 100%;
  margin-right: 400px;
  margin-top: 100px;
}

.logo {
  width: 300px;
}
</style>
