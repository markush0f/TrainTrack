import "./assets/style.css";
import { createApp } from "vue";
import { createPinia } from "pinia";
import VueCookies from "vue3-cookies";
import App from "./App.vue";
import router from "./router";
import axios from "axios";
import { setupCalendar, Calendar, DatePicker } from "v-calendar";
import "v-calendar/style.css";


axios.defaults.baseURL = "http://127.0.0.1:8000";

const app = createApp(App);
app.use(createPinia()).use(router, axios).use(VueCookies, {
  expires: "7d",
});
app.use(setupCalendar, {});
app.component("VCalendar", Calendar);
app.component("VDatePicker", DatePicker);
app.mount("#app");
