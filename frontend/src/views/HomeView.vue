<template>
  <HomePage />
</template>

<script lang="ts">
import { defineComponent } from 'vue';

// Components
import HomePage from '../components/Homepage.vue';

export default defineComponent({
  name: 'HomeView',

  components: {
    HomePage,
  },
});
</script>
