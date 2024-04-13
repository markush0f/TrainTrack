<template>
    <FullCalendar :options='calendarOptions'>
        <template v-slot:eventContent='arg'>
            <b>{{ arg.timeText }}</b>
            <i>{{ arg.event.title }}</i>
        </template>
    </FullCalendar>
</template>

<script setup>
import { ref } from 'vue';
import FullCalendar from '@fullcalendar/vue3';
import dayGridPlugin from '@fullcalendar/daygrid';
import interactionPlugin from '@fullcalendar/interaction';

const info = ref({
    view: null,
    date: '',
    events: []
});

const calendarOptions = ref({
    plugins: [dayGridPlugin, interactionPlugin],
    initialView: 'dayGridMonth',
    locale: 'es',
    events: [
        { title: 'event 1', date: '2024-04-01' },
        { title: 'event 2', date: '2024-04-01' },
        { title: 'event 3', date: '2019-04-02' }
    ],
    dateClick: function (arg) {
        info.value.events = []
        info.value.date = arg.dateStr;
        info.value.events = calendarOptions.value.events.filter(event => event.date === arg.dateStr);
        console.log(info.value);

    },
    dayHeaderFormat: { weekday: 'narrow' }, // Personalizar el formato del encabezado del día
});
</script>

<style scoped>
/* Estilos personalizados para el calendario */
.fc-daygrid-event-dot {
    width: 5px;
    /* Ancho del punto del evento */
}

.fc-daygrid-container {
    border-color: green !important;
    /* Color del borde del calendario */
}
</style>
