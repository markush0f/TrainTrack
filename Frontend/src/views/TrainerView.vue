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
      <!-- div de aviso de los entrenamientos -->
      <div class="justify-center p-4 border border-gray-400">  
        <h1 class="mb-4 text-4xl font-calibri leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-black text-center">Horarios de entrenamiento</h1>
        <table class="w-full border-collapse border border-gray-200">
  <thead>
    <tr>
      <th class="px-4 py-2 bg-green-500 border border-gray-200">L</th>
      <th class="px-4 py-2 bg-green-500 border border-gray-200">M</th>
      <th class="px-4 py-2 bg-green-500 border border-gray-200">X</th>
      <th class="px-4 py-2 bg-green-500 border border-gray-200">J</th> 
      <th class="px-4 py-2 bg-green-500 border border-gray-200">V</th>
      <th class="px-4 py-2 bg-red-300 border border-gray-200">S</th>
      <th class="px-4 py-2 bg-red-300 border border-gray-200">D</th>
    </tr>
  </thead>
  <tbody>
    <tr class="text-center">
      <td class="px-4 py-2 bg-green-300 border border-gray-200">F</td>
      <td class="px-4 py-2 bg-blue-300 border border-gray-200">19-21</td>
      <td class="px-4 py-2 bg-green-300 border border-gray-200">F</td>
      <td class="px-4 py-2 bg-blue-300 border border-gray-200">19-21</td>
      <td class="px-4 py-2 bg-green-300 border border-gray-200">F</td>
      <td class="px-4 py-2 bg-yellow-300 border border-gray-200">MD</td>
      <td class="px-4 py-2 bg-green-300 border border-gray-200">F</td>
    </tr>
  </tbody>
</table>

      </div>
      <!-- div de ultimas notificaciones -->
      <div class="justify-center p-4 border border-gray-400">  
            <h2 class="text-center font-bold mb-4">Notificaciones</h2>
        <div class="w-full p-4 max-h-60 overflow-y-auto">

      <div class="bg-gray-100 p-4 rounded-lg">
        <!-- Contenido de las notificaciones -->
        <!-- Aquí se mostrarían las notificaciones -->
        <div class="mb-4">Notificación 1</div>
        <div class="mb-4">Notificación 2</div>
        <div class="mb-4">Notificación 3</div>
        <div class="mb-4">Notificación 4</div>
        <div class="mb-4">Notificación 5</div>
        <div class="mb-4">Notificación 6</div>
        <div class="mb-4">Notificación 7</div>
        <div class="mb-4">Notificación 8</div>
        <div class="mb-4">Notificación 9</div>
        <div class="mb-4">Notificación 10</div>
        <!-- Fin del contenido de las notificaciones -->
      </div>
    </div>

      </div>
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
</script>