<script lang="ts" setup>
    import { storeToRefs } from 'pinia'
    import { read_one_artist } from '../../services/crud'
    import { useAppStore } from '../../stores';
    import { onMounted } from 'vue';
    import { useRoute } from 'vue-router';
    import { Artist } from '../../models';
    
    const route = useRoute()
    const value = route.params.id
    let id_router:number = parseInt(value[0])
    // let artist_selected:Artist;
    const { one_artist } = storeToRefs(useAppStore())
    onMounted(async() => {

       one_artist.value = (await read_one_artist(id_router))
        // console.log(one_artist.value?.cover)
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
        <div class="card m-3" style="width: 14rem;" v-for="item in one_artist?.list_album" :key="item.id"><!-- v-for="item in list_album" :key="item.id" -->
                <div class="card_title" style="background-color: rgba(0, 0, 0, 0.5)">
                    <img :src=getImage(item.cover) class="album_cover card-img-top rounded" alt="album picture">
                    <!-- Text Overlay -->
                    <div class="card-img" style="font-weight:500;">
                        <div class="card-text">
                            <p class="card-title text-white text-center pt-2">{{item.title}}</p>
                        <p class="text-white text-center align-self-center">{{item.release_date}}</p>
                        </div>
                        
                        <p class="text-white text-center align-self-center">
                            <a href="#">
                                <router-link to="/album_detail">
                                    <font-awesome-icon icon="fa-solid fa-angles-down" size="lg" :style="{ color: 'white' }" class="icon_show_album"/>
                                </router-link>
                            </a>
                        </p>
                    </div>
                </div>
                <div class="card-body">
                    <div class="row">
                        <img src="https://cdn.pixabay.com/photo/2018/08/28/13/29/avatar-3637561__340.png" class="rounded-circle" alt="user">
                        &nbsp;&nbsp;
                        <p class="description_paragraph">{{item.artist_id}}</p>
                    
                    </div>
                </div>
                <div class="card-footer row">
                    <a href="#">
                        <font-awesome-icon icon="fa-solid fa-star" size="lg" :style="{ color: 'black' }"/>
                    </a>
                    <a>
                        <font-awesome-icon icon="fa-solid fa-heart" size="lg" :style="{ color: 'black' }"/>
                    </a>
                    <a>
                            <font-awesome-icon icon="fa-solid fa-angles-right" size="lg" :style="{ color: 'black' }"/>
                    </a>
                    <a>
                            <font-awesome-icon icon="fa-solid fa-cart-shopping" size="lg" :style="{ color: 'orange' }"/>
                    </a>
                    <p>{{item.price}}</p>
                </div>
            </div>
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