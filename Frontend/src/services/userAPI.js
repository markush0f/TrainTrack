import axios from 'axios';
import { useCookies } from "vue3-cookies";
import { useProfileStore, useRolStore } from '@/stores/profile';
const URL = "http://127.0.0.1:8000/api/"
const { cookies } = useCookies();

// Solicitud de registro
export async function signup(data) {
  const res = await axios.post(`${URL}signup`, data)
  console.log("Datos enviados:", res.data);
  try {
    if (res) {
      console.log("Respuesta del servidor: ", res);
      if (res.data.JWT && res.data.success) {
        console.log('Token:', res.data.JWT);
        // Almacenamos el token en las cookies
        cookies.set('token', res.data.JWT)
        this.$router.push('/');
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
      // Almacenamos el token en las cookies
      if (res.data.success) {
        console.log('Token:', res.data.JWT);
        cookies.set('token', res.data.JWT)
        if (res.data.rol == "trainer") {
          window.location.href = "/trainer"
        } else if (res.data.rol == "parent")
          window.location.href = "/parent"
        else window.location.href = "/"
        // this.$router.push('/');
      }
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
        'Authorization': `Bearer ${token}`
      }
      const res = await axios.get(`${URL}profile`, { headers })
      if (res) {
        // console.log('Datos: ', res.data);
        const profileData = res.data.profile
        const profile = useProfileStore()
        profile.data.name = profileData.first_name
        profile.data.surname = profileData.last_name
        profile.data.email = profileData.email
        profile.data.address1 = profileData.address1
        profile.data.address2 = profileData.address2
        profile.data.team = profileData.team
        profile.data.childrens = "..."
        // console.log(profile.getDataProfile());
      }
    } catch (e) {
      console.log("ERROR: ", e);
    }
  }
}

// Solicitud de JWT descodificado
export async function decodeJWT() {
  const token = cookies.get('token')
  const headers = {
    'Authorization': `Bearer ${token}`
  };
  try {
    const res = await axios.post('/api/authenticatejwt', null, { headers });

    const rolStore = useRolStore()
    rolStore.setRol(res.data.rol)
  } catch (e) {
    console.log("Error al cargar el token: ", e);
  }
}