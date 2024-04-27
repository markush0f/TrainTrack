<template>
  <div>
    <NavbarComponent />
    <div class="sm:flex items-center max-w-screen-xl">
      <div class="sm:w-1/2 p-10">
        <div class="image object-center text-center">
          <img src="@/img/LogoTrainTrack.png" />
        </div>
      </div>
      <div class="sm:w-1/2 p-5">
        <div class="text">
          <span class="text-gray-500 border-b-2 border-green-600 uppercase"
            >Sobre nosotros</span
          >
          <h2 class="my-4 font-bold text-3xl sm:text-4xl">
            Sobre <span class="text-green-600">Train Track</span>
          </h2>
          <p class="text-gray-700">
            Somos una aplicacion creada por dos jovenes apacionados por el
            futbol y el desarrollo web, con esta aplicacion queremos darnos a
            conocer y sacar provecho de esta, y seguir creciendo y poder seguir
            avanzando con TrainTrack. En TrainTrack ofrecemos una gestion del
            entrenador con los jugadores, ademas de acceder a la informacion y
            estadisticas de los jugadores,publicar eventos y enviar mensajes
            para los padres registrados de los jovenes jugadores, además
            queremos que el ambiente entre los padres sea agradable y es por eso
            que cada equipo tendrá su propio foro. Con TrainTrack queremos
            lograr una aplicacion nacional y publica para todo el mundo, por
            ahora estaremos disponibles solo en las ISLAS CANARIAS, pero
            queremos expandirla a mas municipios! Es por eso que si te interesa
            nuestro negocio, no dude en contactar con nosotros, muchas gracias y disfruta de Train Track!
          </p>
          <br>
          <router-link to="/contact" class="text-green-600">PULSE AQUI PARA CONTACTAR CON NOSOTROS!!</router-link>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import NavbarComponent from "@/components/layouts/NavbarComponent.vue";
</script>
