<script lang="ts"></script>

<template>
  <div class="container">
    <ul class="container">
      <li>
        <Cart product="{item}" />
      </li>
    </ul>
    <h1>Total: 0$</h1>
  </div>
</template>

<style lang="scss">
ul {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px 1fr));
  gap: 1rem;
  li:hover {
    background: var(--gray-2);
  }
}
</style>
