

<template>
<NavBar/>
<div class="flex">
  <div id="clasification" class="w-1/3 p-4 border border-gray-400 flex-grow min-h-screen flex-basis-0"><Clasification/></div>
  <div id="noticias" class="w-1/3 flex justify-center p-4 border border-gray-400">
    <img src=C:\laragon\www\TrainTrack\data\img\noticiaEjemplo.jpg alt="Noticias" class="flex">
  </div>
  <div id="federation" class="w-1/3 flex justify-center p-4 pr-10 border border-gray-400">
    <img src=C:\laragon\www\TrainTrack\data\img\federacionEjemplo.png alt="Federacion" class="flex">
  </div>
</div>
</template>


<script setup>
  import NavBar from '../components/layouts/NavbarComponent.vue'
  import Clasification from '../components/Clasificacion.vue'
</script>

<style>

</style>

