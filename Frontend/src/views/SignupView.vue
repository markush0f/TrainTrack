<template lang="">
  <div>
    <h1>Pagina de registro</h1>
    <form action="" method="post">
      <label for="inputName" class="col-sm-2 col-form-label">Name</label>
      <div class="col-sm-6 mb-2">
        <input
          type="text"
          name="name"
          class="form-control"
          id="inputName"
          data-bs-theme="dark"
        />
      </div>

      <label for="inputPassword" class="col-sm-2 col-form-label"
        >Password</label
      >
      <div class="col-sm-6 mb-3">
        <input
          type="password"
          name="password"
          class="form-control"
          id="inputPassword"
          data-bs-theme="dark"
        />
      </div>
      <input type="submit" value="Enviar" class="btn btn-primary" />
    </form>
  </div>
</template>
<script setup></script>
<style lang="css"></style>
