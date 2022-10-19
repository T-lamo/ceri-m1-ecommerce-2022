<template>
  <!-- <HelloWorld msg="Thank you for using our product. We're glad you're with us."/> -->
  <Header/>
  <Homepage/>
  <Footer/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Header from './components/Header.vue'
import Homepage from './components/Homepage.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Header,
    Homepage,
    Footer,
  }
}
</script>

<style>
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
}
</style>
