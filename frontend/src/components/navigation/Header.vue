<script lang="ts" setup>
import { watch, watchEffect, ref } from "vue";
import { useAppStore } from "@/stores";
import { storeToRefs } from "pinia";
import { RouterLink, RouterView, useRouter } from "vue-router";
import { index_make_search, toast_function } from "@/services/crud";
import type { Album, User } from "@/models";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

  const router = useRouter()

const { list_cart_item, isAdminStore, searchItems } = storeToRefs(
  useAppStore()
);

// let isAdminStore = ref(Boolean(localStorage.getItem('isAdmin')));
let user_from_localstorage: string;
let user_obj = ref<User>();
let search_text = ref<String>("");
// watch(isAdminStore, () => {

  watch(isAdminStore, (newValue, oldValue) => {
    localStorage.setItem("isAdmin","false")
    console.log("watch isadminstore")
  })

    user_from_localstorage = localStorage.getItem("userId")!
    user_obj = JSON.parse(user_from_localstorage!)    
      
    const isLoggedIn_from_localstorage = Boolean(localStorage.getItem("isLoggedIn"))
  
  // let isAdminUser_from_localstorage = Boolean(localStorage.getItem("isAdmin"))

  const onLogout = (() => {
    isAdminStore.value = false
    localStorage.setItem("isLoggedIn","false")
    localStorage.setItem("isAdmin","false")
    setTimeout(() => {
      router.push({
        name: 'login',
        replace:true})
     
    },1000)
    console.log('logged out')
    
    // isAdminUser_from_localstorage = Boolean(localStorage.getItem("isAdmin"))
    console.log(localStorage.getItem("isAdmin"))
    toast_function('You are logged out successfully!!','success')
  })

  // input search
  let input_search = ref("")
  let show_search_result = ref(false)
  // watch(input_search,async () => {
  //   console.log("value de show_search_result: ", input_search.value.length)
  //   console.log(show_search_result.value)
  //   if (input_search.value.length == 0) {
  //     // reinititalize store
  //     searchItems.value = []
  //     // not display block result component
  //     show_search_result.value = false
  //   } else {
  //       searchItems.value = await search_record_albums(input_search.value) as Album[] 
  //       show_search_result.value = true
  //     }
  // })


  // isAdminUser_from_localstorage = Boolean(localStorage.getItem("isAdmin"))
//alternative 1

watch(search_text, (newValue, oldValue) => {
  if (newValue.toString().trim().length == 0) {
    console.log("the value of the length est:", newValue.toString().length);
    searchItems.value = [];
  } else {
    index_make_search(newValue.toString())
      .then((data: any) => {
        console.log("datattttt", data);
        searchItems.value = data;
      })
      .catch((err) => {
        console.log("SearchError", err);
        searchItems.value = [];
      });
  }

  console.log("test watcher", newValue);
});
//alternative 2
function submitForm() {
  console.log("test", search_text);
}
</script>
<template>

