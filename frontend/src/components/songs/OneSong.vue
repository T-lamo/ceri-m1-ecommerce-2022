<script lang="ts" setup>
    import { onMounted } from 'vue'
    import { read_songs , read_one_album} from '../../services/crud'
    import type { Song } from '../../models'
    
    const props = defineProps<{
        item:Song
    }>()
   
    console.log(props.item)

    const getImage = (imagePath:string) => {
        return (imagePath);
    }
</script>
<template>
    <div class="card m-3 text-center" style="width: 16rem;">
        <div>
          <router-link :to="{ name: 'album_selected', params: {'id': item.id}}">
            <img
            :src=getImage(props.item.cover!) class="album_cover card-img-top rounded img-fluid"
            alt="album picture"
            style="height:180px;"
            />
        </router-link>
        </div>
        <div class="card-body">
        
          <div class="d-flex justify-content-between mb-3">
            <h5 class="mb-0 fs-6">{{props.item.title}}</h5> 
          </div>

        </div>
    </div>
</template>
