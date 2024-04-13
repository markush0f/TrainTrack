<template>
  <div>
    <NavbarComponent />
    <div class="flex h-full">
      <div class="flex flex-col gap-4 h-screen w-1/4 p-6 overflow-y-auto">
        <div>
          <!-- Comunicación-->
          <ListSessionsParent class="border-b-4" />
          <SendNoticeComponent />
        </div>
      </div>
      <div class="flex flex-col flex-grow justify-center p-4 h-full">
        <CalendarComponentParent />
        
        <ShowEventComponent />
      </div>
      <div class="w-1/4 p-4 overflow-y-auto">
        <div class="justify-center p-4">
          nombre y escudo del equipo
          <PlayerInfoComponent />
        </div>
        <ClassificationTableComponent />
      </div>
    </div>
  </div>
</template>

<script setup>
import NavbarComponent from '@/components/layouts/NavbarComponent.vue';
import ClassificationTableComponent from '@/components/teams/ClassificationTableComponent.vue';
import SendNoticeComponent from '@/components/parents/SendNoticeComponent.vue';
import ListSessionsParent from '@/components/parents/ListSessionsParent.vue'
import { onMounted } from 'vue';
import PlayerInfoComponent from '@/components/players/PlayerInfoComponent.vue';
import { usePlayerStore } from '@/stores/players';
import { useProfileStore } from '@/stores/profile';
import CalendarComponentParent from '@/components/parents/CalendarComponentParent.vue';
import ShowEventComponent from '@/components/calendar/ShowEventComponent.vue'
import { loadEvents } from '@/services/calendarAPI';
const playerStore = usePlayerStore()
const profileStore = useProfileStore()

onMounted(async () => {
  // await loadEvents();
  playerStore.player = profileStore.childrens;

})

</script>
