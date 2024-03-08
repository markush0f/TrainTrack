import axios from 'axios';


// Solicitued de subscripción
export async function signup(data) {
  try {
    console.log("Aqui tb");
    const res = await axios.post("http://127.0.0.1:8000/api/createtrainer", data)
    console.log("Datos enviado", res.data);
  } catch (e) {
    console.error("ERROR:", e);
  }

}

