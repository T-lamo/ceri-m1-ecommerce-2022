<script lang="ts" setup>
    import { storeToRefs } from 'pinia'
    import { read_artists } from '../../services/crud'
    import { useAppStore } from '../../stores';
    import { onMounted } from 'vue';

    const { list_artist } = storeToRefs(useAppStore())
    onMounted(async() => {
        list_artist.value = (await read_artists()).map((res:any) => {
            return res;
        })
    })
    const getImage = (imagePath:string) => {
        return (imagePath);
    }
</script>

<template>
    <div class="container-fluid py-2 px-5 my-3">
        <span><i>Liste des artistes <font-awesome-icon icon="fa-solid fa-circle-plus" size="lg" :style="{ color: '#1B1464' }"/></i></span>
        <hr class="dropdown-divider">
        <div class="row">
            <div class="card m-3" style="width: 14rem; background: black;" v-for="item in list_artist" :key="item.id">
                <img :src=getImage(item.cover) class="rounded-circle">
                <div class="card-body">
                    <p>{{item.lastname }}</p>
                    <p>{{item.firstname}}</p>
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