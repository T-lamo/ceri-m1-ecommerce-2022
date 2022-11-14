
<script lang="ts" setup>
import { ref } from "vue"

let id = 0;
    const list_album=ref([
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022}
    ])
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
    <div class="row">
        <div class="card m-3" style="width: 14rem;" v-for="item in list_album" :key="item.id">
            <div class="card_title" style="background-color: rgba(0, 0, 0, 0.5)">
                <img src="https://cdn.pixabay.com/photo/2019/12/18/04/11/dj-4702977__340.jpg" class="card-img-top rounded" alt="album picture">
                <!-- Text Overlay -->
                <div class="card-img-overlay">
                    <h4 class="card-title text-white text-center ">{{item.title}}</h4>
                    <p class="text-white text-center align-self-center">{{item.Annee}}</p>
                    
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
                    <p class="description_paragraph">{{item.Chanteur}}</p>
                  
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
                <p>15$</p>
            </div>
        </div>
    </div>
    
</div>

</template>
<style scoped>
.card-body img {
    height: 30px;
    width: 30px;
}
</style>