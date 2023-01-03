<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
import HeaderComponent from "./components/common/HeaderComponent.vue";
import FooterComponent from "./components/common/FooterComponent.vue";
import SidebarComponent from "./components/common/SidebarComponent.vue";
import SearchComponent from "./components/common/SearchComponent.vue";


</script>

<template>
  <div class="app">
    <div class="header">
      <HeaderComponent />
    </div>

    <div class="sidebar">
      <SidebarComponent />
    </div>
    <nav class="main">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </nav>

    <div class="footer">
      <FooterComponent />
    </div>
    <div class="search">
      <SearchComponent />
    </div>
  </div>

  <RouterView />
</template>

<style lang="scss" scoped>
@use "./assets/scss/mixin" as mixin;

.app {
  display: grid;
  grid-template-areas:
    "h h"
    "s m"
    "f f";
  grid-template-rows: 72px 1fr 50px;
  grid-template-columns: 400px 1fr;
  column-gap: 1rem;

  .header {
    position: sticky;
    top: 0;
    grid-area: h;
    z-index: 10000;
  }
  .sidebar {
    grid-area: s;
    background: var(--gray-1);
  }

  .main {
    padding: 1rem;
    grid-area: m;
    min-height: calc(100vh - (120px + 6rem));
  }
  .footer {
    grid-area: f;
    z-index: 10;
  }

  .search {
    display: flex;
    // justify-content: center;
    width: 50%;
    margin-left: 25%;
    position: fixed;
    top: 60px;
    z-index: 10;
  }
}

@media screen and (max-width: 577px) {
  .app {
    .search {
      position: fixed;
      top: 150px;
      left: 0px;
      margin-left: 5%;
      width: 90%;
      align-items: center;
    }
  }
}

@media screen and (max-width: 992px) {
  .app {
    grid-template-areas:
      "h"
      "m"
      "f";
    grid-template-columns: 1fr;
    .sidebar {
      position: fixed;
      top: 0;
      width: 400px;
    }
  }
}

@media screen and (min-width: 993px) {
  .app {
    grid-template-areas:
      "h h"
      "s m"
      "f f";
    grid-template-rows: 72px 1fr 50px;
    grid-template-columns: 300px 1fr;
    .sidebar {
      position: fixed;
      top: 0;
    }
  }
}

@include mixin.xs {
  .app {
    grid-template-rows: 150px 1fr 50px;
  }
}
</style>
