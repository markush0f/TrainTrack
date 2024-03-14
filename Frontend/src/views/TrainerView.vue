<template>
  <NavbarComponent />
  <div class="flex h-full">
    <!-- div que recoge el escudo y la clasificacion -->
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
    <!-- div que recoge horarios de entrenamiento, ultimas noticias y mensajes a los padres -->
    <div class="flex-grow justify-center p-4">
      <!-- Calendario de entrenamiento-->
      <CalendarComponent />
      <!-- div de ultimas notificaciones -->
      <NotificationComponent />
      <!-- div de mensajes a los padres -->
      <div class="flex p-4 border border-gray-400">
        <form @submit.prevent="submitForm">
          <div class="p-2">
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
              class="bg-main-green hover:bg-green-700 text-white font-bold py-2 px-4 rounded-full" />
          </div>
        </form>
      </div>
    </div>
    <div class="w-1/4 p-4">
      <ListPlayersComponent/>
    </div>
  </div>



</template>
<script setup>
import NavbarComponent from '@/components/layouts/NavbarComponent.vue';
import ClassificationTableComponent from '@/components/teams/ClassificationTableComponent.vue';
import NotificationComponent from '@/components/teams/NotificationComponent.vue';
import CalendarComponent from '@/components/teams/CalendarComponent.vue';
import ListPlayersComponent from '@/components/players/ListPlayersComponent.vue';
import ProfileTrainerComponent from '@/components/trainers/ProfileTrainerComponent.vue';
</script>
<style scoped>
.logo {
  width: 200px;
}
</style>