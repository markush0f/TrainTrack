<template>
    <div class="border-2 border-gray-300 rounded-md">
        <div class="py-1">
            <h1 class="text-2xl font-semibold mt-2 ml-2 text-gray-700">Perfil</h1>
        </div>
        <div class="py-2">
            <div class="border-b border-t py-1 border-gray-300">
                <h3 class="text-base font-medium text-gray-500 pr-2 ml-2">Nombre y apellidos:</h3>
                <h4 class="ml-2">{{ playerStore.player.name }} {{ playerStore.player.surname }}</h4>
            </div>
            <div class="border-b py-1">
                <h3 class="text-base font-medium text-gray-500 pr-2 ml-2">Entrenador:
                </h3>
                <h4 class="ml-2">{{ profileStore.data.name }} {{ profileStore.data.name }} </h4>
            </div>
            <div class=" py-1">
                <h3 class="text-base font-medium text-gray-500 pr-2 ml-2">Posición:</h3>
                <h4 class="ml-2">Delantero</h4>
            </div>
            <div class=" py-1">
                <h3 class="text-base font-medium text-gray-500 pr-2 ml-2">Goles y asistencias:</h3>
                <h4 class="ml-2">G: 10 A: 5</h4>
            </div>

        </div>
    </div>
</template>

<script setup>
import { usePlayerStore } from '@/stores/players';
import { onMounted } from 'vue';
import { useProfileStore } from '@/stores/profile';
const playerStore = usePlayerStore()
const profileStore = useProfileStore()

onMounted(async () => {
    if (profileStore.data.childrens) {
        console.log(profileStore.data);
        if (profileStore.data.rol === 'parent') {
            playerStore.player = profileStore.data.childrens
            console.log(await playerStore.player);
        }
    }
    console.log(await playerStore.player);
    console.log(profileStore.data);
})



</script>