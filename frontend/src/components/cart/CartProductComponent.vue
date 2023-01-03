<script setup lang="ts">
import ListCartProduct from "./ListCartProductComponent.vue";
</script>

<template>
  <div class="container">
    <h2>Panier</h2>
    <ListCartProduct />
    <button class="btn btn-success">Commander</button>
    <button class="btn btn-primary">Modifier</button>
  </div>
</template>

<style lang="scss" scoped>
.container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>
