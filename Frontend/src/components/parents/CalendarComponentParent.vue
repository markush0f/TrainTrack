<template>
        <VDatePicker :attributes="eventsInCalendar" :select-attribute="selectAttribute" expanded
            @dayclick="handleDayClick" locale="es" />
    
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCalendarStore } from '@/stores/calendar';


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

async function loadEventsInCalendar() {
    events.value.forEach(event => {
        eventsInCalendar.value.push(
            {
                id: event.id,
                title: event.title,
                time: event.dateTime,
                description: event.description,
                highlight: {
                    color: 'green',
                },
                dates: event.dateEvent,
            }
        )
    });
}

function handleDayClick(event) {
    console.log('Información del evento:', event);
    if (event.attributes[0]) {
        calendarStore.setEvent(event.attributes[0].id)
        console.log(calendarStore.getEvent());
    }

}

onMounted(async () => {
    // await loadEvents();
    events.value = calendarStore.getAllEvents();
    console.log(events.value);
    await loadEventsInCalendar()
    console.log(eventsInCalendar.value);
});
</script>