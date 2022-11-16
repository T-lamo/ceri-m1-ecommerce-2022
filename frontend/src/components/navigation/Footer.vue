<script lang="ts" setup>

</script>
<template>
  <footer class="my-footer">
    <!-- start div input send email -->
        
    <!-- end div input email-->
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <div class="about">
            <!-- <img src="https://cdn.pixabay.com/photo/2015/05/28/14/38/ux-787980_960_720.jpg" class="img-responsive center-block" alt=""/> -->
            <p>Footer example </p>
            <!-- social media icons-->
            <div class="social-media">
              <ul class="row list-inline">
                <li>
                  <a href="#"><font-awesome-icon icon="fa-brands fa-facebook" size="lg" :style="{ color: 'white' }"/></a>
                </li>
                <li>
                  <a href="#"><font-awesome-icon icon="fa-brands fa-twitter" size="lg" :style="{ color: 'white' }"/></a>
                </li>
                <li>
                  <a href="#"><font-awesome-icon icon="fa-brands fa-google" size="lg" :style="{ color: 'white' }"/></a>
                </li>
                <li>
                  <a href="#"><font-awesome-icon icon="fa-brands fa-linkedin" size="lg" :style="{ color: 'white' }"/></a>
                </li>
              </ul>
            </div> <!-- end div social media -->
          </div> <!-- end div about -->
        </div> <!-- end div col sm 12-->

        <!-- help center div-->
        <div class="col-md-3 col-sm-6">
          <div class="footer-info">
            <h2 class="title" style="color:#2f3640;">Help Center</h2>
            <ul class="list-unstyled">
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
            </ul>
          </div>
      </div>
      <!-- end help center div-->

      <!-- security and privacy -->
      <div class="col-md-3 col-sm-6">
          <div class="footer-info">
            <h2 class="title">Security and privacy</h2>
            <ul class="list-unstyled">
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
            </ul>
          </div>
      </div>
      <!-- end div security and privacy-->
      <!-- start div customer information -->
      <div class="col-md-3 col-sm-6">
          <div class="footer-info">
            <h2 class="title">Customer information</h2>
            <ul class="list-unstyled">
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
            </ul>
          </div>
      </div>
      <!-- end div customer information-->

      <!-- start div another section-->
      <div class="col-md-3 col-sm-6">
          <div class="footer-info">
            <h2 class="title" style="color:#2f3640;">another section</h2>
            <ul class="list-unstyled">
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
              <li>
                <a href="#">
                  <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'white' }"/>
                  How to Pay
                </a>
              </li>
            </ul>
          </div>
      </div>
      <!-- end div another section -->

      </div>
    </div>

    <!-- start div copyright -->
    <section class="copyright">
      <div class="container">

        <div class="row">
          <p class="text-center text-white">Copyright 2022 Music Company</p>
        </div>
      </div>
    </section>
    <!-- end div copyright -->
</footer>
</template>
<style scoped>
* {
  background-color: #131312;
}
footer.my-footer {
background: #131312;;
border-top: 3px solid #b78c33; }
footer.my-footer .about {
margin: 0 auto;
margin-top: 40px;
max-width: 1170px;
text-align: center; }
footer.my-footer .about p {
font-size: 13px;
color: #999;
margin-top: 30px; }
footer.my-footer .about .social-media {
margin-top: 15px; }
footer.my-footer .about .social-media ul li a {
display: inline-block;
width: 45px;
height: 45px;
line-height: 45px;
border-radius: 50%;
font-size: 16px;
color: #b78c33;
border: 1px solid rgba(255, 255, 255, 0.3); }
footer.my-footer .about .social-media ul li a:hover {
background: #b78c33;
color: #fff;
border-color: #b78c33; }
footer.my-footer .footer-info {
margin-top: 30px; }
footer.nb-footer .footer-info .title {
/* color: #aaa; */
color: #b78c33;
text-transform: uppercase;
font-size: 16px;
border-left: 4px solid #b78c33;
padding-left: 5px; }
footer.my-footer .footer-info ul li a {
display: block;
color: #aaa;
padding: 2px 0; }
footer.my-footer .footer-info ul li a:hover {
color: #b78c33;
list-style: none;
list-style-type: none; }
footer.my-footer .footer-info p {
font-size: 13px;
line-height: 20px;
color: #aaa; }
footer.my-footer .copyright {
margin-top: 15px;
background: #111;
padding: 7px 0;
color: #999; }
footer.my-footer .copyright p {
margin: 0;
padding: 0; }
</style>