import { defineStore } from "pinia";
import { ref } from "vue";

export const usePlayerStore = defineStore("player", () => {
  const players = ref({});
  const playerMsg = ref(null);
  const player = ref(null);
  const playerToRemove = ref(null)
  return {
    players,
    playerMsg,
    player,
    playerToRemove,
  };
});

// Modal para mostrar y ocultar el div de crear jugador
export const useShowInsertPlayerStore = defineStore("insertplayer", () => {
  const showInsertPlayer = ref(false);

  function changeModal() {
    showInsertPlayer.value = !showInsertPlayer.value;
  }

  return {
    showInsertPlayer,
    changeModal,
  };
});

export const useRemovePlayerStore = defineStore('removeplayermodal', () => {
  const showRemovePlayer = ref(false)
  function changeModal() {
    showRemovePlayer.value = !showRemovePlayer.value;
  }
  return {
    changeModal,
    showRemovePlayer
  }
})

// export const usePlayerStore = defineStore("showplayertxt", () =>{
//   const
// })
