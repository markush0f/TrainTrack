<template>
  <div class="min-h-screen">
    <NavbarComponent />

    <div class="flex flex-col lg:flex-row h-full">
      <div class="lg:w-1/4 p-4 overflow-y-auto">
        <div class="justify-center p-4">
          <ShieldComponent />
          <PlayerInfoParentComponent />
          <LastGamesComponent />
          <NextGamesComponent />
        </div>
      </div>

      <div class="lg:w-1/2 flex-grow p-4">
        <div class="hidden lg:flex justify-center">
          <CalendarComponentParent />
        </div>
        <div v-if="!profileStore.showProfile">
          <div class="lg:hidden mb-4">
            <CalendarComponentParent />
          </div>
        </div>
        <ListSessionsParent class="border-b-4" />
        <ForumView />
      </div>
      <div class="lg:w-1/4 p-4">
        <div class="hidden lg:block">
          <ShowEventComponent class="p-4" />
          <SendNoticeComponent class="p-3 pb-20" />
        </div>
        <ClassificationTableComponent />
      </div>
    </div>
  </div>
</template>

<script setup>
import NavbarComponent from "@/components/layouts/NavbarComponent.vue";
import ClassificationTableComponent from "@/components/teams/ClassificationTableComponent.vue";
import SendNoticeComponent from "@/components/parents/SendNoticeComponent.vue";
import ListSessionsParent from "@/components/parents/ListSessionsParent.vue";
import { onMounted } from "vue";
import PlayerInfoParentComponent from "@/components/players/PlayerInfoParentComponent.vue";
import { usePlayerStore, useShowInsertPlayerStore } from "@/stores/players";
import { useProfileStore } from "@/stores/profile";
import CalendarComponentParent from "@/components/parents/CalendarComponentParent.vue";
import ShowEventComponent from "@/components/calendar/ShowEventComponent.vue";
import LastGamesComponent from "@/components/teams/LastGamesComponent.vue";
import NextGamesComponent from "@/components/teams/NextGamesComponent.vue";
import ShieldComponent from "@/components/teams/ShieldComponent.vue";
import ForumView from "../forum/ForumView.vue";

const playerStore = usePlayerStore();
const profileStore = useProfileStore();

onMounted(async () => {
  playerStore.player = profileStore.childrens;
});
</script>
<style scoped>
.session {
  width: 600px;
}

.profile {
  width: 30%;
}
</style>
