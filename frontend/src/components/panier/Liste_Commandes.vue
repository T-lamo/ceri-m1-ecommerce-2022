<script lang="ts" setup>
    import OneCommand from './OneCommand.vue'
    import { ref } from "vue"
    import { read_one_album, toast_function } from '@/services/crud';
    import { useAppStore } from '@/stores';
    import { storeToRefs } from 'pinia';
    
    const {list_cart_item} = storeToRefs(useAppStore())

    // const album_chosen = (async (id_album:number) => {
      
    //   return await read_one_album(id_album)
    //           .then((res:any) => {
    //             console.log(res)
    //           })
    //           .catch((error:any) => console.log(error))
    // })
  
    // let id = 0
    // let total = 0

</script>

<template>
            <div class="col-md-8">
                <div class="card mb-4">
                    <div class="card-header">
                        Liste des commandes
                    </div>
                    <!-- One command -->
                    
                    <OneCommand
                        v-for="item in list_cart_item" :key="item.id"
                        :item=item
                        />
                    
                </div>
            </div>

</template>
