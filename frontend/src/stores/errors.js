import { defineStore } from "pinia";
import { ref } from "vue";

export const useErrorStore = defineStore('errors', () => {

    const errorInvalidDateLogin = ref('')
    const errorEmailExist = ref('')
    const errorInvalidCodePassTeam = ref('')
    return {
        errorInvalidDateLogin, 
        errorEmailExist,
        errorInvalidCodePassTeam
    }
})


