<script lang="ts" setup>
import { ref } from "vue"

let id = 0
const list_artist = ref([
    {'id':id++,"firstname":"firstname","username":"username","pseudo":"PSEUDO"},
    {'id':id++,"firstname":"firstname","username":"username","pseudo":"PSEUDO"},
    {'id':id++,"firstname":"firstname","username":"username","pseudo":"PSEUDO"},
    {'id':id++,"firstname":"firstname","username":"username","pseudo":"PSEUDO"},
    {'id':id++,"firstname":"firstname","username":"username","pseudo":"PSEUDO"}
])

</script>

<template>
    <div class="container-fluid py-2 px-5 my-3">
        <span><i>Liste des artistes <font-awesome-icon icon="fa-solid fa-circle-plus" size="lg" :style="{ color: '#1B1464' }"/></i></span>
        <hr class="dropdown-divider">
        <div class="row">
            <div class="card m-3" style="width: 14rem; background: black;" v-for="item in list_artist" :key="item.id">
                <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.9ZlQwEdEIIVtL57JESOE9gHaEK%26pid%3DApi&f=1&ipt=0b8f34aec35e24169c20aa3645e5d94a1c45ddd6d41e641ea2d13f5c9ab285bc&ipo=images" class="rounded-circle">
                <div class="card-body">
                    <p>{{item.firstname }} {{item.username}}</p>
                    <p>{{item.pseudo}}</p>
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