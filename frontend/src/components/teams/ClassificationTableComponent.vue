<template>
  <div class="rounded-md overflow-hidden">
    <table class="table-auto">
      <thead>
        <tr class="">
          <th class="px-4 py-2 text-green-700" colspan="2">Equipos</th>
          <th class="px-4 py-2 text-green-700">PJ</th>
          <th class="px-4 py-2 text-yellow-400">W</th>
          <th class="px-4 py-2 text-gray-400">D</th>
          <th class="px-4 py-2 text-red-500">L</th>
          <th class="px-4 py-2 text-gray-600">PTS</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(team, index) in teams" 
        :class="{
          'rounded-full': index < 5, 'border-l-4 border-green-700': index < 5,
          'border-l-4 border-yellow-400': index >= 5 && index < 8,
          'border-l-4 border-gray-400': index >= 8 && index < 12,
          'border-l-4 border-red-500': index >= 12
        }">
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
  <div class="flex justify-center p-10">

    <div class="border-b-4 border-b-green-700 mr-3">Ascenso</div>
    <div class="border-b-4 border-b-yellow-400 mr-3">Play-off</div>
    <div class="border-b-4 border-b-gray-400 mr-3">Permanencia</div>
    <div class="border-b-4 border-b-red-500 mr-3">Descenso</div>
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
