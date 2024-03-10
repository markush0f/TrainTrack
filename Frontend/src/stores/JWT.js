import { defineStore } from "pinia";
import { inject } from 'vue'
export const useTokenUserStore = defineStore('tokenUser', () => {
  const $cookies = inject('$cookies');
  const setJWT = (newToken) => {
    $cookies.set('tokenUser', newToken, { expire: 7 })
  } 
  const getJWT = () => {
    return $cookies.get('tokenUser')
  }

  return {
    setJWT,
    getJWT
  }

})