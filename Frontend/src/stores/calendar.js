import { defineStore } from "pinia";
import { ref } from "vue";

export const useCalendarStore = defineStore("calendar", () => {
  const events = ref({});
  const event = ref(null);
  const addEventOption = ref(false);
  const eventsInCalendar = ref([]);

  function setEvent(newEvent) {
    events.value.push(newEvent);
  }

  function getEvent() {
    return event.value;
  }

  async function setEvent(id) {
    event.value = events.value.filter((event) => event.id === id);
  }

  function getAllEvents() {
    return events.value;
  }

  function setAllEvents(listEvents) {
    events.value = listEvents
  }

  function cancelEvent() {
    event.value = null
  }



  return {
    setEvent,
    getEvent,
    getAllEvents,
    setAllEvents,
    cancelEvent,
    addEventOption,
    events,
    eventsInCalendar
  };
});
