<script setup>
import { defineProps, ref, computed } from 'vue'
const props = defineProps({
    data: Object,
});
console.log(props.data)
props.data.currentStep--;
const data = ref(props.data);

const cssStyle = computed(() => {
    return {
        '--active-color': data.value.activeColor,
        '--passive-color': data.value.passiveColor,
    }
})
</script>
<template>
    <div class="steps-container" :style="cssStyle">
        <ul class="steps-list">
            <li class="step" v-for="(step,index) in data.steps" :key="index" :class="(index == data.currentStep) ? 'step-active':''">
                <div class="step-bubble"></div>
                <div class="step-line example">
                    <div class="line-fill"></div>
                </div>
            </li>
        </ul>
    </div>
</template>
<style scoped>
.steps-container{
    width: 95%;
    margin: 0 auto;
}
.steps-list {
    display: flex;
    list-style: none;
}
.step {
    display: flex;
    align-items: center;
    flex-grow: 1;
    max-width: 100%;
    position: relative;
    height: 60px;
}
.step:last-child {
    max-width: 60px;

}
.step-bubble {
    width: 35px;
    height: 35px;
    border-radius: 50%;
    background-color: var(--passive-color);
    transition: all .3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
}
.step-line{
    width: 100%;
    height: 5px;
    background-color: var(--passive-color)
    top
    50%;
    left: 0;
    transform: translateY(-50%);
}
.steep-active .step-bubble {

}
</style>