<template>
  <NavBar />
  <!-- ESCUDOS -->
  <ListImgTeamsComponent />
  <!-- Div padre -->
  <div class="flex h-full ">
    <!-- divs hijos -->
    {{ categoryStore.category }}
    <div class="flex flex-col gap-4 h-screen p-6 ">
      <select v-model="categoryStore.category"
        class="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline">
        <!-- <option value="" disabled>Selecciona una categoría</option> -->
        <option value="prebenjamin">Prebenjamin</option>
        <option value="benjamin">Benjamin</option>
        <option value="alevin">Alevin</option>
        <option value="infantil">Infantil</option>
      </select>
      <ClassificationTableComponent />
    </div>
    <!-- div de partidos -->
    <div class="flex-grow justify-center p-4">
      <div class="justify-center p-4 pl-4">
        <NextGamesComponent />
      </div>
      <!-- div de ranking de jugadores -->
      <div class="justify-center p-4 ">

        <RankingPlayersComponent />
      </div>
    </div>
    <div class="w-1/3 justify-center p-4 pr-10">
      <!-- div de federacion -->
      <div class="justify-center p-4 flex">
        <div class="ml-4">
          <img src="https://upload.wikimedia.org/wikipedia/commons/b/b5/Logotipo_del_Gobierno_de_Canarias.svg"
            alt="Federacion" class="w-56">
        </div>
        <div>
          <img src="https://www.ftf.es/2023/img/logos/fcf.png" alt="Federacion" class="w-56">
        </div>
      </div>
      <div>
        <!-- REGISTRAR EQUIPO -->
        <div class="justify-center p-4  ">
          <router-link to="/" class="max-w-xl w-full">
            <div class="bg-gray-100 p-8 rounded-lg shadow-lg hover:shadow-xl transition duration-300">
              <h2 class="text-2xl font-semibold mb-4 ">Registrar equipo</h2>
              <p class="text-gray-700">Registro de equipo para el acceso a crearse la cuenta.
              </p>
            </div>
          </router-link>
        </div>

        <!-- PADRE -->
        <div class="justify-center p-4 ">
          <router-link to="/parent" class="max-w-xl w-full">
            <div class="bg-gray-100 p-8 rounded-lg shadow-lg hover:shadow-xl transition duration-300">
              <h2 class="text-2xl font-semibold mb-4 ">Entrar como padre</h2>
              <p class="text-gray-700">Si no tiene cuenta, primero registre el equipo al que pertence su hijo.
              </p>
            </div>
          </router-link>
        </div>

        <!-- ENTRENADOR-->
        <div class="justify-center p-4">
          <router-link to="/trainer" class="max-w-xl w-full">
            <div class="bg-gray-100 p-8 rounded-lg shadow-lg hover:shadow-xl transition duration-300">
              <h2 class="text-2xl font-semibold mb-4 ">Entrar como entrenador</h2>
              <p class="text-gray-700">Si no tiene cuenta, primero registre el equipo al que pertence
              </p>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
  <Pie />
</template>

<script setup>
import NavBar from '../components/layouts/NavbarComponent.vue';
import NextGamesComponent from '@/components/teams/NextGamesComponent.vue';
import Pie from '../components/layouts/FooterComponent.vue'
import RankingPlayersComponent from '@/components/players/RankingPlayersComponent.vue';
import { useTeamStore, useCategoryStore } from '@/stores/team';
import { ref, onMounted } from 'vue';
import { listAllShields } from '@/services/teamAPI';
import ClassificationTableComponent from '@/components/teams/ClassificationTableComponent.vue';
import ListImgTeamsComponent from '@/components/teams/ListImgTeamsComponent.vue'
const categoryStore = useCategoryStore()
const category = ref('prebenjamin');
// categoryStore.setCategory(category)
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