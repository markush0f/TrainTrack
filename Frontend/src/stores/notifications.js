import { defineStore } from "pinia";
import { ref } from "vue";

export const useNotificationsStore = defineStore("notification", async () => {
  const notifications = ref([]);
  return {
    notifications,
  };
});
