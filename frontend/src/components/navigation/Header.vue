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
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand px-2" href="#">
      Logo
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">
            <router-link to="/" style="color:#bdc3c7;text-decoration: none;">Home</router-link>
          </a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Liste
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li>
              <a class="dropdown-item" href="#"><router-link to="/artists" style="color:black;text-decoration: none;">Artistes</router-link></a>
          </li>
            <li>
              <a class="dropdown-item" href="#"><router-link to="/albums" style="color:black;text-decoration: none;">Albums</router-link></a>
            </li>
            <li><hr class="dropdown-divider"></li>
            <li>
              <a class="dropdown-item" href="#"><router-link to="/promos" style="color:black;text-decoration: none;">Promo</router-link></a>
            </li>
          </ul>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-warning me-4" type="submit">Search</button>
      </form>
      <div class=".col-4 icon_header me-4 py-2 my-2">
        <!-- Link  to shop -->
        <a href="#">
          <router-link to="/panier" class="router_link_class">
            <font-awesome-icon icon="fa-solid fa-cart-shopping" size="2x" :style="{ color: 'white' }"/>
            <!-- <span class="position-absolute top-0 start-0 translate-middle badge rounded-pill bg-danger">
              99+
            <span class="visually-hidden">unread messages</span>
            </span> -->
          </router-link>
        </a>
      </div>
      <!-- compte -->
           <div class=".col-4 icon_header me-4 my-2">
            <ul class="navbar-nav me-auto mb-2">
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      <font-awesome-icon icon="fa-solid fa-user" size="2x" :style="{ color: 'white' }"/>
                  </a>
                  <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                    <li>
                      <a class="dropdown-item" href="#">Account</a>
                    </li>
                    <li>
                      <a class="dropdown-item" href="#">
                        <router-link to="/panier_step" class="router_link_class">Commandes</router-link>
                      </a>
                    </li>
                    <li><hr class="dropdown-divider"></li>
                    <li>
                      <a class="dropdown-item" href="#">Logout</a>
                    </li>
                  </ul>
              </li>
            </ul>
        </div>
    </div>
  </div>
</nav>
</template>
<style scoped>
* {
    margin: 0px 0px 0px 0px;
    /* background-color: #2f3640; */
}
.icon_header{
    margin-top: 5px;
}
.router_link_class {
  text-decoration: none;
  color: black;
}
</style>
