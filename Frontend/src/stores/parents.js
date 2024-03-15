import { defineStore } from "pinia";
import { listParentsByTrainer } from "@/services/parentsAPI";
import { ref } from "vue";

export const useParentStore = defineStore('parent', async () => {
  const parents = ref([]);
  parents.value = await listParentsByTrainer();
  console.log("Mas padres",parents.value);
  function getParents() {
    return parents.value;
  }

  return {
    parents,
    getParents
  };
});