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
import Header from './components/Header.vue'
import Homepage from './components/Homepage.vue'
import Test from './components/Test.vue'
import Promo from './components/Promo.vue'
import ListCategory from './components/ListCategory.vue'
import ListAlbum from './components/ListAlbum.vue'
import Footer from './components/Footer.vue'
import AlbumDetail from './components/AlbumDetail.vue'
import ListAlbumAchat from './components/ListAlbumAchat.vue'
import Panier from './components/Panier.vue'
import StepProgress from './components/StepProgress.vue'
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
