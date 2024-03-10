import { defineStore } from "pinia";
import { inject } from "vue";
export const useCSRFStore = defineStore('CSRF', () => {
  const $cookies = inject('$cookies')
  const getCSRF = () => {
    return $cookies.get('csrftoken')
  }
  return {
    getCSRF
  }
})