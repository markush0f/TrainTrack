<template>
    <div v-if="events.length > 1">
        <div class="flex justify-center">
            <h2 class="text-center text-lg font-semibold p-2 text-green-700">Próximos eventos</h2>
        </div>
        <div v-for="event in calendarStore.events" :key="i" class="p-1">
            <div class="overflow-hidden rounded-xl bg-white border border-green-600 flex flex-col items-center hover:bg-green-100 hover:border-2 cursor-pointer hover:cursor-pointer"
                @click="respondEvent(event)"
                :class="{ 'eventSelected': calendarStore.getEvent() && event.id === calendarStore.getEvent()[0].id }">
                <h3 class="text-center pt-1 font-medium">
                    {{ event.title }}
                </h3>
                <div class="mt-2 mb-2 text-center">
                    <h4 class="text-gray-700">
                        <span v-if="event.description">
                            {{ event.description }}, el
                        </span>
                        <span class="text-green-700 font-semibold">
                            {{ event.dateEvent }}
                        </span>
                        a las
                        <span class="text-green-700 font-semibold">
                            {{ event.dateTime }}
                        </span>
                    </h4>
                </div>
            </div>
        </div>
    </div>
</template>



<script setup>
import { onMounted, ref } from 'vue';
import { useCalendarStore } from '@/stores/calendar';
const calendarStore = useCalendarStore();
const events = ref([])

async function respondEvent(event) {
    console.log("Usted pulso", event);
    calendarStore.setEvent(event.id);
    console.log(calendarStore.getEvent()[0]);
}

onMounted(async () => {
    // await loadEvents();
    events.value = calendarStore.getAllEvents();
    console.log(events.value);
    console.log(calendarStore.getEvent());
})
</script>

<style scoped>
.eventSelected {
    overflow: hidden;
    border-radius: 0.75rem;
    background-color: #eafbf0;
    border: 2px solid #26aa57;
    display: flex;
    flex-direction: column;
    align-items: center;
    color: #0b7732
}
</style>