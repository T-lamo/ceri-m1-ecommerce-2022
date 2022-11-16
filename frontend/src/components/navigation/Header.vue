<script lang="ts">
export default {
  data() {
    return {
      titleClass: 'title'
    }
  }
}
</script>

<template>
  <header>
    <div class="header">
      <!-- <div class="div-logo"> -->
        <a href="#default" class="logo">
        CompanyLogo
      </a>
      <!-- </div> -->
      
      <!-- <div class="search-container"> -->
          
          <!-- <button>
            Search
          </button> -->
      <!-- </div> -->
      <div class="header-right">
        <!-- Search box -->
        <input type="text" name="search" placeholder="Search......" class="search-input">
          <button href="#" class="search-btn" >
              <font-awesome-icon icon="fa-solid fa-magnifying-glass fa-7x"/>
          </button>
        &nbsp;&nbsp;
        <!-- Contact now -->
        <a href="#">
          <font-awesome-icon icon="fa-solid fa-comment-sms" size="lg" :style="{ color: 'white' }" />
        </a>
        &nbsp;&nbsp;
        <!-- Link  to shop -->
        <a href="#">
          <font-awesome-icon icon="fa-solid fa-cart-shopping" size="lg" :style="{ color: 'white' }"/>
        </a>
        <!-- Link for user  -->
        &nbsp;&nbsp;
        <a href="#">
          <font-awesome-icon icon="fa-solid fa-user" size="lg" :style="{ color: 'white' }"/>
        </a>
      
    </div>
  </div>
  </header>
</template>
<style scoped>
.header {
  width: 100%;
  overflow: hidden;
  background-color: #131312;
  padding: 20px 10px;
  /* display: flex; */
  flex-direction: row;
  /* display:flex; */
  /* justify-content: flex-start; */
}
/* style of header links */
.header a {
  color: #fff;
  margin: 0 10px;
  font-size: 16px;
  font-weight: 500;
  text-decoration: none;
  /* color: #414141; */
  /* display: inline-block; */
  /* float: left; */
  /* position: relative; */
  display: block;
  float: left;
}
.header-right {
  display: block;
  float: right;
  margin-right: 20px;
  /* text-align: end; */
  /* float: right; */
  /* display: inline-block; */
  /* word-spacing: 20px; */
}
.header-right input[type=text] {
  float: right;
  padding: 6px;
  border: none;
  margin-top: 8px;
  margin-right: 16px;
  font-size: 17px;
}
.header-right button {
  float: right;
  padding: 6px 10px;
  margin-top: 8px;
  margin-right: 16px;
  background: #ddd;
  font-size: 17px;
  border: none;
  cursor: pointer;
}
.search-container button {
  border-radius: 10px;
  background-color:black;
  color: #fff;
}


/* uncomment for shaking search box */
/* @keyframes hoverShake {
  0% {transform: skew(0deg,0deg);}
  25% {transform: skew(5deg, 5deg);}
  75% {transform: skew(-5deg, -5deg);}
  100% {transform: skew(0deg,0deg);}
} */

.search-input:hover{
  animation: hoverShake 0.15s linear 3;
} 
</style>