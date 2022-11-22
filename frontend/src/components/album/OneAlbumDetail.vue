<script lang="ts" setup>
import { defineProps } from 'vue';
import type { Album } from '../../models';
const props = defineProps<{
    item:Album,
}>()

const getImage = (imagePath:string) => {
    return (imagePath);
}
const getDate = (str:string) => {
        const date = new Date(str)
        return date
}
let dateOfRelease:Date;
dateOfRelease = getDate(props.item.release_date)
// const my_date_of_release:string = dateOfRelease.getDay()+"+""+
console.log('date below: '+dateOfRelease.getDate())
console.log(dateOfRelease.getDay())
console.log(dateOfRelease.getMonth())
console.log(dateOfRelease.getFullYear())

</script>
<template>
    
        <div class="card m-3 py-2 px-2 my-2" style="width: 14rem;">
                <div class="card_title" style="background-color: rgba(0, 0, 0, 0.5)">
                    <img :src=getImage(props.item.cover) class="album_cover card-img-top rounded" alt="album picture">
                    <!-- Text Overlay -->
                    <div class="card-img" style="font-weight:500;">
                        <div class="card-text">
                            <p class="card-title text-white text-center pt-2">{{props.item.title}}</p>
                            <p class="text-white text-center align-self-center">{{props.item.release_date}}</p>
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
                        <p class="description_paragraph">{{props.item.artist_id}}</p>
                    
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
                    <p>{{props.item.price}}</p>
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