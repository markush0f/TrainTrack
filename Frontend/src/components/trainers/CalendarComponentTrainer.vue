<template>
    <VDatePicker :attributes="calendarStore.eventsInCalendar" :select-attribute="selectAttribute" expanded
        @dayclick="handleDayClick" locale="es" />
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCalendarStore } from '@/stores/calendar';
import { loadEventsInCalendar } from '@/services/calendarAPI';
const calendarStore = useCalendarStore();
const events = ref([]);
const eventsInCalendar = ref([]);
const selectAttribute = ref(
    {
        highlight: {
            color: 'green',
            fillMode: 'light'
        }
    }
);



function handleDayClick(event) {
    console.log('Información del evento:', event);
    if (event.attributes[0]) {
        calendarStore.setEvent(event.attributes[0].id)
        console.log(calendarStore.getEvent());
    }

}

onMounted(async () => {
    // await loadEvents();
    // events.value = calendarStore.getAllEvents();
    await loadEventsInCalendar()
});
</script>