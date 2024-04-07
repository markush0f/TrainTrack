import axios from "axios";
import { useCookies } from "vue3-cookies";
import { useSessionStore } from "@/stores/sessions";
const { cookies } = useCookies();
const URL = "http://127.0.0.1:8000/api/";

// Solicitamos la lista de todos los jugadores según el entrenador
export async function listParentsByTrainer() {
  const token = cookies.get("token");
  if (token) {
    try {
      const headers = {
        Authorization: `Bearer ${token}`,
      };
      const res = await axios.get(`${URL}parents/bytrainer`, { headers });
      if (res.data.parents) {
        return res.data.parents;
      }
    } catch (e) {
      console.log("Error:", e);
    }
  }
}

// Solicitamos la creación de una notificación de un padre al entrenador
export async function sendNotification(data) {
  const token = cookies.get("token");
  if (token) {
    try {
      const headers = {
        Authorization: `Bearer ${token}`,
      };
      const res = await axios.get(`${URL}parent/sendnotification`, { headers });
      if (res.data.parents) {
        console.log("Padres:", res.data);
        return res.data.parents;
      }
    } catch (e) {
      console.log("Error:", e);
    }
  }
}

// Solicitamos la creación de un aviso de un padre al entrenador
export async function sendNotice(data) {
  const token = cookies.get("token");
  if (token) {
    try {
      const headers = {
        Authorization: `Bearer ${token}`,
      };
      const res = await axios.post(`${URL}session/parent/sendnotice`, data, {
        headers,
      });
      console.log("Respuestaa...::", res);
      if (res.data.notice) {
        console.log("Advertencia:", res.data);
      }
    } catch (e) {
      console.log("Error:", e);
    }
  }
}

// Solicitamos todos los padres que no estén verificados
export async function getUnverifiedParents() {
  const token = cookies.get("token");
  if (token) {
    try {
      const headers = {
        Authorization: `Bearer ${token}`,
      };
      const res = await axios.get(`${URL}getUnverifiedParents`, { headers });
      console.log(res.data);
      if (res.data.parents) {
        return res.data.parents; // Devuelve los datos obtenidos
      } else {
        return null;
      }
    } catch (e) {
      console.log("Error: ", e);
      return null;
    }
  } else {
    return null;
  }
}

// Solicitamos todas las notificaciones del entrenador al padre
export async function getAllSessions() {
  const token = cookies.get("token");
  const sessionStore = useSessionStore();
  if (token) {
    try {
      const headers = {
        Authorization: `Bearer ${token}`,
      };
      const res = await axios.get(`${URL}session/parent/listsessions`, {
        headers,
      });
      console.log("Dataaa ", res.data);
      if (res.data.sessions) {
        console.log("Sessione:", res.data);
        sessionStore.sessions = res.data.sessions;
      } else {
        useSessionStore.session = null;
      }
    } catch (e) {
      console.log("Error:", e);
    }
  }
}
