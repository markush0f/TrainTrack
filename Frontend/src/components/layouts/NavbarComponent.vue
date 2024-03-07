<template>
  <nav class="bg-white shadow dark:bg-gray-800 text-black">
            
            <div class="max-w-7x mx-auto px-4 py-3 flex items-center justify-between">
                <div class="flex items-center">
                  <span class="text-3xl font-Blacker">Logo</span>
                </div>
                <!-- Links -->
                <div class="flex-1 flex justify-center">
                    <a href="#" class="text-3xl px-3 py-2 hover:bg-green-300"><HomeView/>Home</a>
                    <a href="#" class="text-3xl  px-3 py-2 hover:bg-green-300">About As</a>
                    <a href="#" class="text-3xl  px-3 py-2 hover:bg-green-300">Teams</a>
                    <!-- <a href="#" class="px-3 py-2 hover:bg-gray-700">Contacto</a> -->
                </div>
            </div>
  </nav>
  <nav class="bg-gray-800 shadow dark:bg-gray-800"> 
        <div class="flex items-center">
                  <span class="text-xl font-Blacker" >
                    
                  </span>
                </div>
  </nav>
  <div>
    <select>
      Selecciona la categoria: 
      <option>Pre-benjamin</option>
      <option>Benjamin</option>
      <option>Alevin</option>
      <option>Infantiles</option>
    </select>
    <table>
      <thead>
      
      </thead>
      <tbody>
        
      </tbody>
    </table>
  </div>
  <CodeTeamComponent/>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue'
// import URL_API from "../../variables";

import CodeTeamComponent from "./CodeTeamComponent.vue"
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
const name = ref("");

function sendName() {
  const data = {
    "Name": name.value
  }
  axios.post(`http://127.0.0.1:8000/api/createuser`, data)
    .then(res => {
      console.log(data.Name)
      console.log("Respuesta del servidor: ", res.data);
    })
    .catch(error => {
      console.log("Error: ", error);
    })
}

function showLogo(){
  for (let index = 0; index < 10; index++){
    console.log("Logo");   
  }
};

  showLogo();

</script>
