<script lang="ts" setup>
    import { defineProps } from 'vue';
    import type { Artist } from '../../models';
    const props = defineProps<{
        item:Artist,
    }>()
    const getImage = (imagePath:string) => {
    return (imagePath);
}
</script>
<template>
    <div class="card m-3" style="width: 14rem; background: black;"><!-- v-for="item in list_artist" :key="item.id" -->
                <img :src=getImage(props.item.cover) class="rounded-circle">
                <div class="card-body">
                    <p>{{props.item.lastname }}</p>
                    <p>{{props.item.firstname}}</p>
                        <router-link :to="{ name: 'artist', params: {'id':item.id}}">
                            <font-awesome-icon icon="fa-solid fa-angles-down" size="sm" :style="{ color: '#1289A7' }"/>
                        </router-link>
                </div>
                <div class="">
                    <div class="btn-group-sm" role="group" aria-label="Basic example">
                        <button type="button" class="btn btn-outline-warning">
                            124 albums
                        </button>
                        <button type="button" class="btn btn-outline-warning">
                            2.k
                            <font-awesome-icon icon="fa-solid fa-heart" size="xs" :style="{ color: 'white' }"/>
                        </button>
                        <button type="button" class="btn btn-outline-warning">
                            1.k 
                            <font-awesome-icon icon="fa-solid fa-star" size="xs" :style="{ color: 'white' }"/>
                        </button>
                    </div>                     
                </div>
        </div>
</template>
<style scoped>
.card {
    align-items: center;
    color: white;
    text-align: center;
}
.card img {
    width: 100px;
    height: 120px;
}
.list_btn {
   display: flex;
    /* background: red; */
    width: 100%;
}
.list_btn button {
    display: block;
    padding: 0 0 0 0;
    margin: 0 0 0 0;
}
</style>