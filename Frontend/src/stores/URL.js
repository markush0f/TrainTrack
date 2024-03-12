import { defineStore } from "pinia";
import { inject } from 'vue'
export const useUrlAPIStore = defineStore('URLAPI', () => {
  const getURL = () => {
    return "http://127.0.0.1:8000/api/"
  }
  return getURL
})