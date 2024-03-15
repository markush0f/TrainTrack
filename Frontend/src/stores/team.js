import { defineStore } from "pinia";
import { ref } from "vue";

export const useTeamStore = defineStore('teams', () => {
  const listTeams = ref([])
  function putListTeam(teams) {
    listTeams.value = [...teams]
  }
  return {
    listTeams
  }
})

export const useCategoryStore = defineStore('category', () => {
  const category = ref('category')
  function setCategory(newCategory) {
    category.value = newCategory
  }
  function getCategory() {
    return category.value
  }

  return {
    category,
    setCategory,
    getCategory
  }
})