<script lang="ts" setup>
    import { useAppStore } from '@/stores';
    import { storeToRefs } from 'pinia';

    const {list_album, list_cart_item} = storeToRefs(useAppStore())
    
    const check_id_album = (album_id:number) => {
        let qty = 0
        let found = false
        list_cart_item.value.forEach(cart => {
            if (album_id == cart.album_id) {
                qty = cart.qty
                found = true
            }
        })
        return qty
    }
    const getImage = (imagePath:string) => {
        return (imagePath);
    }
         
</script>
<template>
    <div class="row-cols-3" v-for="product in list_album">
        <div class="col" v-if="check_id_album(product.id)">
            <div class="card m-3" style="width: 16rem;" >
                <img :src=getImage(product.cover!) class="card-img-top" alt="..." style="height:180px;">
                        <div class="card-body">
                            <!-- <h5 class="card-title">Titre de l'album: {{product.title}}</h5> -->
                            <p class="card-text">Titre de l'album: {{product.title}}</p>
                            <p class="card-text">Quantité: {{check_id_album(product.id)}}</p>
                        </div>                
                       
            </div>
        </div>
    </div>
</template>