<script lang="ts" setup>
   import Liste_Commandes from './Liste_Commandes.vue';
   import Paiement from './Paiement.vue';
   import Livraison from './Livraison.vue'
   import { ref } from "vue"
   import { useAppStore } from '@/stores';
   import { storeToRefs } from 'pinia';
   import type { CartItem, OrderDetail } from '@/models';
   import { create_order_detail, read_lastone_order_detail_byuserid,create_order_item } from '@/services/crud';

   const {list_cart_item, total_price, list_album, current_user, current_order_detail} = storeToRefs(useAppStore())

   // create an order detail and add order items
   const create_order_detail_order_items = async () => {

    let new_order_detail =  await create_order_detail({
        "created_date": new Date(),
        "user_id": current_user.value?.id!,
        "total": total_price.value,
        "delivery_status": false,
        "payment_status":false,
        "send_status": false,
        "orders_status": "rien"
    })
    // get last order detail for a user
    let last_order_detail = await read_lastone_order_detail_byuserid(current_user.value?.id!)
    
    // update current_order_detail in store
    current_order_detail.value = last_order_detail as OrderDetail
 
    // create order items for the order detail
    list_cart_item.value.forEach(async (element:CartItem) => {
            await create_order_item({
                "album_id": element.album_id,
                "created_date": new Date(),
                "order_detail_id": last_order_detail.id!,
                "qty": element.qty
            })
        })
    

    }
    

   let step = ref(0)
   // move forward
   const next_step = ((step_id:number) => {
        switch(step_id){
            case 1:
                console.log('passer la commande')
                // create order detail and order items
                create_order_detail_order_items()
                break;
            case 2:
                // create delivery address

                console.log('choisir adresse de livraison et de facturation ??')
                break;
            case 3:
                // confirm payement
                
                // update payement status
                console.log('choisir carte de paiement ??')
                break;
        }
            
        step.value = step.value + 1;
   })

   //move backward
   const prev_step = (() => {
        step.value--;
   })
   console.log('step here: ',step.value)
   // on change quanty of products , change total price
   const handleChange = (() => {
        let total_somme = 0
        list_album.value.forEach((element)=> {
            
            // iterate through list cart item
            list_cart_item.value.forEach((my_cart:CartItem) => {
                if (element.id == my_cart.album_id) {
                    total_somme+= element.price * my_cart.qty
                }
            })
            
        })
        total_price.value = total_somme
        console.log("here total: ",total_price.value)
        return total_price.value
    })
   
   
   </script>

<template>
<div class="multistep_container">
    <div>
        <div v-if="step === 0">
            <div class="container py-5">
                <h2>Liste des produits</h2>
                <div class="row d-flex justify-content-center my-2">
                    <Liste_Commandes
                        />
                    <div class="col-md-4">
                        <div class="card mb-4">
                            <div class="card-header py-3">
                                <h5 class="mb-0">Récapitulatif</h5>
                            </div>
                            <div class="card-body">
                                <ul class="list-group list-group-flush">
                                <li
                                    class="list-group-item d-flex justify-content-between align-items-center border-0 px-0 pb-0">
                                    Produits
                                    <span>$ {{ handleChange()}}</span>
                                </li>
                                <li class="list-group-item d-flex justify-content-between align-items-center px-0">
                                    Autre frais
                                    <span>Gratuit</span>
                                    
                                </li>
                                <li
                                    class="list-group-item d-flex justify-content-between align-items-center border-0 px-0 mb-3">
                                    <div>
                                    <strong>Total </strong>
                                    <strong>
                                        <p class="mb-0">(en incluant le TVA)</p>
                                    </strong>
                                    </div>
                                    <span><strong>$ {{ handleChange()}}</strong></span>
                                </li>
                                </ul>

                                <button type="button" class="btn btn-outline-warning btn-lg" @click="next_step(1)">
                                    Passer la commande
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="step === 1">
            <Livraison
                    />
            <div class="container d-flex justify-content-center my-2">
                <button class="btn btn-secondary" @click="prev_step">
                    Prev
                </button>
                &nbsp;&nbsp;
                <button class="btn btn-outline-warning" @click="next_step(2)">
                    Suivant
                </button>
            </div>
        </div>
        <div v-if="step === 2">
            <Paiement
                    />
            <div class="col-12 text-center">
                <button class="btn btn-secondary" @click="prev_step">
                    Prev
                </button>
                &nbsp;&nbsp;
                <button class="btn btn-outline-warning" @click="next_step(3)">
                    Suivant
                </button>
            </div>
        </div>
        <div v-if="step === 3">
            <div class="container">
                <h2 class="text-center pt-4">
                    <P>Bravo vous avez terminée votre commande. Allez sur le site du transporteur</P>
                    <font-awesome-icon icon="fa-solid fa-circle-check" size="lg" :style="{ color: '#d35400' }"/>

                </h2>
            </div>
            <div class="container d-flex justify-content-center my-2">
                <button class="btn btn-secondary" @click="prev_step">
                    Prev
                </button>
            </div>
        </div>

    </div>
  </div>
</template>
