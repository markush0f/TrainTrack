<template>
    <div class="flex justify-center pb-2">
        <img :src="pathShield" :alt="pathShield">
    </div>
</template>
<script setup>

import { ref } from 'vue';
import pathShieldImg from '../../img/Shields/UD_Las_Zocas.png';

const pathShield = ref(pathShieldImg);

</script>