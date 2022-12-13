<script lang="ts" setup>
    import { defineProps, onMounted, ref } from 'vue';
    import { read_promos , read_artists, read_one_album, read_albums} from '@/services/crud';
    import { Artist, Promo, type Album } from '../../models';
    import { storeToRefs } from 'pinia';
    import { useAppStore } from '@/stores';
    import { toast_function } from '@/services/crud';
    
    let id_cart_item = 0


    const props = defineProps<{
        item:Album,
        promo:boolean,
    }>()
    // console.log("here promo in cardtest: ",props.item)
    const getImage = (imagePath:string) => {
        return (imagePath);
    }
    const getDate = (str:string) => {
            const date = new Date(str)
            return date
    }
    let dateOfRelease:Date;
    // dateOfRelease = getDate(props.item.release_date);
    // const my_date_of_release:string = dateOfRelease.getDay()+"+""+
    // console.log('date below: '+dateOfRelease.getDate())
    // console.log(dateOfRelease.getDay())
    // console.log(dateOfRelease.getMonth())
    // console.log(dateOfRelease.getFullYear())
    const { list_promo , list_artist, list_cart_item, current_shopping_session} = storeToRefs(useAppStore())
    let my_promo:Promo
    onMounted(async () => {
      list_promo.value = (await read_promos()).map((res:any) => {
            return res;

          });
      list_artist.value = (await read_artists()).map((res:any) => {
            return res;
      })
    
    })
    
      
    const check_me_promo = () => {
        let my_selected_promo:Promo = new Promo;
        if (props.promo == true) {
              list_promo.value.forEach((element) => {
                if (element.album_id == props.item.id) {
                  my_selected_promo =  element; /** Select the last promo id */
                }
              })
        }
        
        return my_selected_promo

    }

    const check_me_artist = () => {
        let my_selected_artist = new Artist;
        list_artist.value.forEach((element) => {
          if (element.id == props.item.artist_id) {
            my_selected_artist = element
          }
        })
        return my_selected_artist
    }

    const add_me_to_cart = async (id_album:number,click_type:number) => {
      let my_article;
      /** specify whether it is an article added?=1 added to favory lists?=0 */
      let res = await read_one_album(id_album)
        .then((res) => 
          my_article = res)
        .catch((error) => console.log(error))
     
      
      console.log("here log")
      console.log(my_article)
      list_cart_item.value.push({
        
        'qty':1,
        'album_id': id_album,
        'shopping_session_id': current_shopping_session.value?.id!,
        'created_date': new Date()

      })
      console.log("list cart items for ")
      list_cart_item.value.forEach(element => {
        console.log(element)
      });
      
      // instance.dismiss()
      console.log("add me to chart");
    } 
   

</script>
<template>
    <!-- <div class="col-md-6 col-lg-4 mb-4 mb-md-0"> -->
    
        <div class="card m-3" style="width: 16rem;">
          <div class="d-flex justify-content-between p-3">
            <!-- <p class="lead mb-0">{{props.item}}</p> -->
            <div class="d-grid gap-2 justify-content-md-end">

                <button class="btn btn-outline-warning" @click="add_me_to_cart(props.item.id)">
                    <font-awesome-icon icon="fa-solid fa-cart-shopping" size="lg" style="{ color: '#f0932b' ;}"/>
                </button>
            </div>
            <div
              class="bg-warning rounded-circle d-flex align-items-center justify-content-center shadow-1-strong"
              style="width: 35px; height: 35px;">
              <p class="mb-0 small fa_heart">
                <font-awesome-icon icon="fa-solid fa-heart" size="lg" style="{ color: 'rgb(223, 249, 251)' ;}"/>
              </p>
            </div>
          </div>
          <div class="image_product">
              <img
              :src=getImage(props.item.cover) class="album_cover card-img-top rounded img-fluid"
              alt="album picture"
              style="height:180px;"
              />
          </div>
          
          <!-- <hr /> -->
          <div class="card-body">
            <div class="d-flex justify-content-between">
              <p class="small"><a href="#!" class="text-muted text-decoration-none">{{check_me_artist().firstname}} {{check_me_artist().lastname}}</a></p>
              <p v-if="props.promo == true" class="small text-danger">
                <s class="fs-6">${{props.item.price}}</s>
                </p>
            </div>

            <div class="d-flex justify-content-between mb-3">
              <h5 class="mb-0 fs-6">{{props.item.title}}</h5>
              <h5 v-if="promo" class="text-dark mb-0">$  {{props.item.price - (check_me_promo().rate / 100 * props.item.price)}}</h5>
              <h5 v-else class="text-dark mb-0 fs-6">$  {{props.item.price}} </h5>
            </div>

            <div class="d-flex justify-content-between mb-2">
              <p class="text-muted mb-0">Available: <span class="fw-bold" style="font-size:medium;">{{props.item.stock_qty}}</span></p>
              <div class="ms-auto text-warning">
                <font-awesome-icon icon="fa-solid fa-star" size="xs" style="{ color: '#f9ca24' ;}"/>
                <font-awesome-icon icon="fa-solid fa-star" size="xs" style="{ color: '#f9ca24' ;}"/>
                <font-awesome-icon icon="fa-solid fa-star" size="xs" style="{ color: '#f9ca24' ;}"/>
                <font-awesome-icon icon="fa-solid fa-star" size="xs" style="{ color: '#f9ca24' ;}"/>
                <font-awesome-icon icon="fa-solid fa-star" size="xs" style="{ color: '#f9ca24' ;}"/>
              </div>
            </div>
         
          </div>
      </div>
</template>
<style>
.image_product{
    border-radius: 5%;
}

.image_product:hover{
    cursor: pointer;
    box-shadow: 0 0 5px #1e272e
}
.fa_heart:hover, :focus{
    cursor:pointer;
    background:"red";
}
</style>