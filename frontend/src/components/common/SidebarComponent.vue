<script setup lang="ts"></script>

<template>
  <div class="container">
    <ul>
      <a href="#">
        <li>item</li>
      </a>
    </ul>
  </div>
</template>

<style lang="scss" scoped>
.container {
  background: var(--gray-1);
  width: 300px;
  position: fixed;
  top: calc(70px);
  min-height: 100vh;
  font-size: large;
  font-weight: 700;
  ul {
    padding: 1rem;
    display: grid;
    grid-template-rows: repeat(auto-fit, 1fr);

    overflow-y: auto;
    padding: 0;

    li {
      padding: 1rem;
      background: var(--gray-1);
      color: var(--secondary-black);
      font-size: 2rem;
      border-bottom: 1px solid var(--gray-2);
      align-self: center;
    }
    li:hover {
      background: var(--gray-2);
      border-bottom: 2px solid var(--gray-3);
      cursor: pointer;
    }
  }
}

@media (max-width: 992px) {
  ul {
    width: 300px !important;
    overflow-y: auto;
  }
}
</style>
