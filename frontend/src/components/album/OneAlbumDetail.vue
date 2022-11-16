<script lang="ts" setup>
import { defineProps } from 'vue';
const props = defineProps<{
    album_id: number,
    title: string,
    release_date:string,
    cover:string,
    price:number,
    stock_qty:number,
    description:string,
    category_id:number,
    artist_id:number 
}>()

console.log(props.title)

const getImage = (imagePath:string) => {
    return (imagePath);
}
</script>
<template>
    <!-- <div class="col"> -->
        <div class="card m-3" style="width: 14rem;"><!-- v-for="item in list_album" :key="item.id" -->
                <div class="card_title" style="background-color: rgba(0, 0, 0, 0.5)">
                    <img :src=getImage(props.cover) class="album_cover card-img-top rounded" alt="album picture">
                    <!-- Text Overlay -->
                    <div class="card-img" style="font-weight:500;">
                        <div class="card-text">
                            <p class="card-title text-white text-center pt-2">{{props.title}}</p>
                        <p class="text-white text-center align-self-center">{{props.release_date}}</p>
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
                        <p class="description_paragraph">{{props.artist_id}}</p>
                    
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
                    <p>{{props.price}}</p>
                </div>
            </div>
    <!-- </div> -->
</template>
<style scoped>
.card-body img {
    height: 30px;
    width: 30px;
}
.album_cover {
    /* width; */
    height: 180px;
}
</style>