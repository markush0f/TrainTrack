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