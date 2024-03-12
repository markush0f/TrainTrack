import axios from 'axios';
import { useCookies } from "vue3-cookies";
import { useProfileStore } from '@/stores/profile';
const URL = "http://127.0.0.1:8000/api/"
const { cookies } = useCookies();

// Solicitud de registro
export async function signup(data) {
  const res = await axios.post(`${URL}signup`, data)
  console.log("Datos enviados:", res.data);
  try {
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
}

// Solicitud de login
export async function login(data) {
  try {
    const res = await axios.post(`${URL}login`, data)
    if (res) {
      console.log("Datos: ", res.data);
      console.log("Respuesta del servidor:", res);
      console.log('Token:', res.data.JWT);
      // Almacenamos el token en las cookies
      cookies.set('token', res.data.JWT)
    }
  } catch (e) {
    console.log("ERROR: ", e);
  }
}
// Solicitud de información del usuario
export async function profile() {
  const token = cookies.get('token')
  if (token) {
    // console.log("TOKEN:", token);
    try {
      const headers = {
        'Authorization': `Bearer ${(token)}`
      }
      const res = await axios.get(`${URL}profile`, { headers })
      if (res) {
        console.log('Datos: ', res.data);
        profileData = res.data.profile
        const profile = useProfileStore()
        profile.name = profileData.name
        profile.surname = profileData.surname
        profile.email = profileData.email
        profile.address1 = profileData.address1
        profile.address2 = profileData.address2
        profile.team = profileData.team
        profile.childrens = "..."
      }
    } catch (e) {
      console.log("ERROR: ", e);
    }
  }
}