<script lang="ts" setup>
    import { defineProps, onMounted, ref } from 'vue';
    import { read_promos , read_artists, read_one_album, read_albums,update_cart_item, 
      create_cart_item, read_cart_items_by_sessionid} from '@/services/crud';
    import { Artist, CartItem, Promo, type Album } from '../../models';
    import { storeToRefs } from 'pinia';
    import { useAppStore } from '@/stores';
    import { toast_function } from '@/services/crud';
    
    const user_from_localstorage = localStorage.getItem("userId")
    const user_obj = JSON.parse(user_from_localstorage!)
    const isLoggedIn_from_localstorage = Boolean(localStorage.getItem("isLoggedIn"))
    const props = defineProps<{
        item:Album,
        promo:boolean,
    }>()

    const getImage = (imagePath:string) => {
        return (imagePath);
    }

    const { list_promo , list_artist, list_cart_item, current_shopping_session} = storeToRefs(useAppStore())
   
    onMounted(async () => {
      list_promo.value = (await read_promos()).map((res:any) => {
            return res;

          });
      list_artist.value = (await read_artists()).map((res:any) => {
            return res;
      })
    
    })
    
    const chek_if_exist_in_promo = () => {
      let res = false;
      list_promo.value.forEach((element) => {
          if (element.album_id == props.item.id) {
              res = true
          }
      })
      return res
    }

    const return_promo = () => {
        let my_selected_promo:Promo = new Promo;
        if (chek_if_exist_in_promo()) {
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

    const check_existence_cart_item = ((shopping_session_id:number, album_id:number) => {
      let found = false
      list_cart_item.value.forEach(async (element:CartItem) => {
        if (shopping_session_id == element.shopping_session_id && album_id == element.album_id) {
          // update cart item to db
          
          // update cart item in store
          element.qty+=1
          element.created_date = new Date()
          found = true
        }
      })
      return found
    })

    const add_me_to_cart = async (id_album:number) => {
      
      // if loggedd in
      if (isLoggedIn_from_localstorage == true) {
        let my_article;
        /** specify whether it is an article added?=1 added to favory lists?=0 */
        let res = await read_one_album(id_album)
          .then((res) => 
            my_article = res)
          .catch((error) => console.log(error))
        
        // only if cart item does not in cart item
        if (check_existence_cart_item(current_shopping_session.value?.id!,id_album)) {

        } else {
            // create a new cart item
            let one_cart_item = new CartItem({
              'qty':1,
              'album_id': id_album,
              'shopping_session_id': current_shopping_session.value?.id!,
              'created_date': new Date()
            })

            // create a cart item to shopping session in db
            let response_create_a_cart_item = await create_cart_item(one_cart_item)
              .then(res => console.log("cart item created successfully"))
              .catch(error => console.log(error))

            // add to list_cart_item selected cart item
            list_cart_item.value.push(one_cart_item)

        }

        console.log("list cart items for ")
        list_cart_item.value.forEach(element => {
          console.log(element)
        });
        
        toast_function("Article successfully add to cart!","success")
      }
      else {
        toast_function("Please login","error")
      }
      
    } 
   

</script>
<template>

        <div class="card m-3" style="width: 16rem;">
          <div class="d-flex justify-content-between p-3">
            <div class="d-grid justify-content-md-end">

                <button class="btn btn-outline-warning" @click="add_me_to_cart(props.item.id!)">
                    <font-awesome-icon icon="fa-solid fa-cart-shopping" size="lg" :style="{ color: '#f0932b'}"/>
                </button>
            </div>
          </div>
          <div class="image_product">
            <router-link :to="{ name: 'album_selected', params: {'id': item.id}}">
              <img
              :src=getImage(props.item.cover!) class="album_cover card-img-top rounded img-fluid"
              alt="album picture"
              style="height:180px;"
              />
          </router-link>
          </div>
          <div class="card-body">
            <div class="d-flex justify-content-between">
              <p class="small"><a href="#!" class="text-muted text-decoration-none">{{check_me_artist().firstname}} {{check_me_artist().lastname}}</a></p>
              <p v-if="chek_if_exist_in_promo()" class="small text-danger">
                <s class="fs-6">${{props.item.price}}</s>
                </p>
            </div>

            <div class="d-flex justify-content-between mb-3">
              <h5 class="mb-0 fs-6">{{props.item.title}}</h5>
              <h5  v-if="promo && !chek_if_exist_in_promo" class="text-dark mb-0 fs-6">$  {{props.item.price - (return_promo().rate / 100 * props.item.price)}}</h5>
              <h5 v-else-if="chek_if_exist_in_promo() && promo==false" class="text-dark mb-0 fs-6">$  {{props.item.price - (return_promo().rate / 100 * props.item.price)}}</h5>
              
              <h5 v-else class="text-dark mb-0">$  {{props.item.price}} </h5>
              
            </div>

            <div class="d-flex justify-content-between mb-2">
              <p class="text-muted mb-0">Available: <span class="fw-bold" style="font-size:medium;">{{props.item.stock_qty}}</span></p>
              <div class="ms-auto text-warning">
                <font-awesome-icon icon="fa-solid fa-star" size="xs" :style="{ color: '#f9ca24'}"/>
                <font-awesome-icon icon="fa-solid fa-star" size="xs" :style="{ color: '#f9ca24'}"/>
                <font-awesome-icon icon="fa-solid fa-star" size="xs" :style="{ color: '#f9ca24'}"/>
                <font-awesome-icon icon="fa-solid fa-star" size="xs" :style="{ color: '#f9ca24'}"/>
                <font-awesome-icon icon="fa-solid fa-star" size="xs" :style="{ color: '#f9ca24'}"/>
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