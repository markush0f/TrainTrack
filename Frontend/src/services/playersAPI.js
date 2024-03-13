import axios from "axios";
import { useCookies } from "vue3-cookies";

const { cookies } = useCookies();
const URL = "http://127.0.0.1:8000/api/players/"

// Solicitamos la lista de todos los jugadores

export async function listPlayers() {
  const token = cookies.get('token')
  if (token) {
    // console.log("TOKEN:", token);
    try {
      const headers = {
        'Authorization': `Bearer ${token}`
      }
      const res = await axios.get(`${URL}byteam`, { headers })
      if (res.data) {
        console.log("Datos:", res.data);
      }
    } catch (e) {
      console.log("Error:", e);
    }

  }
}