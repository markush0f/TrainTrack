<template>
    <div>
        <div class="border-solid border-2 border-third-green rounded-md overflow-hidden p-2">
            <h3>Enviar evento global.</h3>
            <form @submit.prevent="submitForm">
                <div class="pt-2">
                    <input type="text" v-model="data.title"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5 dark:placeholder-gray-400"
                        placeholder="Asunto..." required />
                </div>
                <div class="pb-2 pt-2">
                    <input type="text" v-model="data.event"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5 dark:placeholder-gray-400"
                        placeholder="Sesión..." required />
                </div>
                <div class="pb-2 pt-2 flex justify-center">
                    <button type="submit"
                        class="px-5 py-2.5 font-medium bg-green-200 hover:bg-green-300 hover:text-green-600 text-green-500 rounded-lg text-xs mr-4">Enviar</button>
                    <!-- Cambia el tipo de botón de "submit" a "button" -->
                    <button type="button" @click="cancelSession"
                        class="px-5 py-2.5 font-medium bg-red-200 hover:bg-red-300 hover:text-red-600 text-red-500 rounded-lg text-xs">Cancelar</button>
                </div>
            </form>
        </div>
    </div>
</template>
<script setup>
import { ref } from 'vue'
const data = ref({})

function submitForm() {

}
</script>