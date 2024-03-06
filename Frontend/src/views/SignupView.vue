<template lang="">
  <div>
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

      <label for="inputSurName" class="col-sm-2 col-form-label">Surname</label>
      <div class="col-sm-6 mb-2">
        <input
          type="text"
          name="surname"
          class="form-control"
          id="inputSurName"
          data-bs-theme="dark"
          required
        />
      </div>

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
