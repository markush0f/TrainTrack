import { useCookies } from "vue3-cookies";
import { defineStore } from "pinia";

export const useCookiesStore = defineStore('cookies', () => {
  const { cookies } = useCookies();
  const setCookie = (key, value) => {
    cookies.set(key, value)
  }
  const getCookie = (key) => {
    return cookies.get(key)
  }
  const removeCookie = (key) => {
    cookies.remove(key)
  }
  return {
    setCookie,
    getCookie,
    removeCookie
  }
})


