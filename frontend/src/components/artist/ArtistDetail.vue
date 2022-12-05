<script lang="ts" setup>
    import { storeToRefs } from 'pinia'
    import { read_one_artist } from '../../services/crud'
    import { useAppStore } from '../../stores';
    import { onMounted } from 'vue';
    import { useRoute } from 'vue-router';
    import { Artist } from '../../models';
    import OneArticle from '../album/OneArticle.vue';

    const route = useRoute()
    const value = route.params.id
    let id_router:number = parseInt(value[0])
    
    const { one_artist } = storeToRefs(useAppStore())
    onMounted(async() => {

       one_artist.value = (await read_one_artist(id_router))
       
    })
    const getImage = (imagePath:string) => {
        return (imagePath);
    }
</script>
<template>
    <div class="container">
        <h4 class="text-center">Artist Detail: {{$route.params.id}}</h4>
        <br>
        <div class="container-fluid py-2 px-5 my-3 row">
            <div class="col">
                <img class="rounded-circle" :src=getImage(one_artist?.cover)>
            </div>
            <div class="col">
                <p>{{one_artist?.firstname}}</p>
                <p>{{one_artist?.lastname}}</p>
                <p>{{one_artist?.date_of_birth}}</p>
            </div>
           
        </div>
        <!-- a revoir ????-->
        <h2>Album associes</h2>
        <hr class="dropdown-divider">
        <div class="container-fluid" style="display:flex;">
        
               <OneArticle
                v-for="item in one_artist?.list_album" :key="item.id"
                :item="item"
                :promo=false
                    />
        </div>
    </div>
    
</template>
<style scoped>
.col img {
    width: 100px;
    height: 100px;
    border-radius: 50px 50px 50px 50px;
}
.card-body img {
    height: 30px;
    width: 30px;
}
.album_cover {
    /* width; */
    height: 180px;
}
</style>