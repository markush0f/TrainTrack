import { defineStore } from "pinia";
import { ref } from "vue";

export const useSessionStore = defineStore("session", async () => {
  const sessions = ref(null);
  return {
    sessions,
  };
});
