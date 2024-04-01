<template>
  <div
    class="flex bg-white shadow-md justify-start md:justify-center rounded-lg  mx-auto py-4 px-2 md:mx-12">
    <template v-for="(activity, index) in activities" :key="index">
      <div class="flex flex-col items-center justify-center w-16 mx-1">
        <p class="text-green-600 text-sm transition-all duration-300">{{ weekDays[index] }}
        </p>
        <p class="text-gray-900 mt-1 group-hover:font-bold transition-all duration-300 text-xs">
          {{ activity }}</p>
      </div>
    </template>
  </div>
</template>

<script setup>
const weekDays = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom'];
const activities = ['x', 'Entrenamiento', 'x', 'x', 'Entrenamiento', 'Partido', 'x'];
</script>
