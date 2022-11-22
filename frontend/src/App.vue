<template>
  <!-- <HelloWorld msg="Thank you for using our product. We're glad you're with us."/> -->
  <!-- <Header/> -->
  <Test/>
  <router-view></router-view>
  <!-- <Footer/> -->
   <!-- <Homepage/> -->
  <Footer/>
</template>

<script>
import Header from './components/navigation/Header.vue'
import Homepage from './components/Homepage.vue'
import Test from './components/navigation/Header.vue'
import Promo from './components/navigation/Promo.vue'
import ListCategory from './components/category/ListCategory.vue'
import ListAlbum from './components/album/ListAlbum.vue'
import Footer from './components/navigation/Footer.vue'
import AlbumDetail from './components/album/AlbumDetail.vue'
import ListAlbumAchat from './components/album/ListAlbumAchat.vue'
import HelloWorld from './components/HelloWorld.vue'
import OneAlbumDetail from './components/album/OneAlbumDetail.vue'
import OneArtistDetail from './components/artist/OneArtistDetail.vue'
import Authentification from './components/auth//Authentification.vue'
import Panier_Multistep from './components/panier/Panier_Multistep.vue'
import Liste_Commandes from './components/panier/Liste_Commandes.vue'
import Wizard from 'form-wizard-vue3'

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
    HelloWorld,
    OneAlbumDetail,
    OneArtistDetail,
    Authentification,
    Panier_Multistep,
    Liste_Commandes,
    Wizard,
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
