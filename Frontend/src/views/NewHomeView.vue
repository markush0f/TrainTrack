<template>
    <div class="flex flex-col items-center">
        <!-- Contenedor del texto de bienvenida -->
        <NavBar />
        <div class="relative">
            <h1 class="mt-3 text-xl font-semibold">Bienvenido a TRAIN TRACK!!</h1>
            <!-- Aquí va el contenido de tu componente -->
        </div>
        <div class="grid place-items-center h-screen">
            <!-- Contenedor para los divs de registro -->
            <div class="flex justify-center items-center space-x-8">
                <!-- Signup Parent -->
                <div class="p-4 max-w-md">
                    <router-link to="/parent" class="max-w-full">
                        <div class="bg-gray-100 p-8 rounded-lg shadow-lg hover:shadow-xl transition duration-300">
                            <h2 class="text-2xl font-semibold mb-4">Entrar como padre</h2>
                            <p class="text-gray-700">Si no tienes cuenta, primero registra el equipo al que pertenece tu
                                hijo.</p>
                        </div>
                    </router-link>
                </div>
                <!-- Signup Trainer -->
                <div class="p-4 max-w-md">
                    <router-link to="/trainer" class="max-w-full">
                        <div class="bg-gray-100 p-8 rounded-lg shadow-lg hover:shadow-xl transition duration-300">
                            <h2 class="text-2xl font-semibold mb-4">Entrar como entrenador</h2>
                            <p class="text-gray-700">Si no tienes cuenta, primero registra el equipo al que perteneces.
                            </p>
                        </div>
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

import NavBar from '@/components/layouts/NavbarComponent.vue';
</script>