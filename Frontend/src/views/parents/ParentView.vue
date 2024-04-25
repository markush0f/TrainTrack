<template>
  <div class="min-h-screen">
    <NavbarComponent />
    <div class="flex h-full">
      <div class="profile p-4 overflow-y-auto">
        <div class="justify-center p-4">
          <ShieldComponent />
          <PlayerInfoComponent />
          <LastGamesComponent />
          <NextGamesComponent />
        </div>
      </div>
      <div class="flex flex-col flex-grow justify-center p-4 h-full">
        <CalendarComponentParent />
        <ListSessionsParent class="border-b-4" />
        <ForumView />
      </div>

      <div class="flex flex-col p-4">
        <div>
          <ShowEventComponent class="p-4" />
          <SendNoticeComponent class="p-3 pb-20" />
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
import LastGamesComponent from '@/components/teams/LastGamesComponent.vue';
import NextGamesComponent from '@/components/teams/NextGamesComponent.vue';
import ShieldComponent from '@/components/teams/ShieldComponent.vue';
import ForumView from '../forum/ForumView.vue';
const playerStore = usePlayerStore()
const profileStore = useProfileStore()

onMounted(async () => {
  playerStore.player = profileStore.childrens;

})

</script>
<style scoped>
.session {
  width: 600px;
}

.profile {
  width: 30%;
}
</style>