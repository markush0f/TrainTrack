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

export const useCategoryStore = defineStore('category', ()=>{
  const category = ref([])
  function setCategory(category){
    category.value = category
  }
  return{
    category
  }
})