import { defineStore } from "pinia";
import { ref } from "vue";

export const useNotificationsStore = defineStore("parent", async () => {
  const notifications = ref([]);
  return {
    notifications,
  };
});
