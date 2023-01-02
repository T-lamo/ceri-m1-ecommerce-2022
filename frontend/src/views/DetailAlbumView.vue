<template>
    <HomePage />
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue';
  
  // Components
  import AlbumDetail from '../components/AlbumDetail.vue';
  
  export default defineComponent({
    name: 'AlbumView',
  
    components: {
      AlbumDetail,
    },
  });
  </script>