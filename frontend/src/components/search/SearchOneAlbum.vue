<script lang="ts" setup>
    const props = defineProps<{
        item: any
    }>()
</script>
<template>
    <div>
        <h2>{{props.item}}</h2>
    </div>
</template>