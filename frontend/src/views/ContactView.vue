<template>
    <div>
        <NavbarComponent />
        <div class="container mx-auto px-4 py-8">
            <h1 class="text-3xl font-bold text-center mb-8 text-green-600">Contacte con Train Track</h1>
            <div class="max-w-md mx-auto bg-white p-8 rounded-lg shadow-md">
                <form>
                    <div class="mb-4">
                        <label for="nombre" class="block text-gray-700 font-semibold mb-2">Nombre</label>
                        <input type="text" id="nombre" name="nombre" class="w-full px-3 py-2 border rounded-lg
                            focus:outline-none focus:border-blue-500" placeholder="Tu nombre" required>
                    </div>
                    <div class="mb-4">
                        <label for="email" class="block text-gray-700 font-semibold mb-2">Correo electrónico</label>
                        <input type="email" id="email" name="email" class="w-full px-3 py-2 border rounded-lg
                            focus:outline-none focus:border-blue-500" placeholder="example@example.com" required>
                    </div>
                    <div class="mb-4">
                        <label for="mensaje" class="block text-gray-700 font-semibold mb-2">Mensaje</label>
                        <textarea id="mensaje" name="mensaje" class="w-full px-3 py-2 border rounded-lg
                            focus:outline-none focus:border-blue-500" rows="5" placeholder="Escribe tu mensaje aquí"
                            required></textarea>
                    </div>
                    <div class="flex justify-center">
                        <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600
                            focus:outline-none focus:bg-green-600">Enviar</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

</template>
<script setup>
import NavbarComponent from '@/components/layouts/NavbarComponent.vue';

</script>