<template>
    <div class="border-2">
        <!-- NAV -->
        <div>
            Poner nombre del equipo y foto [foto-nombre]
        </div>
        <!-- MESSAGGES -->
        <div class=""></div>
        <!-- SEND MESSAGE -->
        <div class="">
            <form @submit.prevent="submitForm">
                <input type="text" placeholder="Enviar mensaje...">
                <button type="submit"><i class="gg-mail-forward"></i></button>
            </form>
        </div>
    </div>
</template>

<script setup>
import { useProfileStore } from '@/stores/profile';
const profile = useProfileStore()
const dataForum = {
    team: profile.data.team
}
const data = {
    // author,
    message: ''
}
</script>