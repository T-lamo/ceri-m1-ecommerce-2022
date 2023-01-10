<script lang="ts" setup>
import SearchAlbumList from "./SearchAlbumList.vue";
</script>

<template>
  <div class="search-component">
    <SearchAlbumList />
  </div>
</template>
<style scoped>
.search-component {
  display: flex;
  justify-content: center;
  position: fixed;
  top: 100px;
  max-height: 400px;
  width: 100%;
 
}
</style>
