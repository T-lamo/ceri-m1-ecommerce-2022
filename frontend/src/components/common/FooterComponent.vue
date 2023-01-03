<script setup lang="ts"></script>

<template>
  <div class="container">
    <footer>
      <p>
        <a href="/contact"> Nous contacter </a>
      </p>
      <p>Tel: 0749286021</p>
      <p>Copyright © 2021 constellation, Inc.</p>
    </footer>
  </div>
</template>

<style lang="scss" scoped>
footer {
  padding: 3rem 1rem;
  background-color: var(--primary-2);
  font-size: 1.2rem;
  color: white;
  text-align: center;
}

footer p {
  margin-bottom: 0;
}

footer a {
  cursor: pointer;
  text-decoration: underline;
}
</style>
