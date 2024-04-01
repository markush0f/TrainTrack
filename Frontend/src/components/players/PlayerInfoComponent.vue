<template>
    <div class="border-2 border-gray-300 rounded-md">
        <div class="py-1">
            <h1 class="text-2xl font-semibold mt-2 ml-2 text-gray-700">Perfil del jugador</h1>
        </div>
        <div class="py-2">
            <div class="border-b border-t py-1">
                <h3 class="text-base font-medium text-gray-500 pr-2 ml-2">Nombre y apellidos:</h3>
                <h4 class="ml-2">{{ playerStore.player.name }} {{ playerStore.player.surname }}</h4>
            </div>
            <div class="border-b py-1">
                <h3 class="text-base font-medium text-gray-500 pr-2 ml-2">Padre:
                </h3>
                <h4 class="ml-2">{{ playerStore.player.parent }}</h4>
            </div>
            <div class="border-b py-1">
                <h3 class="text-base font-medium text-gray-500 pr-2 ml-2">DNI:</h3>
                <h4 class="ml-2">{{ playerStore.player.DNI }}</h4>
            </div>
            <div class=" py-1">
                <h3 class="text-base font-medium text-gray-500 pr-2 ml-2">Dirección:</h3>
                <h4 class="ml-2">{{ playerStore.player.address1 }} {{ playerStore.player.address1 }}</h4>
            </div>
        </div>
    </div>
</template>

<script setup>
import { usePlayerStore } from '@/stores/players';
import { onMounted } from 'vue';
const playerStore = usePlayerStore()

</script>