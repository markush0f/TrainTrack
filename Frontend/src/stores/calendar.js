import { defineStore } from "pinia";
import { ref } from "vue";

export const useCalendarStore = defineStore("calendar", () => {
  const events = ref([]);
  const event = ref(null)
  
  function setEvent(newEvent) {
    events.value.push(newEvent);
  }

  function getEvent() {
    return event.value;
  }

  function setEvent(id) {
    event.value = events.value.filter((event) => event.id === id);
  }

  function getAllEvents() {
    return events.value;
  }

  function setAllEvents(listEvents) {
    events.value = listEvents
  }

  return {
    setEvent,
    getEvent,
    getAllEvents,
    setAllEvents,
  };
});
