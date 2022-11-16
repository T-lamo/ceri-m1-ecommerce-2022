<script lang="ts" setup>
    import { ref } from "vue"
    let id = 0
    let id_1 = 0
    const list_album_category = ref([
    {"id":id_1++, "title": "all"},
    {"id":id_1++, "title": "country"},
    {"id":id_1++, "title": "rap"},
    {"id":id_1++, "title": "country"},
    {"id":id_1++, "title": "rock"},
    ])
    const list_album_achat=ref([
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452}
    ])

</script>

<template>
<div class="container-fluid py-2 px-5 my-3">
    <ul class="nav nav-tabs" > <!--  v-for="item in list_album_category" :key="item.id_1"-->
        <li class="nav-item" v-for="item_1 in list_album_category" :key="item_1.id">
            <a class="nav-link" href="#" style="color:#2C3A47;">{{item_1.title}}</a>
        </li>
        <form class="form-inline my-2 my-lg-0"> <!-- justify-content-end-->
            <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-warning my-2 my-sm-0" type="submit">Search</button>
        </form>
    </ul>
    <div class="card col-sm-12" style="max-width: 100%;"  v-for="item in list_album_achat" :key="item.id">
        <div class="row">
            <div class="col-md-4 px-4">
            <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.pOj4wYzV37FS_GUL3Jhg4AHaEo%26pid%3DApi&f=1&ipt=f3f9757cd32e68153b3abaefc6f7f8fe541cbe76913d2292551d870e5fab91ea&ipo=images" class="img-fluid rounded-start ps-5" style="max-width:250px;" alt="...">
            <!-- <p>Promotion</p> -->
        </div>
            <div class="col-md4">
            <div class="card-body">
                <h5 class="card-title">{{item.title}}</h5>
                <p class="card-text">{{item.Description}}</p>
                <p class="card-text"><small class="text-muted">{{item.Annee}} || {{item.Chanteur}} || {{item.Duree}} ''</small></p>
                <p>
                    <font-awesome-icon icon="fa-solid fa-star" size="sm" :style="{ color: '#1289A7' }"/>
                    <font-awesome-icon icon="fa-solid fa-star" size="sm" :style="{ color: '#1289A7' }"/>
                    <font-awesome-icon icon="fa-solid fa-star" size="sm" :style="{ color: '#1289A7' }"/>
                    <font-awesome-icon icon="fa-solid fa-star" size="sm" :style="{ color: '#1289A7' }"/>
                    <font-awesome-icon icon="fa-solid fa-star" size="sm" :style="{ color: '#1289A7' }"/>
                </p>
            </div>
            </div>

            <div class="col py-4 px-4 text-center">
                <div class="card-body">
                    <h4 class="font-monospace"><p style="color:#F79F1F;">$ {{item.Prix}}</p></h4>
                </div>
            </div>

            <div class="col py-4 px-4 text-center position-relative">
                <!-- <div class="d-grid gap-2 col-6 mx-auto"> -->
                    <div class="card-body">
                        <button class="btn btn-warning text-white text-center" type="button">
                            <font-awesome-icon icon="fa-solid fa-cart-shopping" size="sm" :style="{ color: '#1289A7' }"/>
                            Ajouter au panier
                        </button>
                    </div>
                
                <!-- </div> -->
            </div>
        </div>
    </div>
</div>

</template>