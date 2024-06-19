import axios from "axios";
import { useCookies } from "vue3-cookies";
import { useSessionStore } from "@/stores/sessions";
import { useCalendarStore } from "@/stores/calendar";
const { cookies } = useCookies();
const URL = "http://127.0.0.1:8000/api/";

export async function loadEvents() {
  const token = cookies.get("token");
  if (token) {
    try {
      const headers = {
        Authorization: `Bearer ${token}`,
      };
      const res = await axios.get(`${URL}session/calendar/events`, { headers });

      if (res.data.events) {
        console.log(res.data.events);
        const calendarStore = useCalendarStore();
        calendarStore.events = res.data.events
        console.log("Lista eventos: ", calendarStore.events);
        return res.data.events;
      }

    } catch (e) {
      console.log("Error: ", e);
    }
  }
}

// Crear nuevo evento
export async function createEvent(data) {
  const token = cookies.get("token");
  const headers = {
    Authorization: `Bearer ${token}`,
  };

  try {
    const res = await axios.post(`${URL}session/calendar/events/createevent`, data, { headers });
    console.log("Data new event: ", res);
    if (res.data.success) {
      // const calendarStore = useCalendarStore();
      // calendarStore.setEvent(res.data.event)
      const calendarStore = useCalendarStore()
      const event = res.data.event;
      console.log(event);
      await loadEvents();
      await loadEventsInCalendar();
      return true;
    }
  } catch (e) {
    console.log(e);
  }
}

// Eliminar evento
export async function removeEvent(id) {
  const token = cookies.get('token');
  const headers = {
    Authorization: `Bearer ${token}`,
  };
  const data = {
    id: id
  }
  console.log(data);
  try {
    const res = await axios.post(`${URL}session/calendar/events/removeevent`, data, { headers })
    console.log("Data: ", res);
    if (res.data.success) {
      // Eliminar en la store
      await loadEvents();
      await loadEventsInCalendar();
      return true;
    }
  } catch (e) {
    console.log(e);
  }
}

// Cargar eventos en el calendario
export async function loadEventsInCalendar() {
  const calendarStore = useCalendarStore();
  calendarStore.events.sort((a, b) => new Date(a.dateEvent) - new Date(b.dateEvent));
  calendarStore.events.forEach(event => {
    calendarStore.eventsInCalendar.push(
      {
        id: event.id,
        title: event.title,
        time: event.dateTime,
        description: event.description,
        highlight: {
          color: event.color,
        },
        dates: event.dateEvent,
      }
    )
  });
}