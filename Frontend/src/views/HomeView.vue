<template>
  <div>
    <!-- Barra de navegación -->
    <NavBar />

    <!-- Sección de escudos de equipos -->
    <ListImgTeamsComponent />

    <!-- Contenido principal -->
    <div class="flex flex-col md:flex-row mt-16 h-full">
      <!-- Texto de bienvenida -->
      <div class="flex flex-col items-center justify-center md:w-1/2 p-6 text-center">
        <img src="../img/LogoTrainTrack.png" alt="" class="flex w-80">
        <p class="text-2xl font-semibold mb-4">¡Bienvenido a TRANTRACK!</p>
        <p class="text-gray-700">
          En TrainTrack, estamos emocionados de ofrecerte una herramienta que facilita la comunicación
          entre jugadores y entrenadores. Sabemos lo importante que es mantener una conexión efectiva
          para apoyar el desarrollo y el crecimiento de los jóvenes.
        </p>
      </div>


      <!-- División para el contenido adicional -->
      <div class="flex flex-col md:w-1/2 justify-center p-4">
        <div class="w-full justify-center p-4 pr-10">

          <div class="justify-center p-4 flex">
            <div class="ml-4">
              <img src="https://upload.wikimedia.org/wikipedia/commons/b/b5/Logotipo_del_Gobierno_de_Canarias.svg"
                alt="Federacion" class="w-56">
            </div>
            <div>
              <img src="../img/fcf.png" alt="Federacion" class="w-56">
            </div>
          </div>

          <!-- División para entrar como padre -->
          <div class="justify-center p-4">
            <router-link to="/parent" class="max-w-xl w-full">
              <div class="bg-gray-100 p-8 rounded-lg shadow-lg hover:shadow-xl transition duration-300">
                <h2 class="text-2xl font-semibold mb-4">Entrar como padre</h2>
                <p class="text-gray-700">Si no tienes cuenta, primero registra el equipo al que pertenece tu hijo.</p>
              </div>
            </router-link>
          </div>
          <img src="" alt="">
          <!-- División para entrar como entrenador -->
          <div class="justify-center p-4">
            <router-link to="/trainer" class="max-w-xl w-full">
              <div class="bg-gray-100 p-8 rounded-lg shadow-lg hover:shadow-xl transition duration-300">
                <h2 class="text-2xl font-semibold mb-4">Entrar como entrenador</h2>
                <p class="text-gray-700">Si no tienes cuenta, primero registra el equipo al que perteneces.</p>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <!-- <img src="../img/TrainTrackPhone.jpg" alt="" class="w-24"> -->
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