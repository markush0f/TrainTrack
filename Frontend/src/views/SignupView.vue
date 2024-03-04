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
          required
        />
      </div>

      <label for="inputSurName" class="col-sm-2 col-form-label">Surname</label>
      <div class="col-sm-6 mb-2">
        <input
          type="text"
          name="surname"
          class="form-control"
          id="inputSurName"
          data-bs-theme="dark"
          required
        />
      </div>

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
          class="form-control"
          id="inputPassword"
          data-bs-theme="dark"
          required
          />
      </div>

      <label for="inputDate" class="col-sm-2 col-form-label">BirthDay</label>
      <div class="col-sm-6 mb-2">
        <input
          type="date"
          name="date"
          class="form-control"
          id="inputDate"
          data-bs-theme="dark"
          required
        />
      </div>

      <lable for="inputPhone" class="col-sm-2  col-form-label">Phone</lable>
      <div class="col-sm-6 mb-2">
        <input
          type="number"
          name="phone"
          class="form-control"
          id="inputPhone"
          data-bs-theme="dark"
          required
          />
      </div>

      <lable for="inputAdress1" class="col-sm-2  col-form-label">Adress 1</lable>
      <div class="col-sm-6 mb-2">
        <input
          type="text"
          name="Adress1"
          class="form-control"
          id="inputAdress1"
          data-bs-theme="dark"
          required
          />
      </div>

      <lable for="inputAdress2" class="col-sm-2  col-form-label">Adress 2</lable>
      <div class="col-sm-6 mb-2">
        <input
          type="text"
          name="Adress2"
          class="form-control"
          id="inputAdress2"
          data-bs-theme="dark"
          />
      </div>
      
      <input type="submit" value="Enviar" class="btn btn-primary" />
    </form>
  </div>
</template>
<script setup>

</script>
<style lang="css"></style>
