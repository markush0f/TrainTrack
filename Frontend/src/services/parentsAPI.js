import axios from "axios";
import { useCookies } from "vue3-cookies";

const { cookies } = useCookies();
const URL = "http://127.0.0.1:8000/api/"

// Solicitamos la lista de todos los jugadores según el entrenador
export async function listParentsByTrainer() {
  const token = cookies.get('token')
  if (token) {
    try {
      const headers = {
        'Authorization': `Bearer ${token}`
      }
      const res = await axios.get(`${URL}parents/bytrainer`, { headers })
      if (res.data.parents) {
        console.log("Padres:", res.data);
        return res.data.parents
      }
    } catch (e) {
      console.log("Error:", e);
    }

  }
}

// Solicitamos la creación de una notificación de un padre al entrenador
export async function sendNotification(data) {
  const token = cookies.get('token')
  if (token) {
    try {
      const headers = {
        'Authorization': `Bearer ${token}`
      }
      const res = await axios.get(`${URL}parent/sendnotification`, { headers })
      if (res.data.parents) {
        console.log("Padres:", res.data);
        return res.data.parents
      }
    } catch (e) {
      console.log("Error:", e);
    }

  }
}

// Solicitamos la creación de un aviso de un padre al entrenador
export async function sendNotice(notice) {
  const token = cookies.get('token')
  if (token) {
    try {
      const headers = {
        'Authorization': `Bearer ${token}`
      }
      const res = await axios.get(`${URL}parent/sendnotification`, { headers })
      if (res.data.notice) {
        console.log("Advertencia:", res.data);
      }
    } catch (e) {
      console.log("Error:", e);
    }

  }
}