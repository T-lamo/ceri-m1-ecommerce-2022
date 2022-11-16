<template>
  <!-- <HelloWorld msg="Thank you for using our product. We're glad you're with us."/> -->
  <!-- <Header/> -->
  <Test/>
  <router-view></router-view>
  <Footer/>
   <!-- <Homepage/> -->
  <!-- <Footer/> -->
</template>

<script>
import Header from './components/navigation/Header.vue'
import Homepage from './components/Homepage.vue'
import Test from './components/navigation/Test.vue'
import Promo from './components/navigation/Promo.vue'
import ListCategory from './components/category/ListCategory.vue'
import ListAlbum from './components/album/ListAlbum.vue'
import Footer from './components/navigation/Footer.vue'
import AlbumDetail from './components/album/AlbumDetail.vue'
import ListAlbumAchat from './components/album/ListAlbumAchat.vue'
import Panier from './components/panier/Panier.vue'
import StepProgress from './components/StepProgress.vue'
import HelloWorld from './components/HelloWorld.vue'
import OneAlbumDetail from './components/album/OneAlbumDetail.vue'
import OneArtistDetail from './components/artist/OneArtistDetail.vue'
export default {
  name: 'App',
  components: {
    Header,
    Homepage,
    Footer,
    Test,
    Promo,
    ListCategory,
    ListAlbum,
    Footer,
    AlbumDetail,
    ListAlbumAchat,
    Panier,
    StepProgress,
    HelloWorld,
    OneAlbumDetail,
    OneArtistDetail,
  }
}
</script>

<style>
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
 
}
/* body {
  background-color: #2f3640;
} */
</style>
