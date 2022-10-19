<script lang="ts">
 import { MDBFooter, MDBContainer, MDBRow, MDBCol, MDBBtn, MDBIcon } from 'mdb-vue-ui-kit';

export default {
  components: {
    MDBFooter,
    MDBContainer,
    MDBRow,
    MDBCol,
    MDBBtn,
    MDBIcon
  },
};
</script>

<template>
    <MDBFooter bg="dark" :text="['center', 'white']">
    <!-- Grid container -->
    <MDBContainer class="p-4 pb-0">
      <!-- Section: Social media -->
      <section class="mb-4">
        <!-- Facebook -->
        <MDBBtn
          tag="a"
          outline="light"
          href="#!"
          floating
          class="m-1"
        >
          <MDBIcon iconStyle="fab" icon="facebook-f"></MDBIcon>
        </MDBBtn>
        <!-- Twitter -->
        <MDBBtn
          tag="a"
          outline="light"
          href="#!"
          floating
          class="m-1"
        >
          <MDBIcon iconStyle="fab" icon="twitter"></MDBIcon>
        </MDBBtn>
        <!-- Google -->
        <MDBBtn
          tag="a"
          outline="light"
          href="#!"
          floating
          class="m-1"
        >
          <MDBIcon iconStyle="fab" icon="google"></MDBIcon>
        </MDBBtn>
        <!-- Instagram -->
        <MDBBtn
          tag="a"
          outline="light"
          href="#!"
          floating
          class="m-1"
        >
          <MDBIcon iconStyle="fab" icon="instagram"></MDBIcon>
        </MDBBtn>
        <!-- Linkedin -->
        <MDBBtn
          tag="a"
          outline="light"
          href="#!"
          floating
          class="m-1"
        >
          <MDBIcon iconStyle="fab" icon="linkedin-in"></MDBIcon>
        </MDBBtn>
        <!-- Github -->
        <MDBBtn
          tag="a"
          outline="light"
          href="#!"
          floating
          class="m-1"
        >
          <MDBIcon iconStyle="fab" icon="github"></MDBIcon>
        </MDBBtn>
      </section>
      <!-- Section: Social media -->
    </MDBContainer>
    <!-- Grid container -->
    <!-- Copyright -->
    <div
      class="text-center p-3"
      style="background-color: rgba(0, 0, 0, 0.2)"
    >
      © 2022 Copyright:
      <a class="text-white" href="#"
        >faramos.com</a
      >
    </div>
    <!-- Copyright -->
  </MDBFooter>
</template>

