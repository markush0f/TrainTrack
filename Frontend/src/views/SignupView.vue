<template lang="">
  <div>
    <form class="w-full max-w-lg" @submit.prevent="submitForm">
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputName">Name</label>
      <input  v-model="data.name" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="name" id="inputName"  placeholder="Insert your name..." >
      <p class="text-red-500 text-xs italic">Please fill out this field.</p>
    </div>
    

    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputSurname">surname</label>
      <input v-model="data.surname" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="surname" id="inputSurname"  placeholder="Insert your surname..." >
      <p class="text-red-500 text-xs italic">Please fill out this field.</p>
    </div>
  </div>

  
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputEmail">Email</label>
      <input  v-model="data.email" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="email" id="inputEmail"  placeholder="Insert your Email..." >
    </div>
    <div class="w-full px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputPassword">Password</label>
      <input  v-model="data.password" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" name="password" id="inputPassword" type="password" placeholder="******************">
      <p class="text-gray-600 text-xs italic">Make it as long and as crazy as you'd like</p>
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
      <input v-model="data.address1" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="adress" id="inputAdress1"  placeholder="Insert first Adress..." >
    </div>
    <div class="w-full px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputAdress2">Adress2</label>
      <input v-model="data.address2" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="adress" id="inputAdress2"  placeholder="Insert second Adress..." >
    </div>
    <div>
      <input v-model="data.dni" class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="adress" id="inputAdress2"  placeholder="Insert second Adress..." >

    </div>
  </div>
  <input type="submit" value="Register"  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" />
</form>
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
  "dni": ""
})
// Cambiarlo al archivo userAPI
const submitForm = async () => {
  signup(data.value)
}
</script>
