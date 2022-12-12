<script lang="ts" setup>
   import Liste_Commandes from './Liste_Commandes.vue';
   import Paiement from './Paiement.vue';
   import Livraison from './Livraison.vue'
   import { ref } from "vue"
   import { useAppStore } from '@/stores';
   import { storeToRefs } from 'pinia';

   const {list_cart_item} = storeToRefs(useAppStore())
   let total_somme = 0
   let price = 1
   list_cart_item.value.forEach((element) => {
        total_somme +=element.qty*price
   })
    
   let step = ref(0)
   const next_step = (() => {
        step.value = step.value + 1;
   })
   const prev_step = (() => {
        step.value--;
   })
   let my_step = step.value

</script>

<template>
<div class="multistep_container">
    <div>
        <div v-if="step === 0">
            <div class="container py-5">
                <h2>Liste des produits</h2>
                <div class="row d-flex justify-content-center my-2">
                    <div class="col-md-8">
                        <div class="card mb-4">
                            <div class="card-header">
                                Liste des commandes
                            </div>
                            
                        </div>
                    </div>
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
                                    <span>$ {{ total_somme}}</span>
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
                                    <span><strong>$ {{ total_somme}}</strong></span>
                                </li>
                                </ul>

                                <button type="button" class="btn btn-outline-warning btn-lg" @click="next_step">
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
                <button class="btn btn-outline-warning" @click="next_step">
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
                <button class="btn btn-outline-warning" @click="next_step">
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

      <!-- </Wizard> -->
    </div>
  </div>
</template>

<style>
/* .multistep_container{
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
} */
</style>
