<template>
  <div class="fixed top-0 left-0 flex items-center justify-center w-full h-full bg-black bg-opacity-50">
    <div class="max-w-lg mx-auto bg-white rounded-lg shadow-lg overflow-hidden z-10 p-6">
      <form>
        <div class="border-b border-main-green pb-12">
          <h1 class="text-base font-semibold leading-7 text-main-green">Añadir jugador</h1>
          <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
            <div class="sm:col-span-3">
              <label for="first-name" class="block text-sm font-medium leading-6 text-gray-900">Nombre</label>
              <div class="mt-2">
                <input type="text" name="first-name" id="first-name"
                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
              </div>
            </div>

            <div class="sm:col-span-3">
              <label for="last-name" class="block text-sm font-medium leading-6 text-gray-900">Last name</label>
              <div class="mt-2">
                <input type="text" name="last-name" id="last-name"
                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
              </div>
            </div>
            <div class="sm:col-span-3">
              <label for="country" class="block text-sm font-medium leading-6 text-gray-900">Padre/Madre</label>
              <div class="mt-2">
                <select id="country" name="country"
                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                  <option readonly>Eliga el padre del jugador</option>
                  <option>Juan</option>
                  <option>Alberto</option>
                  <option>Pedro</option>
                </select>
              </div>
            </div>
            <div class="sm:col-span-3">
              <label for="country" class="block text-sm font-medium leading-6 text-gray-900">Fecha de nacimiento</label>
              <div class="mt-2">
                <input type="date" id="country"
                  class="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm">
              </div>
            </div>

            <div class="sm:col-span-2">
              <label for="position" class="block text-sm font-medium leading-6 text-gray-900">Posición</label>
              <div class="mt-2">
                <select id="position" name="position"
                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                  <option readonly>Posición</option>
                  <option>Portero</option>
                  <option>Defensa</option>
                  <option>Centrocampista</option>
                  <option>Delantero</option>
                </select>
              </div>
            </div>
          </div>
        </div>
        <div class="flex items-center justify-center pt-6">
          <input type="submit" value="Entrar"
            class="bg-green-700 hover:bg-green-900 text-white font-bold py-2 px-4 rounded-full mr-4" />
          <router-link to="/trainer"
            class="bg-white-500 hover:bg-green-200 text-green-700 font-bold py-2 px-4 rounded-full">Volver</router-link>
        </div>
      </form>
    </div>
  </div>


</template>