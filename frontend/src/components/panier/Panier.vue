<script lang="ts" setup>
import { ref , computed} from "vue"

let id = 0
let total = 0
const list_album_panier=ref([
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
const count = ref(0)
/* increment function */
const increment = computed(() => {
    count.value++
})
/* decrement funtion */
const decrement = computed(() => {
    count.value--
})
</script>

<template>
<div class="container row">
    <div class="container-fluid py-2 px-5 my-3 col">
    <h4 class="text-center">LISTE DE MES ACHATS </h4>
        <div class="card mb-3 col" style="max-width: 540px;" v-for="item in list_album_panier" :key="item.id">
            <div class="row">
                <div class="col-md-4">
                <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.UXfWyeZW4Fh03oB0ECwZPwHaHa%26pid%3DApi&f=1&ipt=5b9ee3ebfca08d1f753b9657ac74db41ba70fa8a50a5df266b64738c3424275a&ipo=images" class="img-fluid rounded-start" alt="...">
                </div>
                <div class="col-md-8">
                <div class="card-body">
                    <h5 class="card-title">{{item.title}}</h5>
                    <hr class="dropdown-divider">
                    <p class="card-text">{{item.Description}} || {{item.Chanteur}} || {{item.Annee}} </p>
                    <p class="card-text">
                        <small class="text-muted">
                            <button class="btn btn-outline-warning" @click="decrement">
                                <font-awesome-icon icon="fa-solid fa-minus" size="lg" :style="{ color: '#B33771' }"/>
                            </button>
                            <input type="number" value={{count}} min="0">
                            <button class="btn btn-outline-warning" @click="increment">
                                <font-awesome-icon icon="fa-solid fa-plus" size="lg" :style="{ color: '#B33771' }"/>
                            </button>
                            <card-text>
                                {{total}} || {{count}}
                            </card-text>
                        </small>
                </p>
                </div>
                <div class="card-footer">
                    <div class="col">
                        <font-awesome-icon icon="fa-solid fa-heart" size="lg" :style="{ color: '#B33771' }"/>
                        <font-awesome-icon icon="fa-solid fa-pen-to-square" size="lg" :style="{ color: '#1B9CFC' }"/>
                        <font-awesome-icon icon="fa-solid fa-trash" size="lg" :style="{ color: '#B33771' }"/>
                    </div>
                </div>
                </div>
            </div>
        </div>
    </div>
    <br>
    <div class="container-fluid py-2 px-5 my-3 col"> <!-- col-auto py-2 px-5 my-3 pt-4-->
        <h4>Test here</h4>
            <div class="card mb-3 col">
                <div class="card-title">
                    <h4>RECAPITULATIF</h4>
                </div>
                <hr class="dropdown-divider">
                <div class="card-body">
                    <div class="card-text">Produit 1 (250$)</div>
                </div>
                <div class="card-footer">
                    <button class="btn-lg btn btn-warning">PASSER LA COMMANDE </button>
                </div>
            </div>
        </div>
    
</div>
</template>
