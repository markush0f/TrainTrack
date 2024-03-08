<template>
<div class=""> 
  <div class="justify-center text-4xl">
    Clasificacion
  </div>
    <div class="">
Categorias: 
<div class="flex flex-grap">
 <div class="">
   <select class="block appearance-none w-full bg-white border border-gray-400 hover:border-gray-500 px-4 py-2 pr-8 rounded shadow leading-tight focus:outline-none focus:shadow-outline">
      <option value="" disabled selected>Selecciona una categoría</option>
      <option value="prebenjamin">Prebenjamin</option>
      <option value="benjamin">Benjamin</option>
      <option value="alevin">Alevin</option>
      <option value="infantil">Infantil</option>
    </select>
    <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700"></div>
  
 
<table class="table-auto">
  <thead class>
    <tr>
      <th class="px-4 py-2 bg-green-300 text-black ">Club</th>
      <th class="px-4 py-2 bg-green-300">PJ</th>
      <th class="px-4 py-2 bg-green-300">W</th>
      <th class="px-4 py-2 bg-green-300">D</th>
      <th class="px-4 py-2 bg-green-300">L</th>
      <th class="px-4 py-2 bg-green-300 ">PTS</th>
    </tr>
  </thead>
  <tbody>
    <tr class="hover:bg-gray-100">
      <td class="px-4 py-2">Equipo 1</td>
      <td class="px-4 py-2">10</td>
      <td class="px-4 py-2">7</td>
      <td class="px-4 py-2">2</td>
      <td class="px-4 py-2">1</td>
      <td class="px-4 py-2">23</td>
    </tr>
    <tr>
      <td class="px-4 py-2">Equipo 2</td>
      <td class="px-4 py-2">9</td>
      <td class="px-4 py-2">5</td>
      <td class="px-4 py-2">3</td>
      <td class="px-4 py-2">1</td>
      <td class="px-4 py-2">18</td>
    </tr>
    <!-- Añade más filas según sea necesario -->
  </tbody>
</table>
</div>
</div>
  </div>
</div>
</template>

<script>

</script>
