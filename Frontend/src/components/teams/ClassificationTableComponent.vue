<template>
  <select v-model="category"
    class="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline">
    <option value="" disabled selected>Selecciona una categoría</option>
    <option value="prebenjamin">Prebenjamin</option>
    <option value="benjamin">Benjamin</option>
    <option value="alevin">Alevin</option>
    <option value="infantil">Infantil</option>
  </select>
  <table class="table-auto">
    <thead class>
      <tr class="bg-main-green">
        <!-- <th class="px-4 py-2"></th> -->
        <th class="px-4 py-2 " colspan="2">Club</th>
        <th class="px-4 py-2">PJ</th>
        <th class="px-4 py-2">W</th>
        <th class="px-4 py-2">D</th>
        <th class="px-4 py-2">L</th>
        <th class="px-4 py-2">PTS</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(team, index) in teams" class="hover:bg-gray-100">
        <td class="px-4 py-2">{{ index + 1 }}.</td>
        <td class="px-4 py-2 pr-8 "> {{ team.name }}</td>
        <td class="px-4 py-2">{{ team.matchPlayed }}</td>
        <td class="px-4 py-2">{{ team.matchWinned }}</td>
        <td class="px-4 py-2">{{ team.matchLosed }}</td>
        <td class="px-4 py-2">{{ team.matchDrawed }}</td>
        <!-- <td>{{ team.}}</td> -->
        <td class="px-4 py-2">0</td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useTeamStore } from '@/stores/team';
import { listTeams } from '@/services/teamAPI';

const category = ref('prebenjamin');
const teams = ref([]);

onMounted(async () => {
  console.log("Cargando equipos...");
  teams.value = await listTeams(category.value);
});
</script>
