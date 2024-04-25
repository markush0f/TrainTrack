<template>

    <body class="bg-gray-200">
        <div class="container mx-auto px-4 py-4">
            <h1 class="text-2xl font-semibold mb-4 text-green-700">{{dataForum.team}}</h1>
            <div class="space-y-4">
                <div class="bg-white p-3 rounded-lg shadow-md">
                    <h2 class="text-lg font-semibold mb-1">Autor</h2>
                    <p class="text-sm text-gray-700 mb-2">Contenido de la publicación. Aquí se puede incluir texto,
                        imágenes, enlaces, etc.</p>
                    <div class="flex items-center justify-between">
                    </div>
                </div>

                <div class="bg-white p-3 rounded-lg shadow-md">
                    <h2 class="text-lg font-semibold mb-1">Autor</h2>
                    <p class="text-sm text-gray-700 mb-2">Contenido de la publicación. Aquí se puede incluir texto,
                        imágenes, enlaces, etc.</p>
                    <div class="flex items-center justify-between">

                    </div>
                </div>
            </div>
            <div class="mt-8">
                <h2 class="text-lg font-semibold mb-2">Nueva Publicación</h2>
                <form>
                    <div class="mb-2">
                        <label for="titulo" class="block text-gray-700 font-bold mb-1">Título</label>
                        <input type="text" id="titulo" name="titulo"
                            class="w-full px-3 py-2 rounded-lg border focus:outline-none focus:border-blue-500"
                            required>
                    </div>
                    <div class="mb-2">
                        <label for="contenido" class="block text-gray-700 font-bold mb-1">Contenido</label>
                        <textarea id="contenido" name="contenido" rows="4"
                            class="w-full px-3 py-2 rounded-lg border focus:outline-none focus:border-blue-500"
                            required></textarea>
                    </div>
                    <div>
                        <button type="submit"
                            class="bg-green-500 text-white px-4 py-2 rounded-lg hover:bg-green-600">Publicar</button>
                    </div>
                </form>
            </div>
        </div>
    </body>
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