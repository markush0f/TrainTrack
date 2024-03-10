import { useCookiesStore } from '@/stores/cookies';
import axios from 'axios';
import { useCookies } from "vue3-cookies";

const { cookies } = useCookies();
// Solicitud de subscripción
export async function signup(data) {
  try {
    const res = await axios.post("http://127.0.0.1:8000/api/createtrainer", data)
    if (res) {
      console.log("Respuesta del servidor: ", res);
      if (res.data.JWT) {
        console.log('Token:', res.data.JWT);
        // Almacenamos el token en las cookies
        cookies.set('token', res.data.JWT)
      }
    } else console.log("No hay respuesta del servidor");
    console.log("Datos enviado", res.data);
  } catch (e) {
    console.error("ERROR:", e);
  }

  // eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo4fQ.SNKyI5nxOSsXwi38I2rHqB33-EmRlWVTQ8Ivwcon-tI
  // eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo5fQ._zzpXtxsHgEfl8i2-8PicXO95AQFk-gqDanXRre8bbI
}


// Solicitud de login
export async function login(data) {
  try {
    const res = await axios.post("http://127.0.0.1:8000/api/logintrainer", data)
    console.log("Datos: ", res.data);
    if (res) {
      console.log("Respuesta del servidor:", res);
    }
  } catch (e) {
    console.log("ERROR: ", e);
  }
}
