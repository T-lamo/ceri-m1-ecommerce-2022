<script lang="ts" setup>
    import { onMounted } from 'vue'
    import { read_songs , read_one_album, read_albums} from '../../services/crud'
    import  { Album, type Song } from '../../models'
    import { useRoute } from 'vue-router'
    import { storeToRefs } from 'pinia'
    import { useAppStore } from '@/stores'
    import OneSong from '../songs/OneSong.vue'
    
    const { list_song, list_album} = storeToRefs(useAppStore())

    onMounted(async() => {
        list_song.value = await read_songs() as Song[]
        list_album.value = await read_albums() as Album[]
    })

    // routing
    const route = useRoute()
    const value = route.params.id
    let id_router:number = parseInt(value[0])

    // read one album
    const readOneAlbum = ():Album => {
        let res = new Album
        list_album.value.forEach((element) => {
            if (element.id == id_router) 
                res = element
        })
        return res
    }
    
    // return corresponding songs for selected album
    const returnSongsOneAlbum = (): Array<Song> => {
        let res:Array<Song> = []
        list_song.value.forEach((element) => {
            if (element.album_id == id_router) 
                res.push(element)
        })
        return res
    }

    const getImage = (imagePath:string) => {
        return (imagePath);
    }


</script>
<template>
    
    <div class="container pt-4">
        <button class="btn btn-transparent">
            <router-link to="/albums" style="color:#bdc3c7;text-decoration: none;" >
                <font-awesome-icon icon="fa-solid fa-arrow-left-long" size="lg" :style="{ color: 'black'}"/>
                Back  
            </router-link>
        </button>
        <h4 class="text-center">Album Detail # {{$route.params.id}}</h4>
        <br>
        <div class="container-fluid py-2 px-5 my-3 row">
            <div class="col">
                <img class="img-fluid" :src=getImage(readOneAlbum().cover!)>
            </div>
            <div class="col">
                <p><b>Title:</b>{{readOneAlbum().title}}</p>
                <p><b>Description: </b>{{readOneAlbum().description}}</p>
                <p><b>Singers: </b>{{readOneAlbum().artist_id}}</p>
                <p><b>Price: $</b>{{readOneAlbum().price}}</p>
            </div>
        
        </div>
        <h2 class="text-center">Associated songs:</h2>
        <hr class="dropdown-divider">
        <div class="container-fluid" style="display:flex;">
        
            <OneSong
                v-for="item in returnSongsOneAlbum()" :key="item.id"
                :item = item
                    />
        </div>
    </div>
</template>
<style scoped>
.col img {
    width: auto;
}
</style>