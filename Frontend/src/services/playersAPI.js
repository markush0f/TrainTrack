import axios from "axios";
import { useCookies } from "vue3-cookies";
import { useCategoryStore } from "@/stores/team";
const { cookies } = useCookies();
const URL = "http://127.0.0.1:8000/api/players"

// Solicitamos la lista de todos los jugadores según el equipo
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
        loadListPlayer()
        return true;
      }
    } catch (e) {
      console.log("Error:", e);
    }

  }
}
export async function loadListPlayer() {
  players.value = await listPlayers();
}

// Solicitamos la lista de todos los jugadores según la categoría
export async function playersByCategory() {
  const categoryStore = useCategoryStore();
  try {
    const category = categoryStore.category;
    const res = await axios.get(`${URL}/bycategory?category=${category}`);
    console.log("Categoría seleccionada:", res.data);
    if (res.data.players) {
      console.log("Jugadores por categoría:", res.data);
      return res.data.players;
    }
  } catch (e) {
    console.log("Error:", e);
  }
}