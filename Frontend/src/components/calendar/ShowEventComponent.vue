<template>
    <div v-if="events.length > 1 && !calendarStore.getEvent()">
        <div v-for="(event, i) in events" :key="i" class="p-1">
            <div class="overflow-hidden  rounded-xl bg-white border border-green-500 flex flex-col items-center">
                <div class="text-center pt-1"> 
                    {{ event.title }}
                </div>
                <div class="mt-2 mb-2 text-center">
                    <p class="text-gray-700">{{ event.description }}</p>
                </div>
            </div>
        </div>
    </div>
    <div v-else-if="calendarStore.getEvent()" class="flex justify-center items-center h-screen">
        seleccionado
    </div>
    
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCalendarStore } from '@/stores/calendar';
import { loadEvents } from '@/services/calendarAPI';
const calendarStore = useCalendarStore();
const events = ref([])

onMounted(async () => {
    // await loadEvents();
    events.value = calendarStore.getAllEvents();
    console.log(events.value);
    console.log(calendarStore.getEvent());
})
</script>