<template>
  <div class="max-w-4xl mx-auto py-8">
    <h2 class="text-2xl font-bold text-center p-4 text-green-700">Últimos partidos</h2>
    <div class="overflow-x-auto">
      <table class="table-auto w-full">
        <thead>
          <tr>
            <th class="px-4 py-2">Equipo Local</th>
            <th class="px-4 py-2">Resultado</th>
            <th class="px-4 py-2">Equipo Visitante</th>
          </tr>
        </thead>
        <tbody>
          <template v-for="(match, index) in matches" :key="index">
            <tr :class="index % 2 === 0 ? 'bg-gray-100' : 'bg-white'">
              <td class="border px-4 py-2"
                :class="{ 'text-green-600': match.winner === 'local', 'text-red-600': match.winner === 'visitor' }">
                {{ index % 2 === 0 ? match.localTeam : match.visitorTeam }}
              </td>
              <td class="border px-4 py-2">{{ match.result }}</td>
              <td class="border px-4 py-2"
                :class="{ 'text-green-600': match.winner === 'visitor', 'text-red-600': match.winner === 'local' }">
                {{ index % 2 === 0 ? match.visitorTeam : match.localTeam }}
              </td>
            </tr>
          </template>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script setup>
import { listTeams } from '@/services/teamAPI';
import { useProfileStore } from '@/stores/profile';
import { onMounted, ref } from 'vue';

const profileStore = useProfileStore().data;
const listTeam = ref(null);
const matches = ref([]);

async function loadMatches() {
  const results = [
    '1 - 0', '2 - 1', '3 - 2', '2 - 2', '3 - 1', '4 - 0',
    '0 - 1', '1 - 2', '2 - 3', '2 - 2', '1 - 3', '0 - 4'
  ];
  for (let i = 0; i < 7; i++) {
    if (!matches.value.some((match) => match.visitorTeam === listTeam.value[i])) {
      const randomResultIndex = Math.floor(Math.random() * results.length);
      const randomResult = results[randomResultIndex];
      const winner = determineWinner(randomResult, listTeam.value[i].name);
      matches.value.push({ localTeam: profileStore.team, result: randomResult, visitorTeam: listTeam.value[i].name, winner });
    }
  }
}

function determineWinner(result) {
  const [localGoals, visitorGoals] = result.split(' - ').map(Number);
  if (localGoals > visitorGoals) {
    return 'local';
  } else if (localGoals < visitorGoals) {
    return 'visitor';
  } else {
    return null;
  }
}

onMounted(async () => {
  listTeam.value = await listTeams();
  await loadMatches();
});
</script>
