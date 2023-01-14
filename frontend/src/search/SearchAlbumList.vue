<script lang="ts" setup>
import { onMounted, watchEffect } from "vue";
import { useAppStore } from "@/stores";
import { storeToRefs } from "pinia";
import SearchOneAlbum from "./SearchOneAlbum.vue";

const { searchItems } = storeToRefs(useAppStore());

watchEffect(() => {
  console.log("search items album list", searchItems.value);
});
</script>

<template>
  <div class="cont">
    <ul>
      <router-link
        v-for="item in searchItems"
        :key="item.id"
        :to="{ name: 'album_selected', params: { id: item.id } }"
      >
        <li>
          <SearchOneAlbum :album="item" />
        </li>
      </router-link>
    </ul>
  </div>
</template>

<style scoped>
.cont {
  background-color: #ffffff;
  width: 600px;
  border: 1px solid gray;
  max-height: 395px;
  overflow-y: auto;
}
ul {
  display: flex;
  flex-direction: column;
  /* grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); */
  color: black;
  overflow-y: auto;
  list-style: none;
  padding: 2px !important;
  margin: 0px !important;
}
li {
  color: red;

}

/* li:hover {
  background: var(--gray-2);
} */
</style>
