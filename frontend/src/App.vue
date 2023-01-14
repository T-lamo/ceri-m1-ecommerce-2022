<template>
  <!-- <HelloWorld msg="Thank you for using our product. We're glad you're with us."/> -->
  <Header />
  <!-- <Header
    /> -->
  <div class="content">
    <router-view></router-view>
  </div>
  <!-- <Footer/> -->
  <!-- <Homepage/> -->
  <!-- <Footer /> -->
</template>

<script lang="ts">
import Header from "./components/navigation/Header.vue";
import Homepage from "./components/Homepage.vue";
import ListCategory from "./components/category/ListCategory.vue";
import ListAlbum from "./components/album/ListAlbum.vue";
import Footer from "./components/navigation/Footer.vue";
import OneAlbumDetail from "./components/album/OneAlbumDetail.vue";
import OneArtistDetail from "./components/artist/OneArtistDetail.vue";
import Authentification from "./components/auth//Authentification.vue";
import Panier_Multistep from "./components/panier/Panier_Multistep.vue";
import Liste_Commandes from "./components/panier/Liste_Commandes.vue";
import Promo from "./components/promo/Promo.vue";

export default {
  name: "App",
  components: {
    Header,
    Homepage,
    Footer,
    ListCategory,
    ListAlbum,
    OneAlbumDetail,
    OneArtistDetail,
    Authentification,
    Panier_Multistep,
    Liste_Commandes,
    Promo,
  },
};
</script>

<style>
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
}
.content {
  min-height: 1000px;
}
</style>
