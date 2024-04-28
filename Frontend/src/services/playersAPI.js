import axios from "axios";
import { useCookies } from "vue3-cookies";
import { useCategoryStore } from "@/stores/category";
import {
  useShowInsertPlayerStore,
  usePlayerStore,
  useRemovePlayerStore,
} from "@/stores/players";
const URL = "http://127.0.0.1:8000/api/players";
const { cookies } = useCookies();
// Solicitamos la lista de todos los jugadores según el equipo
export async function listPlayers() {
  const token = cookies.get("token");
  if (token) {
    try {
      const headers = {
        Authorization: `Bearer ${token}`,
      };
      const res = await axios.get(`${URL}byteam`, { headers });
      if (res.data.players) {
        const playerStore = usePlayerStore();
        playerStore.players = res.data.players;
        console.log(playerStore.players);
        return res.data.players;
      }
    } catch (e) {
      console.log("Error:", e);
    }
  }
}

// Solicitamos la creación de un jugador
export async function createPlayer(data) {
  const token = cookies.get("token");
  if (token) {
    try {
      const headers = {
        Authorization: `Bearer ${token}`,
      };
      const res = await axios.post(`${URL}`, data, { headers });
      if (res.data.success) {
        useShowInsertPlayerStore().showInsertPlayer = false
        await listPlayers();
        return true;
      }
    } catch (e) {
      console.log("Error:", e);
    }
  }
}

export async function removePlayer(data) {
  const token = cookies.get("token");
  if (token) {
    try {
      const headers = {
        Authorization: `Bearer ${token}`,
      };
      const res = await axios.post(`${URL}/removeplayer`, data, { headers });
      console.log(res);
      if (res.data.success) {
        console.log('Player removed');
        await listPlayers()
      }
    } catch (e) {
      console.log("Error:", e);
    }
  }
}

// Solicitamos la lista de todos los jugadores según la categoría
// export async function playersByCategory() {
//   const categoryStore = useCategoryStore();
//   try {
//     const category = categoryStore.getCategory();
//     const res = await axios.get(`${URL}/bycategory?category=${category}`);
//     // console.log("Categoría seleccionada:", res.data);
//     if (res.data.players) {
//       // console.log("Jugadores por categoría:", res.data);
//       return res.data.players;
//     }
//   } catch (e) {
//     console.log("Error:", e);
//   }
// }
