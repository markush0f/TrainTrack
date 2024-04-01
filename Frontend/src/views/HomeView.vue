<template>
  <NavBar />
  <!-- ESCUDOS -->
  
  <ListImgTeamsComponent />
  <div class="flex flex-col md:flex-row mt-16 h-full">
    <div class="flex flex-col gap-4 md:w-1/3 h-full p-6">
      <SelecCategory />
      <ClassificationTableComponent />
      <RankingPlayersComponent />
    </div>
    <!-- div de partidos -->
    <div class="flex-grow justify-center p-4">
      <!-- <div class="justify-center p-4 pl-4">
        <NextGamesComponent />
      </div> -->
      <!-- div de ranking de jugadores -->
      <div class="justify-center p-4">
        
      </div>
    </div>
    <!-- div de federacion y registros -->
    <div class="w-full md:w-1/3 justify-center p-4 pr-10">
      <!-- div de federacion -->
      <div class="justify-center p-4 flex">
        <div class="ml-4">
          <img src="https://upload.wikimedia.org/wikipedia/commons/b/b5/Logotipo_del_Gobierno_de_Canarias.svg"
            alt="Federacion" class="w-56">
        </div>
        <div>
          <img src="../img/fcf.png" alt="Federacion" class="w-56">
        </div>
      </div>
      <!-- PADRE -->
      <div class="justify-center p-4 ">
        <router-link to="/parent" class="max-w-xl w-full">
          <div class="bg-gray-100 p-8 rounded-lg shadow-lg hover:shadow-xl transition duration-300">
            <h2 class="text-2xl font-semibold mb-4 ">Entrar como padre</h2>
            <p class="text-gray-700">Si no tiene cuenta, primero registre el equipo al que pertenece su hijo.</p>
          </div>
        </router-link>
      </div>
      <!-- ENTRENADOR -->
      <div class="justify-center p-4">
        <router-link to="/trainer" class="max-w-xl w-full">
          <div class="bg-gray-100 p-8 rounded-lg shadow-lg hover:shadow-xl transition duration-300">
            <h2 class="text-2xl font-semibold mb-4 ">Entrar como entrenador</h2>
            <p class="text-gray-700">Si no tiene cuenta, primero registre el equipo al que pertenece.</p>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>


<script setup>
import NavBar from '../components/layouts/NavbarComponent.vue';
import RankingPlayersComponent from '@/components/players/RankingPlayersComponent.vue';
import { ref, } from 'vue';
import ClassificationTableComponent from '@/components/teams/ClassificationTableComponent.vue';
import ListImgTeamsComponent from '@/components/teams/ListImgTeamsComponent.vue'
import SelecCategory from '@/views/teams/SelectCategory.vue'
// CADA VEZ QUE CAMBIE DE CATEGORÍA SE CAMBIE TODO, HACIENDO UNA FUNCIÓN DE LOAD

</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>