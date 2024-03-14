<template>
  <NavbarComponent />
  <div class="flex h-full">
    <div class="flex flex-col gap-4 h-screen p-6 ">
      <!-- div del Escudo del equipo -->
      <div class="justify-center p-4 border border-gray-400">
        <img src="https://www.dyntra.org/new/wp-content/uploads/2018/07/federacion-canaria-futbol.jpg" alt="Federacion"
          class="logo">
      </div>
      <!-- div de la clasificacion -->
      <div>
        <ClassificationTableComponent />
      </div>
    </div>
    <div class="flex-grow justify-center p-4 border border-gray-400">
        <!-- div de horario de entrenamiento -->
        <h2 class="text-lg font-bold text-center">Horario de entrenamiento</h2>
      <CalendariComponent />
      <!-- div de ultimas notificaciones -->
      <NotificationComponent />
    </div>

    <div class="w-1/4 p-4">
      <!-- divs donde ira la informacion del equipo, ficha del hijo, Avisos Para el dia del entrenamiento/partido, Enviar mensaje al entrenador, proximo partido. -->
      <!-- div de la informacion del equipo -->
      <div class ="justify-center p-4 border border-gray-400">
        <h2 class="text-lg font-bold text-center">Informacion del equipo</h2>
        <p class="text-gray-600">Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique voluptatibus corporis adipisci iste vel incidunt ipsum ut veritatis, in voluptate sint fugit. Quisquam nulla hic itaque praesentium iure labore eius.</p>
      </div>
      <!-- div de ficha del hijo -->
      <div class ="justify-center p-4 border border-gray-400">
        <h2 class="text-lg font-bold text-center p-2">Ficha del hijo</h2>
        <button class="bg-main-green hover:bg-blue-700 text-white font-bold py-2 w-full rounded-full">Ficha del hijo</button><br><br>
        <!-- div de form para enviar aviso al entrenador. -->
        <div class ="justify-center p-4 border border-gray-400"> 
          <h2 class="text-lg font-bold text-center p-1">Enviar aviso al entrenador</h2>
          <form class="w-full max-w-lg p-4">
            <select>
              <option>No Asisto</option>
              <option>Asisto</option>
              <option>Llego tarde</option>
            </select><br><br>
            <input type="submit" value="Enviar" class="bg-main-green hover:bg-blue-700 text-white font-bold py-2 w-full rounded-full" />
          </form>
        </div>
      </div>
      <!-- form para enviar mensaje al entrenador -->
      <div class=" p-4 border border-gray-400 ">
        <form @submit.prevent="submitForm">
           <h2 class="text-lg font-bold text-center p-2">Enviar mensaje al entrenador</h2><br>
          <div class="p-2 w-full">
            <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
              for="Asunto">Asunto</label>
            <input type="text" name="Asunto" id="inputAsunto" cols="70" placeholder="Introduce el asunto...">
          </div>

          <div class="p-2">
            <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
              for="Motivo">Motivo</label>
            <input type="text"
              class="appearance-none block w-full bg-gray-200 text-gray-700 border border-black-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
              name="Asunto" id="inputAsunto" placeholder="Introduce un asunto...">
          </div>
          <div class="p-2">
            <input type="submit" value="Enviar"
              class="bg-main-green hover:bg-green-700 text-white font-bold py-2 w-full rounded-full" />
          </div>
        </form>
      </div>
      <!-- Proximo partido -->
      <div class="p-4 border border-gray-400 ">
        <h2 class="text-lg font-bold text-center p-2">PROXIMO PARTIDO</h2><br>
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
          </tbody>
        </table>
      </div>
    </div>
  </div>
   
</template>

<script setup>
import NavbarComponent from '@/components/layouts/NavbarComponent.vue';
import ClassificationTableComponent from '@/components/teams/ClassificationTableComponent.vue';
import CalendariComponent from '@/components/teams/CalendariComponent.vue';
import NotificationComponent from '@/components/teams/NotificationComponent.vue';
</script>