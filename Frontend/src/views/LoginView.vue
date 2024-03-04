<template lang="">
  <div>
    <h1>Pagina de login</h1>
    <form action="" method="post">
      <lable for="inputEmail" class="col-sm-2  col-form-label">Email</lable>
      <div class="col-sm-6 mb-2">
        <input
          type="email"
          name="email"
          class="form-control"
          id="inputEmail"
          data-bs-theme="dark"
          required
          />
      </div>

    <label for="inputPassword" class="col-sm-2 col-form-label">Password</label>
      <div class="col-sm-6 mb-3">
        <input
          type="password"
          name="password"
          minlength="8"
          maxlength="30"          
          class="form-control"
          id="inputPassword"
          data-bs-theme="dark" 
          required
        />
      </div>
      <input type="submit" value="Entrar" class="btn btn-primary" />
    </form>
  </div>
</template>
<script setup>

</script>
<style lang="">
  
</style>