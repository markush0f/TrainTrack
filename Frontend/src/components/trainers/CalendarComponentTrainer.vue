<template>
    <div class="flex-grow flex justify-center p-4 h-full">
        <form @submit.prevent="addEvent">
            <label for="newEventDate">Fecha del nuevo evento:</label>
            <input type="date" id="newEventDate" v-model="newEventDate" required>
            <button type="submit">Añadir evento</button>
        </form>

        <VDatePicker :attributes="events" expanded mode="dateTime" is24hr />
    </div>
</template>

<script setup>
import { ref } from 'vue';

// Variables de estado
const newEventDate = ref('');
const date = new Date();
const year = date.getFullYear();
const month = date.getMonth();
const events = ref([
    {
        key: 'today',
        highlight: {
            color: 'green',
            fillMode: 'solid',
            contentClass: 'italic',
        },
        dates: new Date(year, month, 12),
    },
    {
        highlight: {
            color: 'green',
            fillMode: 'light',
        },
        dates: new Date(year, month, 13),
    },
    {
        highlight: {
            color: 'green',
            fillMode: 'outline',
        },
        dates: new Date(year, month, 14),
    },
]);

// Método para agregar un nuevo evento
const addEvent = () => {
    if (newEventDate.value) {
        const newDate = new Date(newEventDate.value);
        events.value.push({
            highlight: {
                color: 'blue', // Puedes cambiar el color según tu preferencia
                fillMode: 'solid',
            },
            dates: newDate,
        });
        newEventDate.value = ''; // Limpiar el input después de agregar el evento
    }
};
</script>



<!--     <div class="flex-grow flex justify-center p-4 h-full"> -->