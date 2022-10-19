<script lang="ts">
import { MDBBtn, MDBNavbar, MDBNavbarToggler, MDBNavbarNav, MDBNavbarItem } from 'mdb-vue-ui-kit';

export default {
  components: {
    MDBBtn,
    MDBNavbar,
    MDBNavbarToggler,
    MDBNavbarNav,
    MDBNavbarItem
  },
};
// import { defineComponent } from 'vue'
// import { ref } from 'vue'

// const activeIndex = ref('1')
// const handleSelect = (key: string, keyPath: string[]) => {
//   console.log(key, keyPath)
// }
// export default defineComponent({
//     name : "header_vue",
//     data() {
//         return {
//             // example
//             count: 1
//         }
//     }

// })
</script>

<template>
  <header>
    <!-- Navbar -->
    <MDBNavbar expand="lg" light bg="white" container position="sticky">
      <MDBNavbarToggler target="#navbarExample01"></MDBNavbarToggler>
      <MDBNavbarNav collapse="navbarExample01" class="mb-2 mb-lg-0">
        <MDBNavbarItem to="#" active>
          Home
        </MDBNavbarItem>
        <MDBNavbarItem to="#">
          Features
        </MDBNavbarItem>
        <MDBNavbarItem to="#">
          Pricing
        </MDBNavbarItem>
        <MDBNavbarItem to="#">
          About
        </MDBNavbarItem>
      </MDBNavbarNav>
    </MDBNavbar>
    <!-- Navbar -->
    </header>
</template>
