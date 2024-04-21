<template>
    <div v-if="events.length > 1">
        <div class="flex justify-center">
            <h2 class="text-center text-xl font-semibold p-2 text-green-700">Próximos eventos</h2>
        </div>
        <div v-for="(event, i) in events" :key="i" class="p-1">
            <div class="overflow-hidden rounded-xl bg-white border border-green-600 flex flex-col items-center  "
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
                    <div class="pt-1 flex justify-center space-x-2 ">
                        <button @click="editEvent(event)"
                            class="px-3 py-1.5 font-medium bg-green-700 hover:bg-green-600 hover:text-white text-green-200 rounded-lg text-xs">
                            Editar
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div class="pt-1 flex justify-center">
            <button @click="newEvent()"
                class="flex-grow px-3 py-1.5 font-medium bg-green-700 hover:bg-green-600 hover:text-white text-white rounded-lg ">
                Añadir evento
            </button>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useCalendarStore } from '@/stores/calendar';
const calendarStore = useCalendarStore();
const events = ref([])

async function editEvent(event) {
    console.log("Usted pulso", event);
    calendarStore.setEvent(event.id);
    console.log(calendarStore.getEvent()[0]);
}

async function newEvent() {
    calendarStore.addEventOption = true;

}



onMounted(async () => {
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