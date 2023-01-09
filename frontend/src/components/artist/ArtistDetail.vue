<script lang="ts" setup>
    import { storeToRefs } from 'pinia'
    import { read_one_artist } from '../../services/crud'
    import { useAppStore } from '../../stores';
    import { onMounted } from 'vue';
    import { useRoute } from 'vue-router';
    import type { Artist } from '../../models';
    import OneArticle from '../album/OneArticle.vue';

    const route = useRoute()
    const value = route.params.id
    let id_router:number = parseInt(value[0])
    
    const { one_artist } = storeToRefs(useAppStore())
    onMounted(async() => {

       one_artist.value = (await read_one_artist(id_router)) as Artist
       
    })
    const getImage = (imagePath:string) => {
        return (imagePath);
    }
</script>
<template>
    <div class="container pt-4">
        <button class="btn btn-transparent">
            <router-link to="/artists" style="color:#bdc3c7;text-decoration: none;" >
                <font-awesome-icon icon="fa-solid fa-arrow-left-long" size="lg" :style="{ color: 'black'}"/>
                Back  
            </router-link>
        </button>
        <h4 class="text-center">Artist Detail # {{$route.params.id}}</h4>
        <br>
        <div class="container-fluid py-2 px-5 my-3 row">
            <div class="col">
                <img class="rounded-circle" :src=getImage(one_artist?.cover!)>
            </div>
            <div class="col">
                <p><b>Firstame:</b> {{one_artist?.firstname}}</p>
                <p><b>Lastname: </b>{{one_artist?.lastname}}</p>
                <p><b>Born in: </b>{{one_artist?.date_of_birth}}</p>
            </div>
           
        </div>
        <h2 class="text-center">Associated albums:</h2>
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
</style>