<script setup>
import NavBar from '../components/layouts/NavbarComponent.vue'
import Pie from '../components/FooterComponent.vue'
</script>

<template>
  <NavBar />
  <!-- Div padre -->
  <div class="flex h-full">
    <!-- divs hijos -->
    <div class="flex flex-col gap-4 h-screen p-4">
      <select
        class="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline">
        <option value="" disabled selected>Selecciona una categoría</option>
        <option value="prebenjamin">Prebenjamin</option>
        <option value="benjamin">Benjamin</option>
        <option value="alevin">Alevin</option>
        <option value="infantil">Infantil</option>
      </select>
      <table class="table-auto">
        <thead class>
          <tr>
            <th class="px-4 py-2 bg-green-300 text-black ">Club</th>
            <th class="px-4 py-2 bg-green-300">PJ</th>
            <th class="px-4 py-2 bg-green-300">W</th>
            <th class="px-4 py-2 bg-green-300">D</th>
            <th class="px-4 py-2 bg-green-300">L</th>
            <th class="px-4 py-2 bg-green-300 ">PTS</th>
          </tr>
        </thead>
        <tbody>
          <tr class="hover:bg-gray-100">
            <td class="px-4 py-2">Equipo 1</td>
            <td class="px-4 py-2">10</td>
            <td class="px-4 py-2">7</td>
            <td class="px-4 py-2">2</td>
            <td class="px-4 py-2">1</td>
            <td class="px-4 py-2">23</td>
          </tr>
          <tr>
            <td class="px-4 py-2">Equipo 2</td>
            <td class="px-4 py-2">9</td>
            <td class="px-4 py-2">5</td>
            <td class="px-4 py-2">3</td>
            <td class="px-4 py-2">1</td>
            <td class="px-4 py-2">18</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="flex-grow justify-center p-4 border border-gray-400">
      <!-- div de noticias -->
      <div class="justify-center p-4 border border-gray-400">
        <img src=C:\laragon\www\TrainTrack\data\img\noticiaEjemplo.jpg alt="Noticias" class="max-w-full text-center">
      </div>
      <!-- div de partidos -->
      <div class="justify-center p-4 border border-gray-400">
        <h1
          class="mb-4 text-4xl font-calibri leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-black text-center">
          Proximos partidos</h1>
        <table class="w-full">
          <thead>
            <tr>
              <th class="px-4 py-2 bg-green-300"></th>
              <th class="px-4 py-2 bg-green-300"></th>
              <th class="px-4 py-2 bg-green-300"></th>
            </tr>
          </thead>
          <tbody>
            <tr class="text-center">
              <td class="px-4 py-2">Equipo 1</td>
              <td class="px-4 py-2">-</td>
              <td class="px-4 py-2">Equipo 2</td>
            </tr>
            <tr class="text-center">
              <td class="px-4 py-2">Equipo 1</td>
              <td class="px-4 py-2">-</td>
              <td class="px-4 py-2">Equipo 2</td>
            </tr>
            <tr class="text-center">
              <td class="px-4 py-2">Equipo 1</td>
              <td class="px-4 py-2">-</td>
              <td class="px-4 py-2">Equipo 2</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div class="w-1/3 justify-center p-4 pr-10 border border-gray-400">
      <!-- div de federacion -->
      <div class="justify-center p-4 border border-gray-400">
        <img src=C:\laragon\www\TrainTrack\data\img\federacionEjemplo.png alt="Federacion" class="">
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
          <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full">Iniciar sesion como
            entrenador</button>
        </div>

        <!-- Boton de iniciar sesion como padre-->
        <div class="justify-center p-4 border border-gray-400">
          <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full">Iniciar sesion como
            padre</button>
        </div>
      </div>
    </div>
  </div>
  <Pie />
</template>




<style></style>
