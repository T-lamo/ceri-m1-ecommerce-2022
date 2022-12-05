<script lang="ts" setup>
import ListAlbum from './album/ListAlbum.vue';
import ListCategory from './category/ListCategory.vue';
import ListArtist from './artist/ListArtist.vue';
import HelloWorld from './HelloWorld.vue';
import Promo from './promo/Promo.vue';


</script>

<template>
  <div class="py-2 px-2">
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
</template>
<style scoped>

</style>