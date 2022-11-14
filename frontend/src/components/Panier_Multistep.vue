<script lang="ts" setup>
    import { defineProps } from 'vue';
    import StepProgress from './StepProgress.vue'
    const dataSteps = {
        steps: ['Step 1','Step 3','Step 3'],
        currentStep: 1,
        activeColor:'#FD7272',
        passiveColor: '#ddd'
    }
</script>
<template>

    <StepProgress :data="dataSteps"/>
</template>
<style scoped>

</style>