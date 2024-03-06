<template>
  <div v-if="!showCTV" class="card" style="width: 18rem;">
    <div class="card-body">
      <h5 class="card-title">Gestión del jugador</h5>
      <p class="card-text">Acceder a la gestión del jugador.</p>
      <RouterLink to="/login" class="card-link">Iniciar</RouterLink>
      <button class="card-link" @click="redirectToCheckCT">Registro</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import router from "@/router";
// CTV=codeteamviews
const showCTV = ref(false);
function redirectToCheckCT() {
  return router.push("/checkcodeteam")
}
</script>