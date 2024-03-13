<template>
<NavbarComponent />
  <div class="flex h-full">
    <!-- div que recoge el escudo y la clasificacion -->
    <div class="flex flex-col gap-4 h-screen p-6 ">
      <!-- div del Escudo del equipo -->
      <div class="justify-center p-4 border border-gray-400">
        <img src="https://www.dyntra.org/new/wp-content/uploads/2018/07/federacion-canaria-futbol.jpg" alt="Federacion"
          class="">
      </div>
      <!-- div de la clasificacion -->
      <div>
        <ClassificationTableComponent />
      </div>
    </div>
    <!-- div que recoge horarios de entrenamiento, ultimas noticias y mensajes a los padres -->
    <div>
      <!-- Calendario de entrenamiento-->
      <CalendariComponent />
      <!-- div de ultimas notificaciones -->
      <NotificationComponent />
      
      <!-- div de mensajes a los padres -->
      <h1 class="text-3xl justify-center">Enviar mensaje al padre del jugador</h1>
        <div class="flex p-4 border border-gray-400">
          <form>
            <div class="p-2">
              <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="Asunto">Asunto</label>
              <input type="text" name="Asunto" id="inputAsunto" cols="70" placeholder="Introduce el asunto...">
            </div>

            <div class="p-2">
              <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="Motivo">Motivo</label>
              <textarea class="appearance-none block w-full bg-gray-200 text-gray-700 border border-black-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="textarea" name="Asunto" id="inputAsunto"  placeholder="Introduce un asunto..." ></textarea>
            </div>

            <div class="p-2">
              <input type="submit" value="Enviar"  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" />
            </div>
          </form>
        </div>
    </div>  
    <div class="w-1/4 p-4">
      <h2 class="text-lg font-bold mb-4">Lista de jugadores</h2>
      <ul class="w-full">
    <li class="flex items-center justify-between border-b border-gray-300 py-2">
      <span>Jugador 1</span>
      <span>Nº 1</span>
    </li>
    <li class="flex items-center justify-between border-b border-gray-300 py-2">
      <span>Jugador 2</span>
      <span>Nº 6</span>
    </li>
    <li class="flex items-center justify-between border-b border-gray-300 py-2">
      <span>Jugador 3</span>
      <span>Nº 13</span>
    </li>
    <li class="flex items-center justify-between border-b border-gray-300 py-2">
      <span>Jugador 4</span>
      <span>Nº 10</span>
    </li> 
      </ul>
    </div>
  </div>
  

</template>
<script setup>
import NavbarComponent from '@/components/layouts/NavbarComponent.vue';
import ClassificationTableComponent from '@/components/teams/ClassificationTableComponent.vue';
import NotificationComponent from '@/components/teams/NotificationComponent.vue';
import CalendariComponent from '@/components/teams/CalendariComponent.vue';
</script>