<script lang="ts" setup>
  import { useAppStore } from '@/stores';
  import { storeToRefs } from "pinia";
  import { onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { toast_function } from '@/services/crud';

  const router = useRouter()

  const { current_user , isLoggedIn, list_cart_item} = storeToRefs(useAppStore())

  const onLougout = (() => {
    setTimeout(() => {
      router.push({
        name: 'login',
        replace:true})
      isLoggedIn.value = false
    },1000)
    console.log('logged out')
    toast_function('You are logged out successfully!!','success')
  })
 
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
            <router-link to="/home" style="color:#bdc3c7;text-decoration: none;">Home</router-link>
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
          <router-link to="/panier" class="router_link_class" v-if="isLoggedIn">
            <font-awesome-icon icon="fa-solid fa-cart-shopping" size="2x" :style="{ color: 'white' }"/>
              <!-- <span>hello </span> -->
            <span class="badge rounded-pill bg-danger">
              {{ list_cart_item.length }}
            <!-- <span class="visually-hidden">unread messages</span> -->
            </span>
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
                    <li v-if='isLoggedIn' class='px-3 py-2'>Log in as:</li>
                    <li v-if='isLoggedIn'><hr class="dropdown-divider"></li>
                    <li v-if='isLoggedIn' class='px-3 py-2 fst-normal'>
                      {{current_user.username}} {{current_user.firstname}}
                    </li>
                    <li v-if='isLoggedIn' class='px-3 py-1 fst-normal'>
                      {{current_user.email}}
                    </li>
                  
                    <li><hr class="dropdown-divider"></li>
                    <li>
                      <a class="dropdown-item" href="#">Account</a>
                    </li>
                    <li>
                      <a class="dropdown-item" href="#">
                        <router-link to="/panier_step" class="router_link_class">Commands</router-link>
                      </a>
                    </li>
                    <li>
                      <a class="dropdown-item" href="#">
                        <router-link to="/" class="router_link_class">Wishing list</router-link>
                      </a>
                    </li>
                    <li v-if='isLoggedIn'><hr class="dropdown-divider"></li>
                    <li v-if="isLoggedIn">
                      <a class="dropdown-item" href="#">
                        <div class="d-grid gap-2">
                          <button class="btn btn-danger" @click="onLougout">Logout</button>
                        </div>
                      </a>
                    </li>
                    <li v-else>
                      <a class="dropdown-item" href="#">
                        <div class="d-grid gap-2">
                          <router-link to="/" style="text-decoration:none ;">Sign In </router-link>
                        </div>
                      </a>
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
