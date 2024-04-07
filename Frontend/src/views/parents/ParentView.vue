<template>
  <NavbarComponent />
  <div class="flex h-full">
    <div class="flex flex-col gap-4 h-screen p-6 overflow-y-auto">
      <!-- div del Escudo del equipo -->
      <div class="justify-center p-4">
        <!-- <img src="https://www.dyntra.org/new/wp-content/uploads/2018/07/federacion-canaria-futbol.jpg" alt="Federacion"
          class="logo"> -->
      </div>
      <!-- div de la clasificacion -->
      <div>
        <ClassificationTableComponent />
      </div>
    </div>
    <div class="flex-grow justify-center p-4 overflow-y-auto">
      <ListSessionsParent class="border-b-4"/>
      <PlayerInfoComponent />
    </div>

    <div class="w-1/4 p-4 overflow-y-auto">
      <!-- div de ficha del hijo -->
      <div class="justify-center p-4">
        <h2 class="text-lg font-bold text-center p-2">Ficha del hijo</h2>
        <button
          class="bg-main-green border-solid border-2 border-third-green hover:bg-green-700 text-white font-bold py-2 w-full rounded-full">Ficha
          del
          hijo</button><br><br>
        <!-- div de form para enviar aviso al entrenador. -->
        <div class="justify-center p-4">
          <SendNoticeComponent/>
          <div class="justify-center p-4">
            <h2 class="text-lg font-bold text-center p-2">Enviar mensaje al entrenador</h2><br>
            <form @submit.prevent="submitForm">
              <div class="p-2 w-full">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                  for="Asunto">Asunto</label>
                <input type="text" name="Asunto" id="inputAsunto" cols="70" placeholder="Introduce el asunto...">
              </div>

              <div class="p-2">
                <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                  for="Motivo">Motivo</label>
                <input type="text"
                  class="appearance-none block w-full bg-gray-200 text-gray-700  -black-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"
                  name="Asunto" id="inputAsunto" placeholder="Introduce un asunto...">
              </div>
              <div class="p-2">
                <input type="submit" value="Enviar"
                  class="bg-main-green hover:bg-green-700 text-white font-bold py-2 w-full rounded-full" />
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import NavbarComponent from '@/components/layouts/NavbarComponent.vue';
import ClassificationTableComponent from '@/components/teams/ClassificationTableComponent.vue';
import SendNoticeComponent from '@/components/parents/SendNoticeComponent.vue';
import ListSessionsParent from '@/components/parents/ListSessionsParent.vue'
import { ref, onMounted } from 'vue';
import PlayerInfoComponent from '@/components/players/PlayerInfoComponent.vue';
import { usePlayerStore } from '@/stores/players';
import { useProfileStore } from '@/stores/profile';
const playerStore = usePlayerStore()
const profileStore = useProfileStore()
onMounted(() => {
  playerStore.player = profileStore.childrens
  console.log("Player: ");
  console.log(playerStore);
})

</script>