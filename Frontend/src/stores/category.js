import { defineStore } from "pinia";
import { ref } from 'vue';

export const useCategoryStore = defineStore('category', () => {
  const category = ref('')

  function setCategory(newCategory) {
    category.value = newCategory;
  }

  function getCategory() {
    return category.value;
  }
  return {
    setCategory,
    getCategory
  }
})


