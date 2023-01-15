<script lang="ts" setup>
  import { storeToRefs } from "pinia";
  import {
    read_albums,
  } from "../../services/crud";
  import { useAppStore } from "../../stores";
  import { onMounted, type Ref } from "vue";
  import OneArticle from "./OneArticle.vue";
  const { list_album } = storeToRefs(useAppStore());

  onMounted(async () => {
    list_album.value = (await read_albums()).map((res: any) => {
      return res;
    });
    
  });
</script>
<template>
  <div class="container-fluid py-2 px-5 my-2 text-center">
    <span><i> List of albums </i> </span>
    <hr class="dropdown-divider" />
    <div class="row mx-auto">
      <OneArticle
        v-for="item in list_album"
        :key="item.id"
        :item="item"
        :promo="false"
      />
    </div>
  </div>
</template>

