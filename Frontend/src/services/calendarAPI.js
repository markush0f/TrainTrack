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
        calendarStore.setAllEvents(res.data.events)
        console.log(calendarStore.getAllEvents());
      }

    } catch (e) {
      console.log("Error: ", e);
    }
  }
}
