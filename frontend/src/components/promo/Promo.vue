<script lang="ts" setup>
    import { read_promos, read_albums} from '@/services/crud';
    import { storeToRefs } from 'pinia';
    import { useAppStore } from '@/stores';
    import { onMounted } from 'vue';
    import type { Album, Promo } from '../../models';
    import OneArticle from '../album/OneArticle.vue';
        
    const { list_promo, list_album } = storeToRefs(useAppStore())

    onMounted(async () => {
        list_album.value = (await read_albums()).map((res:any) => {
            return res;
        })
        list_promo.value = (await read_promos()).map((res:any) => {
            return res;

        });
    })

    let today:Date = new Date()
    const album_promo = () => {
        let last_product_promo =list_promo.value.reduce<Promo[]>((acc: Promo[], curr: Promo)=> {
            let find_album: Promo[] = acc.filter((v)=> v.album_id == curr.album_id);
            let my_date:Date = new Date(curr.end_date)
            if (find_album.length==0 || my_date >= today ) { /** à changer */
                acc.push(curr)
            }
            return acc;
        }, [])

        let album_id_list: number[] = last_product_promo.map( (promo:Promo)=> {
            return promo.album_id;
        }) 

        let list_album_promo: Album[] = list_album.value.filter((album : Album) => {
            if (album_id_list.includes(album.id!)) {
                return true;
            }
            return false;
        })
        
        return list_album_promo;
    }
  
</script>

<template >
    <div class="container-fluid py-2 px-5 my-2 text-center">
        <span><i>
            Promotions 
        </i>
        </span>
        <hr class="dropdown-divider">
        
                <div class="row mx-auto"> 
                
                    <OneArticle 
                        v-for="item in album_promo()" :key="item.id"
                        :item = item
                        :promo = true
                            />
                </div>
          
    </div>
</template>