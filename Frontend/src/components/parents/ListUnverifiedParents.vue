<template>
  <div>
    <p>Lista de peticiones</p>
    Actualizar ista de padres al añadir un hijo
    <div class="flex p-4" v-if="unverifiedParents != null">
      <div class="justify-center w-full">
        <!-- Con el max-h-60 ajustamos el scroll -->
        <div class="w-full overflow-y-auto max-h-60">
          <!-- Iterar sobre los padres y mostrarlos en una columna -->
          <div
            v-for="parent in unverifiedParents"
            :key="parent.id"
            class="w-full mb-4"
          >
            <div
              class="bg-gray-50 rounded-lg shadow-lg hover:shadow-xl transition duration-300 border border-green-300"
            >
              <h2 class="text-sm font-semibold p-2">
                {{ parent.name }} {{ parent.surname }} (DNI: {{ parent.DNI }})
              </h2>
              <h3 class="text-xs pl-2"></h3>
              <div class="pt-1 flex justify-center space-x-2 p-2">
                <button
                  @click="manageRequest(true, parent.id)"
                  class="px-3 py-1.5 font-medium bg-green-200 hover:bg-green-300 hover:text-green-600 text-green-500 rounded-lg text-xs"
                >
                  Aceptar
                </button>
                <button
                  @click="manageRequest(false, parent.id)"
                  class="px-3 py-1.5 font-medium bg-red-200 hover:bg-red-300 hover:text-red-600 text-red-500 rounded-lg text-xs"
                >
                  Rechazar
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <p>No hay ninguna solicitud pendiente</p>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { getUnverifiedParents } from "@/services/parentsAPI";
import { manageRequestParent } from "@/services/userAPI";
import { useParentStore } from "@/stores/parents";
const parentStore = useParentStore();
const unverifiedParents = ref([]);

onMounted(async () => {
  unverifiedParents.value = await getUnverifiedParents();
  console.log(unverifiedParents.value);
});

async function manageRequest(decision, parentId) {
  if (decision) {
    console.log("Aprobado", parentId);
  } else {
    console.log("Denegado", parentId);
  }

  await manageRequestParent(decision, parentId);
  removeParent(parentId);
}

function removeParent(parentId) {
  unverifiedParents.value = unverifiedParents.value.filter(
    (parent) => parent.id !== parentId
  );
}
</script>
