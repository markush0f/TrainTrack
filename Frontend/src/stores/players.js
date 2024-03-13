import { defineStore } from "pinia";
import { inject } from 'vue'
import { ref } from "vue";
export const usePlayerStore = defineStore('showplayer', () => {
  const player = ref({
    "name": "",
    "surname": "",
    "birth": "",
    "parent": "",
    "position": "",
    "dorsal": ""
  })

  function setPlayer(data) {
    player.name = data.name,
    player.surname = data.surname,
    player.birth = data.birth,
    position.bir
  }
})