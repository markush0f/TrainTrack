<template lang="html">
    <div v-if="sessionStore.sessions && sessionStore.sessions.length > 0" class="justify-center p-3">
        <h2 class="text-center font-bold mb-4">Notificaciones recientes</h2>
        <div class="w-full p-2 max-h-60 overflow-y-auto">
            <div class="b p-4 rounded-lg">
                <div class="mb-3">
                    <div v-for="(session, i) in sessions.session" :key="i">
                        <div v-if="i % 2 === 0" class="flex mb-3 items-center justify-center">
                            <div class="w-5/12 border border-main-green p-4 rounded-lg mr-3" :key="session.id">
                                <div class="relative">
                                    <h3 class="font-bold text-base mb-1">{{ session.title }}</h3>
                                    <button @click="deleteSession(session.id)"
                                        class="absolute text-lg font-bold top-0 right-0 -mt-3 -mr-1 text-gray-300 hover:text-red-500 focus:outline-none">
                                        X
                                    </button>
                                </div>
                                <p class="text-sm">{{ session.session }}.</p>
                                <span class="text-xs">{{ session.created_at }}</span>
                            </div>

                            <div class="w-5/12 border border-main-green p-4 rounded-lg mr-3"
                                v-if="sessions.session[i + 1]" :key="sessions.session[i + 1].id">
                                <div class="relative">
                                    <h3 class="font-bold text-base mb-1">{{ sessions.session[i + 1].title }}</h3>
                                    <button @click="deleteNotification(sessions.session[i + 1].id)"
                                        class="absolute text-lg font-semibold top-0 right-0 -mt-3 -mr-1 text-gray-300 hover:text-red-500 focus:outline-none">
                                        X
                                    </button>
                                </div>
                                <p class="text-sm">{{ sessions.session[i + 1].notification }}</p>
                                <span class="text-xs">{{ sessions.session[i + 1].created_at }}</span>
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
import { getAllSession } from '../../services/parentsAPI'
import { useSessionStore } from '../../stores/sessions'
const sessionStore = useSessionStore()

onMounted(async () => {
    await getAllSession()
})

</script>
