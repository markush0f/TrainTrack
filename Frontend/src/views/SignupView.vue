<template lang="">
  <div class="flex items-center justify-center h-screen bg-green-100">
    <div class="bg-white p-8 rounded-lg shadow-lg">
  <div>
    <form class="w-full max-w-lg" @submit.prevent="submitForm">
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputName">Name</label>
      <input  v-model="data.name" class="appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="name" id="inputName"  placeholder="Insert your name..." >
      <p class="text-red-500 text-xs italic">Please fill out this field.</p>
    </div>
    

    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputSurname">surname</label>
      <input v-model="data.surname" class="appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="surname" id="inputSurname"  placeholder="Insert your surname..." >
      <p class="text-red-500 text-xs italic">Please fill out this field.</p>
    </div>
  </div>

  
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputEmail">Email</label>
      <input  v-model="data.email" class="appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="email" id="inputEmail"  placeholder="Insert your Email..." >
    </div>
    <div class="w-full px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputPassword">Password</label>
      <input  v-model="data.password" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" name="password" id="inputPassword" type="password" placeholder="******************">
    </div>
  </div>

  
  <div class="flex flex-wrap -mx-3 mb-2">
    <div class="w-full md:w-1/3 px-3 mb-6 md:mb-0">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputBirthday">
        BirthDay
      </label>
      <input   v-model="data.birth" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="inputBirthday" type="date"  >
    </div>
    <div class="w-full md:w-1/3 px-3">
      <label   class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputNumber">
        Number
      </label>
      <input v-model="data.phone" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="inputPhone" type="phone" placeholder="XXX-XXX-XXX" maxlength="9" >
    </div>
  </div>

  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputAdress1">Adress</label>
      <input v-model="data.address1" class="appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="adress" id="inputAdress1"  placeholder="Insert first Adress..." >
    </div>
    <div class="w-full px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputAdress2">Adress2</label>
      <input v-model="data.address2" class="appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="adress" id="inputAdress2"  placeholder="Insert second Adress..." >
    </div>
    <div>
      <input v-model="data.dni" class="appearance-none block w-full bg-gray-200 text-gray-700 border  rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="adress" id="inputAdress2"  placeholder="Introduzca su DNI..." >
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
import { signup } from '../services/userAPI'
import axios from 'axios';
// import { useRolStore } from '@/stores/ROL';
// const store = useRolStore()
const data = ref({
  "name": "",
  "surname": "",
  "email": "",
  "password": "",
  "birth": "",
  "phone": "",
  "address1": "",
  "address2": "",
  "dni": ""
});

const submitForm = async () => {
  signup(data.value)
};
</script>
