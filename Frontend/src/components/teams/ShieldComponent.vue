<template>
    <img :src="pathShield" :alt="pathShield">
</template>
<script setup>
import { useProfileStore } from '@/stores/profile';
import { onMounted, ref } from 'vue';

// const pathShield = ref('')
// const shields = ref([
//     { name: 'UD_Las_Zocas', path: ('../../img/Shields/UD_Las_Zocas.png') },
//     { name: 'CD_Atalaya', path: ('../../img/Shields/CD_Atalaya.png') },
//     // Agrega más objetos para cada imagen que quieras mostrar
// ]);
// function loadShield() {
//     shields.value.forEach(shield => {
//         console.log(shield);
//         console.log(useProfileStore().data.team);
//         if (shield.name === useProfileStore().data.team) {
//             console.log('si funciona');
//             pathShield.value = `../../img/Shields/UD_Las_Zocas.png`;

//         }
//     });
// }
// onMounted(() => {
//     loadShield()
// })




import pathShieldImg from '../../img/Shields/UD_Las_Zocas.png';

const pathShield = ref(pathShieldImg);

</script>