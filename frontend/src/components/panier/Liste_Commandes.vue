<script lang="ts" setup>
import OneCommand from './OneCommand.vue'
import { ref , computed} from "vue"

let id = 0
let total = 0

const list_album_panier=ref([
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452},
        {"id":id++, "title": "Album 1", "Description":"description album 1","Chanteur":"chanerur 1","Annee":2022,"Duree":45,"Prix":452},
    ])
</script>

<template>
            <div class="col-md-8">
                <div class="card mb-4">
                    <div class="card-header">
                        Liste des commandes
                    </div>
                    <!-- One command -->
                    <OneCommand
                        v-for="item in list_album_panier" :key="item.id"
                                />
                    
                </div>
            </div>

</template>
