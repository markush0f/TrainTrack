import axios from "axios";
import { useCookies } from "vue3-cookies";
import { useNotificationsStore } from "@/stores/notifications.js";
const URL = "http://127.0.0.1:8000/api/";
const { cookies } = useCookies();

// Solicitud para recoger la lista de las notificaciones
export async function listNotifications() {
  const notificationsStore = useNotificationsStore();
  const token = cookies.get("token");
  // console.log(token);
  const headers = {
    Authorization: `Bearer ${token}`,
  };
  try {
    const res = await axios.get(
      `${URL}session/trainer/messages/listnotifications`,
      { headers }
    );
    console.log(res.data);
    if (res.data.notifications) {
      (await notificationsStore).notifications = res.data.notifications;
      console.log("Notificaciones: ", (await notificationsStore).notifications);
    } else console.log("No hay notificaciones");
  } catch (e) {
    // console.log("Error: ", e);
  }
}

// Solicitud para enviar la sesión
export async function sendSession(data) {
  const token = cookies.get("token");
  const headers = {
    Authorization: `Bearer ${token}`,
  };
  try {
    console.log(data);
    const res = await axios.post(`${URL}session/trainer/sendsession`, data, {
      headers,
    });
    console.log(res.data);
    // Poner un mensaje en pantalla de que se envio la sesión.
  } catch (e) {
    console.log("Error: ", e);
  }
}

// Solicitud para elimianr una notificación
export async function removeNotification(id) {
  const token = cookies.get("token");
  const headers = {
    Authorization: `Bearer ${token}`,
  };
  const data = {
    id: id,
  };
  try {
    const res = await axios.post(`${URL}session/removenotification`, data, {
      headers,
    });
    console.log("Data: ", res.data);
    if (res.data.success) {
      // Eliminar la notificación el en array
      console.log("Eliminado");
      return true;
    }
  } catch (e) {
    console.log("Error: ", e);
  }
}
