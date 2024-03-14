import axios from 'axios';
import { useCookies } from "vue3-cookies";
const URL = "http://127.0.0.1:8000/api/"
const { cookies } = useCookies();

// Solicitud para recoger la lista de las notificaciones
export async function listNotifications() {
  const token = cookies.get('token')
  const headers = {
    'Authorization': `Bearer ${token}`
  };
  try {
    const res = await axios.get(`${URL}session/trainer/messages/listnotifications`, null, { headers });
    if (res.data.notifications) {
      console.log(res.data);
      return res.data.notifications
    } else console.log("No hay notificaciones");
  } catch (e) {
    console.log("Error al cargar el token: ", e);
  }
}