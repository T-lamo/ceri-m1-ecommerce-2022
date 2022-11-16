
<script lang="ts" setup>
    import { storeToRefs } from 'pinia'
    import { read_albums } from '../../services/crud'
    import { useAppStore } from '../../stores';
    import { onMounted } from 'vue';
    import OneAlbumDetail  from './OneAlbumDetail.vue'

    const { list_album } = storeToRefs(useAppStore())
    onMounted(async() => {
        list_album.value = (await read_albums()).map((res:any) => {
            return res;
        })
    })
    // const data_album = {
    //     "id": 0,
    //     "title":'',
    //     "release_date": '',
    //     "cover":'',
    //     "price":0,
    //     "stock_qty":0,
    //     "description":'',
    //     "category_id":0
    // }
</script>
<template>
<div class="container-fluid py-2 px-5 my-3">
    <span><i>
        Liste des albums 
        <router-link to="/list_album_achat">    
            <font-awesome-icon icon="fa-solid fa-circle-plus" size="lg" :style="{ color: '#1B1464' }"/>
        </router-link>
    </i>
    </span>
    <hr class="dropdown-divider">
    <div v-for="item in list_album" :key="item.id">
        <OneAlbumDetail
            :album_id="item.id"
            :title="item.title"
            :release_date="item.release_date"
            :cover="item.cover"
            :price="item.price"
            :stock_qty="item.stock_qty"
            :description="item.description"
            :category_id="item.category_id"
            :artist_id="item.artist_id"
            />
    </div>
    
</div>

</template>