<template>
  <div class="rounded-md overflow-hidden mb-2">
    <table class="table-auto">
      <thead>
        <tr class="bg-main-green border-2 border-dark-green">
          <th class="px-4 py-2 text-white" colspan="2">Club</th>
          <th class="px-4 py-2 text-white">PJ</th>
          <th class="px-4 py-2 text-white">W</th>
          <th class="px-4 py-2 text-white">D</th>
          <th class="px-4 py-2 text-white">L</th>
          <th class="px-4 py-2 text-white">PTS</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(team, index) in teams" class="border-2 border-third-green">
          <td class="px-4 py-2">{{ index + 1 }}.</td>
          <td class="px-4 py-2 pr-8">{{ team.name }}</td>
          <td class="px-4 py-2">{{ team.matchPlayed }}</td>
          <td class="px-4 py-2">{{ team.matchWinned }}</td>
          <td class="px-4 py-2">{{ team.matchLosed }}</td>
          <td class="px-4 py-2">{{ team.matchDrawed }}</td>
          <td class="px-4 py-2">0</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCategoryStore } from '@/stores/category';
import { listTeams } from '@/services/teamAPI';
const teams = ref([]);
const categoryStore = useCategoryStore()
onMounted(async () => {
  teams.value = await listTeams(categoryStore.category);
});
</script>
