<script lang="ts" setup>

</script>
<template>
  <div class="container-fluid">
    <div class="b-example-divider"></div>
    <footer class="py-3"> <!---->
      <ul class="nav justify-content-center border-bottom">
        <li class="nav-item">
          <a href="#" class="nav-link px-2">
          <router-link to="/home" class="text-muted text-decoration-none">
            Home
          </router-link>
          </a>
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link px-2">
            <router-link to="/albums" class="text-muted text-decoration-none">
              Albums
            </router-link>
          </a>
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link px-2">
            <router-link to="/promo" class="text-muted text-decoration-none">
              Promo
            </router-link>
          </a>
        </li>
        <li class="nav-item">
          <a href="#" class="nav-link px-2 text-muted">Contact</a></li>
        <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">About</a></li>
      </ul>
      <p class="text-center text-muted">&copy; 2022 Vinyl Company, Inc</p>
    </footer>
  </div>
</template>
<style scoped>
* {
  background-color: #131312;
  margin-top: 10px;
  
}
footer {
  display: block;
  width: 100%;
  bottom: 0;
}
</style>