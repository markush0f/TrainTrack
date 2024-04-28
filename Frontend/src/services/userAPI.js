import axios from "axios";
import { useCookies } from "vue3-cookies";
import { useProfileStore, useRolStore } from "@/stores/profile";
import { getUnverifiedParents } from "./parentsAPI";
import { useParentStore } from "@/stores/parents"
import { useErrorStore } from "@/stores/errors";
const URL = "http://127.0.0.1:8000/api/";
const { cookies } = useCookies();

// Solicitud de registro de oadre
export async function signup(data) {
  const res = await axios.post(`${URL}signup`, data);
  console.log("Datos enviados:", res.data);
  try {
    if (res) {
      const errorStore = useErrorStore();
      console.log("Respuesta del servidor: ", res.data);
      errorStore.errorEmailExist = ''
      errorStore.errorInvalidCodePassTeam = ''
      if (res.data.emailExist) {
        console.log('ya existe');
        errorStore.errorEmailExist = 'Este email ya existe, si ya esta registrado espere la confirmacion del entrenador.'
      }

      if (res.data.codePassNotExist = true) {
        console.log('Codigo equipo incorrecto');
        errorStore.errorInvalidCodePassTeam = 'Codigo o contraseña de equipo incorrecto.'
      }
      if (res.data.success) {
        console.log("Success:", res.data.success);
        window.location.href = "/registersuccess";
      }
    } else console.log("No hay respuesta del servidor");
    console.log("Datos enviado", res.data);
  } catch (e) {
    console.error("ERROR:", e);
  }
}

// Solicitud de login de padre
export async function login(data) {
  try {
    const res = await axios.post(`${URL}login`, data);
    if (res) {
      const errorStore = useErrorStore();
      console.log("Datos: ", res.data);
      console.log("Respuesta del servidor:", res);
      if (res.data.success) {
        console.log("Token:", res.data.token);
        cookies.set("token", res.data.token);
        errorStore.errorInvalidDateLogin = ''
        if (res.data.rol == "trainer") {
          window.location.href = "/trainer";
        } else if (res.data.rol == "parent") window.location.href = "/parent";
        else window.location.href = "/";
        // this.$router.push('/');
      } else {
        errorStore.errorInvalidDateLogin = 'Contraseña o email incorrectos'
      }
    }
  } catch (e) {
    console.log("ERROR: ", e);
  }
}
// Solicitud de información del usuario
export async function profile() {
  const token = cookies.get("token");
  if (token) {
    // console.log("TOKEN:", token);
    try {
      const headers = {
        Authorization: `Bearer ${token}`,
      };
      const res = await axios.get(`${URL}profile`, { headers });
      if (res) {
        console.log("Datos perfil: ", res.data);
        const profileData = res.data.profile;
        const profileStore = useProfileStore();
        profileStore.data.name = profileData.first_name;
        profileStore.data.surname = profileData.last_name;
        profileStore.data.email = profileData.email;
        profileStore.data.address1 = profileData.address1;
        profileStore.data.address2 = profileData.address2;
        profileStore.data.team = profileData.team;
        profileStore.data.rol = profileData.rol
        if (profileData.childrens) {
          console.log("tiene");
          profileStore.data.childrens = profileData.childrens;
        }
        // console.log(profile.getDataProfile());
      }
    } catch (e) {
      console.log("ERROR: ", e);
    }
  }
}

// Solicitud de JWT descodificado
// export async function decodeJWT() {
//   const token = cookies.get("token");
//   const headers = {
//     Authorization: `Bearer ${token}`,
//   };
//   try {
//     const res = await axios.post("/api/authenticatejwt", null, { headers });

//     const rolStore = useRolStore();
//     rolStore.setRol(res.data.rol);
//   } catch (e) {
//     console.log("Error al cargar el token: ", e);
//   }
// }

export async function manageRequestParent(decision, parentId) {
  const token = cookies.get("token");
  const data = {
    decision: decision,
    parentId: parentId,
  };
  const headers = {
    Authorization: `Bearer ${token}`,
  };
  console.log(data);
  try {
    const res = await axios.post(`${URL}managerequestparent`, data, {
      headers,
    });
    console.log("Data: ", res.data);
    if (res.data.success) {
      await getUnverifiedParents();
    }
  } catch (e) {
    console.log("Error: ", e);
  }
}
