import { defineStore } from "pinia";
import { ref } from "vue";

export const useProfileStore = defineStore('showprofile', () => {
  const showProfile = ref(false);
  const data = ref({
    "name": "",
    "surname": "",
    "email": "",
    "address1": "",
    "address2": "",
    "team": ""
  })
  function changeModal() {
    showProfile.value = !showProfile.value;
  }

  return {
    showProfile,
    changeModal,
    data
  };
});
