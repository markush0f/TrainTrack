<template>
  <main
    class="grid min-h-full place-items-center bg-white px-6 py-24 sm:py-32 lg:px-8"
  >
    <div class="text-center">
      <p class="text-base font-bold text-main-green sm:text-5xl">Ha sido registrado</p>
      <h1
        class="mt-4 text-3xl font-bold tracking-tight text-gray-900 sm:text-5xl"
      >
        Debe esperar a que el entrenador solicitado acepte su solicitud de registro para acceder 
        a las funciones de Train Track.
        <br>
        Cuando el entrenador acepte su solicitud le llegará un correo electrónico
      </h1>
      <p class="mt-6 text-base leading-7 text-gray-600"></p>
      <div class="mt-10 flex items-center justify-center gap-x-6">
        <router-link
          to="/"
          class="rounded-md bg-main-green px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-green-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >VOLVER</router-link
        >
      </div>
    </div>
  </main>
</template>
