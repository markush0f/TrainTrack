import axios from "axios";
const URL = "http://127.0.0.1:8000/api/league/"
import { useTeamStore } from "@/stores/team";

// Solicitamos la lista de equipos
export async function listTeams(data) {
  data = {
    'category': "alevin"
  }
  try {
    const res = await axios.get(`${URL}teams`, { params: data })
    console.log(res.data.team);
    if (res.data.team) {
      // dataTeam = useTeamStore().dataTeams
      return res.data.team
    }
  } catch (e) {
    console.log("Error: ", e);
  }
}

// Solicitamos los escudos de los equipos
export async function listAllShields(){
  try{
  const res = await axios.get(`${URL}shields`)    
  console.log(res.data);
  return res.data.imgs
  }catch(e) {
    console.log("Error: ",e);
  }
}