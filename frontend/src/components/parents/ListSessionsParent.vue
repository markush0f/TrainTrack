<template lang="html">
    <div v-if="sessionStore.sessions && sessionStore.sessions.length > 0" class="justify-center p-3">
        <h2 class="text-center font-bold mb-4 text-green-700 text-2xl">Notificaciones recientes</h2>
        <div class="w-full p-2 max-h-64 overflow-y-auto">
            <div class="b p-4 rounded-lg">
                <div class="mb-3">
                    <div v-for="(session, i) in sessionStore.sessions" :key="i">
                        <div v-if="i % 2 === 0" class="flex mb-3 items-center justify-center">
                            <div class="w-5/12 border border-main-green p-4 rounded-lg mr-3" :key="session.id">
                                <div class="relative">
                                    <h3 class="font-bold text-base mb-1">{{ session.title }}</h3>

                                </div>
                                <p class="text-sm">{{ session.session }}.</p>
                                <span class="text-xs">{{ session.created_at }}</span>
                            </div>

                            <div class="w-5/12 border border-main-green p-4 rounded-lg mr-3"
                                v-if="sessionStore.sessions[i + 1]" :key="sessionStore.sessions[i + 1].id">
                                <div class="relative">
                                    <h3 class="font-bold text-base mb-1">{{ sessionStore.sessions[i + 1].title }}</h3>
                             
                                </div>
                                <p class="text-sm">{{ sessionStore.sessions[i + 1].session }}</p>
                                <span class="text-xs">{{ sessionStore.sessions[i + 1].created_at }}</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div v-else>
        <h2 class="text-center font-bold mb-4">No hay notificaciones recientes</h2>
    </div>
</template>
<script setup>
import { onMounted } from 'vue';
import { getAllSessions } from '@/services/parentsAPI';
import { useSessionStore } from '@/stores/sessions';
import { removeNotification } from '@/services/trainerAPI';
const sessionStore = useSessionStore()

onMounted(async () => {
    await getAllSessions()
    console.log(await sessionStore.sessions);
})

</script>