<div class="container_fluid"  v-if="isAdminStore">
  <div class="row flex-nowrap">
      <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-dark">
          <div class="d-flex flex-column align-items-center align-items-sm-start text-white min-vh-100 px-3 pt-2">

              <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start" id="menu">
                  <!-- Charts -->
                  <li class="nav-item pt-2">
                      <a href="#" class="nav-link align-middle px-0">
                        <router-link to="/admin/admin_charts" style="color:#bdc3c7;text-decoration: none;">
                          <font-awesome-icon icon="fa-solid fa-chart-pie" size="lg" :style="{ color: '#f0932b'}"/>
                           <span class="ms-1 d-none d-sm-inline px-2">Charts</span>
                        </router-link>
                      </a>
                  </li>
                  <!-- Orders -->
                  <li class="nav-item pt-2">
                      <a href="#" class="nav-link px-0 align-middle">
                        <router-link to="/admin/orders" style="color:#bdc3c7;text-decoration: none;">
                          <font-awesome-icon icon="fa-solid fa-bag-shopping" size="lg" :style="{ color: '#f0932b'}"/>  
                          <span class="ms-1 d-none d-sm-inline px-2">Orders</span>
                        </router-link>
                      </a>
                  </li>
                  <!--  albums -->
                  <li class="nav-item pt-2">
                    <a href="#" class="nav-link px-0 align-middle">
                      <router-link to="/admin/admin_albums" style="color:#bdc3c7;text-decoration: none;">
                        <font-awesome-icon icon="fa-solid fa-record-vinyl" size="lg" :style="{ color: '#f0932b'}"/> 
                        <span class="ms-1 d-none d-sm-inline px-2">Albums</span>
                      </router-link>
                    </a>
                  </li>
                  <!-- artists -->
                  <li class="nav-item pt-2">
                    <a href="#"  class="nav-link px-0 align-middle">
                      <router-link to="/admin/admin_artists"  style="color:#bdc3c7;text-decoration: none;" >
                        <font-awesome-icon icon="fa-solid fa-user-tie" size="lg" :style="{ color: '#f0932b'}"/>  
                        <span class="ms-1 d-none d-sm-inline px-2">Artists</span>
                      </router-link>
                    </a>
                  </li>

                  <!-- customers -->
                  <li class="nav-item pt-2">
                    <a href="#" class="nav-link px-0 align-middle">
                      <router-link to="/admin/customers" style="color:#bdc3c7;text-decoration: none;">
                        <font-awesome-icon icon="fa-solid fa-users" size="lg" :style="{ color: '#f0932b'}"/>
                        <span class="ms-1 d-none d-sm-inline">Customers</span>
                      </router-link>
                    </a>
                  </li>
                  <!-- category -->
                  <li class="nav-item pt-2">
                    <a href="#" class="nav-link px-0 align-middle">
                      <router-link to="/admin/admin_cat" style="color:#bdc3c7;text-decoration: none;">
                        <font-awesome-icon icon="fa-solid fa-cat" size="lg" :style="{ color: '#f0932b'}"/>
                        <span class="ms-1 d-none d-sm-inline">Categories</span>
                      </router-link>
                    </a>
                  </li>
                  <li class="nav-item pt-2">
                    <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/f/f4/User_Avatar_2.png" alt="hugenerd" width="30" height="30" class="rounded-circle">
                        <span class="d-none d-sm-inline mx-1">{{user_obj?.firstname}} Test {{user_obj?.username}}</span>
                    </a>
                      <ul class="dropdown-menu dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser1">
                        <li><a class="dropdown-item" href="#">Settings</a></li>
                        <li><a class="dropdown-item" href="#">Profile</a></li>
                        <li>
                            <hr class="dropdown-divider">
                        </li>
                        <li>
                            <a class="dropdown-item" href="#">
                              <button class="btn btn-warning" @click="onLogout">
                                Sign out
                              </button> 
                            </a>
                        </li>
                    </ul>
                  </li>
              </ul>
              <hr>
          </div>
      </div>
      <div class="col-md-8">
        <router-view name="orders_name"></router-view>
        <router-view name="customers_name"></router-view>
        <router-view name="albums_name"></router-view>
        <router-view name="artists_name"></router-view>
        <router-view name="cat_name"></router-view>
        <router-view name="charts_name"></router-view>
      </div>
  </div>
  
</div>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark" v-else>
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
        <li class="nav-item">
          <a class="nav-link active" href="#">
            <router-link to="/categories" style="color:#bdc3c7;text-decoration: none;">Categories</router-link>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="#">
            <router-link to="/artists" style="color:#bdc3c7;text-decoration: none;">Singers</router-link>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">
            <router-link to="/albums" style="color:#bdc3c7;text-decoration: none;">Albums</router-link>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">
            <router-link to="/promo" style="color:#bdc3c7;text-decoration: none;">Promo</router-link>
          </a>
        </li>
      </ul>
      
        <div class="row">
          <form class="d-flex">
            <input
              class="form-control me-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
              v-model="search_text"
            />
            <button class="btn btn-outline-warning me-4" type="submit" @click="submitForm">
              Search
            </button>
          </form>
         
        </div>
      <div class=".col-4 icon_header me-4 py-2 my-2">
        <!-- Link  to shop -->
        <a href="#">
          <router-link to="/panier" class="router_link_class" v-if="isLoggedIn_from_localstorage">
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
                    <li v-if='isLoggedIn_from_localstorage' class='px-3 py-2'>Log in as:</li>
                    <li v-if='isLoggedIn_from_localstorage'><hr class="dropdown-divider"></li>
                    <li v-if='isLoggedIn_from_localstorage' class='px-3 py-2 fst-normal'>
                      {{user_obj?.username}} {{user_obj?.firstname}}
                    </li>
                    <li v-if='isLoggedIn_from_localstorage' class='px-3 py-1 fst-normal'>
                      {{user_obj?.email}}
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
                    <li v-if='isLoggedIn_from_localstorage'><hr class="dropdown-divider"></li>
                    <li v-if="isLoggedIn_from_localstorage">
                      <a class="dropdown-item" href="#">
                        <div class="d-grid gap-2">
                          <button class="btn btn-danger" @click="onLogout">Logout</button>
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
