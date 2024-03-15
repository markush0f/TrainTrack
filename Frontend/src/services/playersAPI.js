import axios from "axios";
import { useCookies } from "vue3-cookies";

const { cookies } = useCookies();
const URL = "http://127.0.0.1:8000/api/players"

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
      if (res.data.players) {
        console.log("Jugadores:", res.data);
        return res.data.players
      }
    } catch (e) {
      console.log("Error:", e);
    }

  }
}

// Solicitamos la creación de un jugador
export async function createPlayer(data) {
  const token = cookies.get('token')
  console.log("Jugador:", data);
  if (token) {
    try {
      const headers = {
        'Authorization': `Bearer ${token}`
      }
      const res = await axios.post(`${URL}`, data, { headers })

      if (res.data.success) {
        return true;
      }
    } catch (e) {
      console.log("Error:", e);
    }

  }
}