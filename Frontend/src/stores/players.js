import { defineStore } from "pinia";
import { inject } from "vue";
import { ref } from "vue";

export const usePlayerStore = defineStore("player", () => {
  const players = ref([]);
  const playerMsg = ref(null);
  const player = ref({});
  return {
    players,
    playerMsg,
    player,
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

// export const usePlayerStore = defineStore("showplayertxt", () =>{
//   const
// })
