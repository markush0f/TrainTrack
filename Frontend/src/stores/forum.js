import { defineStore } from "pinia";
import { ref } from 'vue';

export const useForumStore = defineStore('forum', () => {
  const messagesForum = ref('')

  function setMessage(newForum) {
    messagesForum.value = newForum;
  }

  function getMessages() {
    return messagesForum.value;
  }

  return {
    setMessage,
    getMessages
  }
})

