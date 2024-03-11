import { defineStore } from "pinia";
import { ref } from "vue";
export const useRolStore = defineStore('rol', () => {
  const rol = ref('')
  function setRol(newRol) {
    rol.value = newRol
  }
  return { rol, setRol }
})