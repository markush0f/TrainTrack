<template>
  <NavBar />

  <!-- Div padre -->
  <div class="flex h-full">
    <!-- divs hijos -->
    <div class="flex flex-col gap-4 h-screen p-6 ">
      <ClassificationTableComponent />
    </div>
    <div class="flex-grow justify-center p-4 border border-gray-400">
      <!-- div de noticias -->
      <div class="justify-center p-4 border border-gray-400">
        <img
          src=https://previews.123rf.com/images/yupiramos/yupiramos1609/yupiramos160920026/62953659-de-dibujos-animados-de-televisi%C3%B3n-de-noticias-reportera-ejemplo-gr%C3%A1fico-del-vector.jpg
          alt="Noticias" class="news">
      </div>
      <!-- div de partidos -->
      <div class="justify-center p-4 border border-gray-400">
        <NextGamesComponent />
      </div>
    </div>
    <div class="w-1/3 justify-center p-4 pr-10 border border-gray-400">
      <!-- div de federacion -->
      <div class="justify-center p-4 border border-gray-400">
        <img src="https://www.dyntra.org/new/wp-content/uploads/2018/07/federacion-canaria-futbol.jpg" alt="Federacion"
          class="">
      </div>
      <!-- Div de acciones -->
      <div>
        <!-- Boton de registrar equipo -->
        <div class="justify-center p-4 border border-gray-400">
          <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full">Registrar
            equipo</button>
        </div>

        <!-- Boton de Iniciar sesion de entrenador -->
        <div class="justify-center p-4 border border-gray-400">
          <router-link to="/signup" @click="saveRol('trainer')"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full">Control de
            entrenador</router-link>
        </div>

        <!-- Boton de iniciar sesion como padre-->
        <div class="justify-center p-4 border border-gray-400">
          <router-link to="/signup" @click="saveRol('parent')"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full">Control de
            padre</router-link>
        </div>
      </div>
    </div>
  </div>
  <Pie />
</template>

<script setup>
import NavBar from '../components/layouts/NavbarComponent.vue';
import NextGamesComponent from '@/components/teams/NextGamesComponent.vue';
import Pie from '../components/FooterComponent.vue'

import { ref } from 'vue';
import { useRolStore } from '@/stores/ROL';
import ClassificationTableComponent from '@/components/teams/ClassificationTableComponent.vue';


const store = useRolStore()
function saveRol(rol) {
  store.setRol(rol)
  console.log(store.rol);
}

</script>




<style lang="css">
.news {
  /*max-width: 100%;*/
  text-align: center;
  width: 500px;
  margin: 0 auto;

}
</style>
