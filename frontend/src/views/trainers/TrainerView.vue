<template>
  <div class="min-h-screen">
    <NavbarComponent />
    <div class="flex flex-col md:flex-row">
      <div class="flex flex-col gap-4 md:w-1/4 h-full p-6">
        <div>
          <ShieldComponent class="border-b-4" />
          <EditEventComponent class="mb-5 mt-2" />
          <AddEventComponent />
        </div>
        <LastGamesComponent />
        <NextGamesComponent />
      </div>
      <div class="flex-grow justify-center p-4">
        <div v-if="!storeShowPlayer.showInsertPlayer">
          <CalendarComponentTrainer />
        </div>
        <ListNotificationsTrainerComponent class="border-b-4" />
        <div class="flex flex-col p-4">
          <div v-if="playerStore.player != null">
            <PlayerInfoTrainerComponent />
            <SendSessionComponentTrainer />
          </div>
          <div v-else>
            <p class="text-center text-gray-400 text-2xl">
              Seleccione un jugador para acceder a sus características
            </p>
          </div>
        </div>
      </div>
      <div class="w-full md:w-1/4 p-4">
        <ListPlayersComponent />
        <ConfirmRemovePlayer />
        <br />
        <ListUnverifiedParents class="border-b-4" />
        <ClassificationTableComponent />
      </div>
    </div>
    <div></div>
  </div>
</template>
<script setup>
import NavbarComponent from "@/components/layouts/NavbarComponent.vue";
import ClassificationTableComponent from "@/components/teams/ClassificationTableComponent.vue";
import ListNotificationsTrainerComponent from "@/components/trainers/ListNotificationTrainerComponent.vue";
import ListPlayersComponent from "@/components/players/ListPlayersComponent.vue";
import SendSessionComponentTrainer from "@/components/trainers/SendSessionComponent.vue";
import ListUnverifiedParents from "@/components/parents/ListUnverifiedParents.vue";
import { listParentsByTrainer } from "@/services/parentsAPI";
import PlayerInfoTrainerComponent from "@/components/players/PlayerInfoTrainerComponent.vue";
import NextGamesComponent from "@/components/teams/NextGamesComponent.vue";
import { onMounted } from "vue";
import { usePlayerStore, useShowInsertPlayerStore } from "@/stores/players";
import ShieldComponent from "@/components/teams/ShieldComponent.vue";
import LastGamesComponent from "@/components/teams/LastGamesComponent.vue";
import CalendarComponentTrainer from "@/components/trainers/CalendarComponentTrainer.vue";
import EditEventComponent from "@/components/calendar/EditEventComponent.vue";
import AddEventComponent from "@/components/calendar/AddEventComponent.vue";
import ConfirmRemovePlayer from "@/components/players/ConfirmRemovePlayer.vue";

const playerStore = usePlayerStore();

const storeShowPlayer = useShowInsertPlayerStore();

onMounted(async () => {
  await listParentsByTrainer();
  console.log(playerStore.player);
});
</script>
<style scoped>
.logo {
  width: 200px;
}
</style>
