<template>
    <transition name="fade">
        
    <div v-if="calendarStore.addEventOption" class="border-t-4">
        <div class="mt-2">
            <form @submit.prevent="submitForm">
                <label for="title" class="block mb-2 font-medium text-green-700 ">Título del evento</label>
                <input type="text" id="title" v-model="data.title"
                    class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs">

                <label for="Descripción" class="block mb-2 font-medium text-green-700 mt-2">Descripcion del
                    evento</label>
                <input type="text" id="small-input" v-model="data.description"
                    class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs">

                <div class="flex w-full">
                    <div class="mr-4 ">
                        <label for="title" class="mb-2 font-medium text-green-700 block mt-2">Fecha del
                            evento</label>
                        <VDatePicker v-model="date" :select-attribute="selectAttribute" :popover="false">
                            <template #default="{ togglePopover, inputValue, inputEvents }">
                                <div class="flex rounded-lg border border-gray-300 overflow-hidden">
                                    <button type="button"
                                        class="flex justify-center items-center px-2 bg-accent-100 hover:bg-accent-200 text-accent-700 border-r border-gray-300"
                                        @click.stop="togglePopover">
                                        <i class="gg-calendar"></i>
                                    </button>
                                    <input :value="inputValue" v-on="inputEvents"
                                        class="flex-grow px-2 py-1 bg-white" />
                                </div>
                            </template>
                        </VDatePicker>
                        <VDatePicker v-model="date" mode="time" class="mt-2 mb-2" hide-time-header />
                        <label for="title" class="block mb-2 font-medium text-green-700 ">Color del evento</label>
                        <div class="flex  mt-2 mb-2 space-x-1">
                            <input type="radio" id="color-red" name="color" value="red" v-model="data.color"
                                class="hidden">
                            <input type="radio" id="color-yellow" name="color" value="yellow" v-model="data.color"
                                class="hidden">
                            <input type="radio" id="color-green" name="color" value="green" v-model="data.color"
                                class="hidden">
                            <input type="radio" id="color-blue" name="color" value="blue" v-model="data.color"
                                class="hidden">
                            <label for="color-red"
                                class="cursor-pointer w-6 h-6 rounded-full border border-gray-300 bg-red-500 flex items-center justify-center hover:border-2 hover:border-red-700"
                                :class="{ 'border-red-700 border-4': data.color === 'red' }">
                                <span class="sr-only">Rojo</span>
                            </label>
                            <label for="color-green"
                                class="cursor-pointer  w-6 h-6 rounded-full border border-gray-300 bg-green-500 flex items-center justify-center hover:border-2 hover:border-green-700"
                                :class="{ 'border-green-700 border-4': data.color === 'green' }">
                                <span class="sr-only">Verde</span>
                            </label>
                            <label for="color-blue"
                                class="cursor-pointer  w-6 h-6 rounded-full border border-gray-300 bg-blue-500 flex items-center justify-center hover:border-2 hover:border-blue-700"
                                :class="{ 'border-blue-700 border-4': data.color === 'blue' }">
                                <span class="sr-only">Azul</span>
                            </label>
                            <label for="color-yellow"
                                class="cursor-pointer  w-6 h-6 rounded-full border border-gray-300 bg-yellow-500 flex items-center justify-center hover:border-2 hover:border-yellow-700"
                                :class="{ 'border-yellow-600 border-4': data.color === 'yellow' }">
                                <span class="sr-only">Amarillo</span>
                            </label>
                        </div>

                    </div>
                </div>
                <div>
                    <button
                        class="flex-grow px-10 py-1.5 font-medium bg-gray-500 hover:bg-gray-600 hover:text-white text-white rounded-lg ">
                        Aceptar
                    </button>
                    <button type="button" @click="cancelForm()"
                        class="flex-grow px-10 py-1.5 font-medium bg-red-500 hover:bg-red-600 hover:text-white text-white rounded-lg ml-10">
                        Cancelar
                    </button>



                </div>
            </form>
        </div>
    </div>
</transition>
</template>


<script setup>
import { useCalendarStore } from '@/stores/calendar';
import { onMounted, ref } from 'vue';
import { createEvent } from '@/services/calendarAPI';

const calendarStore = useCalendarStore();
const date = ref(new Date())
const selectAttribute = ref(
    {
        highlight: {
            color: 'green',
            fillMode: 'light'
        }
    }
);
const event = ref();
const data = ref({
    title: '',
    description: '',
    date: '',
    time: '',
    color: ''
})
function cancelForm() {
    console.log(data.value);
    calendarStore.addEventOption = false;
}
async function submitForm() {
    const formatted = formatDate(date.value);
    console.log(formatted.formattedTime);
    data.value.date = formatted.formattedDate;
    data.value.time = formatted.formattedTime;
    console.log(data.value);
    await createEvent(data.value)

}

function formatDate(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');
    const seconds = String(date.getSeconds()).padStart(2, '0');

    const formattedDate = `${year}-${month}-${day}`;
    const formattedTime = `${hours}:${minutes}:${seconds}`;

    return { formattedDate, formattedTime };
}
onMounted(async () => {
    // if (calendarStore.getEvent()) {
    //     event = calendarStore.getEvent()[0];
    //     console.log(event);

    // }
})

</script>