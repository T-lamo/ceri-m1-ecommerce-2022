<script lang="ts" setup>
  import ListAlbum from './album/ListAlbum.vue';
  import ListCategory from './category/ListCategory.vue';
  import ListArtist from './artist/ListArtist.vue';
  import Promo from './promo/Promo.vue';
  import { storeToRefs } from 'pinia';
  import { useAppStore } from '@/stores';
  import Dashboard from './admin/Dashboard.vue';
  const { current_user } = storeToRefs(useAppStore())

</script>

<template>
  <div class="py-2 px-2" v-if="current_user?.is_admin == false">
    <button class="btn btn-primary">Albums</button> &nbsp;&nbsp;
    <button class="btn btn-secondary">Artists</button> &nbsp;&nbsp;
    <button class="btn btn-warning">
      <router-link to="/promo"> Promos</router-link>
    </button>
    <!-- <HelloWorld/> -->
    <Promo/>
    <ListCategory/>
    <ListAlbum/> 
    <ListArtist/>
    <!-- <Footer/>   -->
  </div> 
  <div class="py-2 px-2">
    <!-- Admin menu dashboard -->
    <!-- <Dashboard
      /> -->
  </div>
</template>
<style scoped>

</style>