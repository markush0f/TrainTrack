<template lang="">
  <div>
<<<<<<< HEAD
    <h1>Pagina de registro</h1>
    <form @submit.prevent="submitForm">
      <label for="inputName" class="col-sm-2 col-form-label">Name</label>
      <div class="col-sm-6 mb-2">
        <input
          type="text"
          v-model="formData.name"
          class="form-control"
          id="inputName"
          data-bs-theme="dark"
          required
        />
      </div>
=======
    <h1 class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-black">Pagina de registro</h1>
>>>>>>> upstream/tailwind

    <form class="w-full max-w-lg">
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputName">Name</label>
      <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="name" id="inputName"  placeholder="Insert your name..." required>
      <p class="text-red-500 text-xs italic">Please fill out this field.</p>
    </div>
    

<<<<<<< HEAD
      <label for="inputEmail" class="col-sm-2  col-form-label">Email</label>
      <div class="col-sm-6 mb-2">
        <input
          type="email"
          name="email"
          class="form-control"
          id="inputEmail"
          data-bs-theme="dark"
          required
          />
      </div>

      <label for="inputPassword" class="col-sm-2 col-form-label">Password</label>
      <div class="col-sm-6 mb-3">
        <input
          type="password"
          v-model="formData.password"
          class="form-control"
          id="inputPassword"
          data-bs-theme="dark"
          required
          />
      </div>

      <label for="inputDate" class="col-sm-2 col-form-label">BirthDay</label>
      <div class="col-sm-6 mb-2">
        <input
          type="date"
          name="date"
          class="form-control"
          id="inputDate"
          data-bs-theme="dark"
          required
        />
      </div>

      <label for="inputPhone" class="col-sm-2  col-form-label">Phone</label>
      <div class="col-sm-6 mb-2">
        <input
          type="number"
          name="phone"
          class="form-control"
          id="inputPhone"
          data-bs-theme="dark"
          required
          />
      </div>

      <label for="inputAdress1" class="col-sm-2  col-form-label">Adress 1</label>
      <div class="col-sm-6 mb-2">
        <input
          type="text"
          name="Adress1"
          class="form-control"
          id="inputAdress1"
          data-bs-theme="dark"
          required
          />
      </div>

      <label for="inputAdress2" class="col-sm-2  col-form-label">Adress 2</label>
      <div class="col-sm-6 mb-2">
        <input
          type="text"
          name="Adress2"
          class="form-control"
          id="inputAdress2"
          data-bs-theme="dark"
          />
      </div>
      
      <input type="submit" value="Enviar" class="btn btn-primary" @click="submitForm" />
    </form>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';

const formData = ref({
  name: '',
  password: '',
})

// Función para obtener el valor de una cookie por su nombre
const getCookie = (name) => {
  const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
  return cookieValue ? cookieValue.pop() : '';
};

const submitForm = async () => {
  try {
    // Token de las cookies
    const csrf = getCookie('csrftoken')
    axios.defaults.headers.common['X-CSRFToken'] = csrf;
    const res = await axios.post('http://127.0.0.1:8000/api/createuser', formData.value);
    console.log("Datos enviados", res.data);
  } catch (error) {
    console.log("Error", error);
  }
}
</script>

<style lang="css"></style>
=======
    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputSurname">surname</label>
      <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="surname" id="inputSurname"  placeholder="Insert your surname..." required>
      <p class="text-red-500 text-xs italic">Please fill out this field.</p>
    </div>
  </div>

  
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputEmail">Email</label>
      <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="email" id="inputEmail"  placeholder="Insert your Email..." required>
    </div>
    <div class="w-full px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputPassword">Password</label>
      <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" name="password" id="inputPassword" type="password" placeholder="******************">
      <p class="text-gray-600 text-xs italic">Make it as long and as crazy as you'd like</p>
    </div>
  </div>

  
  <div class="flex flex-wrap -mx-3 mb-2">
    <div class="w-full md:w-1/3 px-3 mb-6 md:mb-0">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputBirthday">
        BirthDay
      </label>
      <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="inputBirthday" type="date"  required>
    </div>
    <div class="w-full md:w-1/3 px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputNumber">
        Number
      </label>
      <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="inputPhone" type="phone" placeholder="XXX-XXX-XXX" maxlength="9" required>
    </div>
  </div>

  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputAdress1">Adress</label>
      <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="adress" id="inputAdress1"  placeholder="Insert first Adress..." required>
    </div>
    <div class="w-full px-3">
      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="inputAdress2">Adress2</label>
      <input class="appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text" name="adress" id="inputAdress2"  placeholder="Insert second Adress..." required>
    </div>
  </div>
  <input type="submit" value="Resgister" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" />
</form>
</div>
</template>

>>>>>>> upstream/tailwind
