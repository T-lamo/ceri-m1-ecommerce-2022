
<script lang="ts" setup>
    import { storeToRefs } from 'pinia'
    import { read_albums } from '../../services/crud'
    import { useAppStore } from '../../stores';
    import { onMounted } from 'vue';
    import OneArticle from "./OneArticle.vue"
    const { list_album } = storeToRefs(useAppStore())
    onMounted(async() => {
        list_album.value = (await read_albums()).map((res:any) => {
            return res;
        })
        // console.log("here list: ",list_album.value)
    })
  

</script>
<template>
<div class="container-fluid py-2 px-5 my-2">
    <span><i>
        Liste des albums 
        <router-link to="/list_album_achat">    
            <font-awesome-icon icon="fa-solid fa-circle-plus" size="lg" :style="{ color: '#1B1464' }"/>
        </router-link>
    </i>
    </span>
    <hr class="dropdown-divider">
    <div class="row mx-auto">
                <OneArticle
                    v-for="item in list_album" :key="item.id"
                    :item = item
                    :promo=false
                    />
    </div>
</div>

</template>
<style scoped>
    
</style>
