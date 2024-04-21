<template>
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
                        <label for="title" class="mb-2 font-medium text-green-700 block mt-2">Selecciona la fecha del
                            evento</label>
                        <VDatePicker v-model="date" :select-attribute="selectAttribute" :popover="false">
                            <template #default="{ togglePopover, inputValue, inputEvents }">
                                <div class="flex rounded-lg border border-gray-300 overflow-hidden">
                                    <button
                                        class="flex justify-center items-center px-2 bg-accent-100 hover:bg-accent-200 text-accent-700 border-r border-gray-300"
                                        @click="() => togglePopover()">
                                        <i class="gg-calendar"></i>
                                    </button>
                                    <input :value="inputValue" v-on="inputEvents"
                                        class="flex-grow px-2 py-1 bg-white" />
                                </div>
                            </template>
                        </VDatePicker>
                        <div>
                            <VDatePicker v-model="date" mode="time" class="mt-2 mb-2" hide-time-header />

                        </div>
                        <div>
                        </div>

                    </div>
                </div>
                <button @click="addEvent()"
                    class=" w-full px-3 py-1.5 font-medium bg-gray-500 hover:bg-gray-600 hover:text-white text-white rounded-lg ">
                    Confirmar
                </button>
            </form>
        </div>
    </div>

</template>

<script setup>
import { useCalendarStore } from '@/stores/calendar';
import { ref } from 'vue';
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
const data = ref({
    title: '',
    description: '',
    date: '',
    time: ''
})

function submitForm() {
    const formatted = formatDate(date.value);
    console.log(formatted.formattedTime);
    data.value.date = formatted.formattedDate;
    data.value.time = formatted.formattedTime;
    console.log(data.value);
    createEvent(data.value)
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

</script>