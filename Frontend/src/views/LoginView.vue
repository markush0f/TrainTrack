<template lang="html">
  <div>
    
    <div class="flex items-center justify-center h-screen bg-green-100">
      <div class="bg-white p-8 rounded-lg shadow-lg">
        <h1 class="mr-10 ml-10">Introduzca sus datos para iniciar sesión</h1>
        <form @submit.prevent="submitForm" class="bg-white px-8 pt-6 pb-8 mb-4">
          <div class=" mb-4 ">
            <div class="grid grid-flow-row sm:grid-flow-col gap-3">
              <div class="sm:col-span-4 justify-self-start">
                <label class="block text-black-700 text-sm font-bold mb-2" for="inputEmail">Email</label>
                <input v-model="data.email"
                  class="shadow apperance-none border rounded w-full py-2 px-3 text-grey-700 leading-tight focus:outline-none focus:shadow-outline"
                  type="text" name="email" id="inputEmail" placeholder="Escriba su email..." required></input>
              </div>
            </div>
          </div>
          <div class=" mb-4 ">
            <div class="grid grid-flow-row sm:grid-flow-col gap-3">
              <div class="sm:col-span-4 justify-self-start">
                <label class="block text-black-700 text-sm font-bold mb-2" for="inputPassword">Password</label>
                <input v-model="data.password"
                  class="shadow apperance-none border rounded w-full py-2 px-3 text-grey-700 leading-tight focus:outline-none focus:shadow-outline"
                  type="password" name="password" id="inputPassword" placeholder="************" required></input>
              </div>
            </div>
          </div>
          <input type="submit" value="Entrar"
            class="bg-green-700 hover:bg-green-900 text-white font-bold py-2 px-4 rounded-full mr-4" />
          <input type="submit" value="Volver"
            class="bg-white-500 hover:bg-green-200 text-green-700 font-bold py-2 px-4 rounded-full" />
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

import { login } from '@/services/userAPI';

import { useTokenUserStore } from '@/stores/JWT';

const data = ref({
  email: '',
  password: '',
  JWT: useTokenUserStore.getToken,
});

const submitForm = async () => {
  await login(data.value);
};
</script>

<style lang="css" scoped>

</style>
