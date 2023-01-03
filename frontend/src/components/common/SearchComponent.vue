<script setup lang="ts"></script>

<template>
  <div class="container">
    <ul class="container">
      <a href="/product-details/{item.id}">
        <li>item</li>
      </a>
    </ul>
  </div>
</template>

<style lang="scss">
.container {
  width: 100%;
  max-height: 500px;
  background: var(--gray-1);
}
ul {
  display: flex;
  flex-direction: column;
  li:hover {
    background: var(--gray-2);
  }
  overflow-y: auto;
}
</style>
