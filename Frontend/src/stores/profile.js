import { defineStore } from "pinia";
import { ref } from "vue";

export const useProfileStore = defineStore('showprofile', () => {
  const showProfile = ref(false);
  const data = ref({
    "name": "",
    "surname": "",
    "email": "",
    "address1": "",
    "address2": "",
    "team": ""
  })
  function changeModal() {
    showProfile.value = !showProfile.value;
  }
  function getDataProfile() {
    return data.value
  }

  return {
    showProfile,
    changeModal,
    getDataProfile,
    data
  };
});


export const useRolStore = defineStore('rol', () => {
  const rol = ref('')
  function setRol(newRol) {
    rol.value = newRol
  }
  function getRol(){
    return rol.value
  }
  return { 
    setRol,
    getRol,
    rol
  };
})