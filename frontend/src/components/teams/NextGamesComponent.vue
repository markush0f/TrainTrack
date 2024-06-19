<template>
    <div class="max-w-4xl mx-auto py-8">
        <h2 class="text-2xl font-bold text-center p-4 text-green-700">Proximos partidos</h2>
        <div class="overflow-x-auto">
            <table class="table-auto w-full">
                <thead>
                    <tr>
                        <th class="px-4 py-2">Equipo Local</th>
                        <th class="px-4 py-2">Fecha</th>
                        <th class="px-4 py-2">Equipo Visitante</th>
                    </tr>
                </thead>
                <tbody>
                    <template v-for="(match, index) in matches" :key="index">
                        <tr :class="index % 2 === 0 ? 'bg-gray-100' : 'bg-white'">
                            <td class="border px-4 py-2">
                                {{ index % 2 === 0 ? match.localTeam : match.visitorTeam }}
                            </td>
                            <td class="border px-4 py-2 flex justify-center">-</td>
                            <td class="border px-4 py-2">
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
    for (let i = 0; i < 7; i++) {
        if (!matches.value.some((match) => match.visitorTeam === listTeam.value[i])) {
            matches.value.push({ localTeam: profileStore.team, visitorTeam: listTeam.value[i].name });
        }
    }
}


onMounted(async () => {
    listTeam.value = await listTeams();
    await loadMatches();
});
</script>