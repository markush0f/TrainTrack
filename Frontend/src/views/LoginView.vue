<template lang="">
  <div>
    <h1 class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-black" >Pagina de login</h1>
    <form action="" method="post" class="bg-white px-8 pt-6 pb-8 mb-4">
      <div class =" mb-4 ">
        <div class="grid grid-flow-row sm:grid-flow-col gap-3">
          <div class="sm:col-span-4 justify-self-start">
            <label class="block text-black-700 text-sm font-bold mb-2" for="inputEmail">Email</label>
            <input class="shadow apperance-none border rounded w-full py-2 px-3 text-grey-700 leading-tight focus:outline-none focus:shadow-outline"  type="email" name="email" id="inputEmail" placeholder="Search your email" required></input>
          </div>
        </div>
      </div>
      <div class =" mb-4 ">
        <div class="grid grid-flow-row sm:grid-flow-col gap-3">
          <div class="sm:col-span-4 justify-self-start">
            <label class="block text-black-700 text-sm font-bold mb-2" for="inputPassword">Password</label>
            <input class="shadow apperance-none border rounded w-full py-2 px-3 text-grey-700 leading-tight focus:outline-none focus:shadow-outline"  type="password" name="password" id="inputPassword" placeholder="************" required></input>
          </div>
        </div>
      </div>
      <input type="submit" value="Entrar" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" />
    </form>
  </div>
</template>
<script setup>

</script>
<style lang="">
  
</style>