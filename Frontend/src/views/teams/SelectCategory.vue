<template>
  <div class="inline-flex rounded-md " role="group">
    <div class="group-btn">
      <input type="button" value="Prebenjamin"
        class="group-btn-item px-4 py-2 text-sm font-medium text-gray-900 bg-white border rounded-l-lg hover:text-main-green focus:text-main-green"
        :class="{ 'text-main-green border-2 border-main-green': selectedButton === 'prebenjamin' }"
        @click="selectButton('prebenjamin')">
      <input type="button" value="Benjamin"
        class="group-btn-item px-4 py-2 text-sm font-medium text-gray-900 bg-white border hover:text-main-green focus:text-main-green"
        :class="{ 'text-main-green border-2 border-main-green': selectedButton === 'benjamin' }"
        @click="selectButton('benjamin')">
      <input type="button" value="Alevin"
        class="group-btn-item px-4 py-2 text-sm font-medium text-gray-900 bg-white border hover:text-main-green focus:text-main-green"
        :class="{ 'text-main-green border-2 border-main-green': selectedButton === 'alevin' }"
        @click="selectButton('alevin')">

      <input type="button" value="Infantil"
        class="group-btn-item px-4 py-2 text-sm font-medium text-gray-900 bg-white border rounded-r-lg hover:text-main-green focus:text-main-green"
        :class="{ 'text-main-green border-2 border-main-green': selectedButton === 'infantil' }"
        @click="selectButton('infantil')">
    </div>
  </div>


</template>

<script setup>
import { useCategoryStore } from '@/stores/category.js';
import {ref, onMounted} from 'vue'
const selectedButton = ref('');
const categoryStore = useCategoryStore();

onMounted(() => {
  selectedButton.value = categoryStore.getCategory();
});

const selectButton = (button) => {
  selectedButton.value = button;
  categoryStore.setCategory(button)
}
</script>