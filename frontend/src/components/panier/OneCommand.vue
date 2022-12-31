<script lang="ts" setup>
import { Album, type CartItem } from "@/models";
import { computed, ref } from "vue";
import { defineProps } from "vue";

import { useAppStore } from "@/stores";
import { storeToRefs } from "pinia";

// list of stores used in this section
const { list_promo, list_cart_item, list_album, current_user, total_price } =
  storeToRefs(useAppStore());

// define props
const props = defineProps<{
  item: CartItem;
}>();

// the quantity of product
const qty_cart = ref(1);

const check_me_album = () => {
  let my_selected_album = new Album();
  list_album.value.forEach((element) => {
    if (element.id == props.item.album_id) {
      my_selected_album = element;
    }
  });
  return my_selected_album;
};
// modify quantity of product in store
const handleChange = () => {
  list_cart_item.value.forEach((element) => {
    if (element.album_id == props.item.album_id) {
      element.qty = qty_cart.value;
      console.log("for : ", element.album_id);
      console.log("change qty here: ", element.qty);
    }
  });
};

// get image source
const getImage = (imagePath: string) => {
  return imagePath;
};
</script>

<template>
  <div>
    <!-- First item -->
    <div class="card rounded-3 mb-4">
      <div class="card-body p-4">
        <div class="row d-flex justify-content-between align-items-center">
          <div class="col-md-2 col-lg-2 col-xl-2">
            <img
              :src="getImage(check_me_album().cover!)"
              class="img-fluid rounded-3"
              alt="Cotton T-shirt"
            />
            <p>{{ handleChange() }}</p>
          </div>
          <div class="col-md-3 col-lg-3 col-xl-3">
            <p class="lead fw-normal mb-2">
              {{ check_me_album().title }} {{ props.item.album_id }}
            </p>
            <p>$ {{ check_me_album().price }}</p>
            <!-- <p><span class="text-muted">Size: </span>M <span class="text-muted">Color: </span>Grey</p> -->
          </div>
          <div class="col-md-3 col-lg-3 col-xl-2 d-flex">
            <button
              class="btn btn-link px-2"
              onclick="this.parentNode.querySelector('input[type=number]').stepDown()"
            >
              <i class="fas fa-minus"></i>
            </button>

            <input
              id="form1"
              min="1"
              name="quantity"
              type="number"
              v-model="qty_cart"
              class="form-control form-control-sm"
            />
            <span>{{ qty_cart }}</span>

            <button
              class="btn btn-link px-2"
              onclick="this.parentNode.querySelector('input[type=number]').stepUp()"
            >
              <i class="fas fa-plus"></i>
            </button>
          </div>
          <div class="col-md-3 col-lg-2 col-xl-2 offset-lg-1">
            <h5 class="mb-0">
              <p>{{ check_me_album().price * qty_cart }}</p>
            </h5>
          </div>
          <div class="col-md-1 col-lg-1 col-xl-1 text-end">
            <a href="#!" class="text-danger"
              ><i class="fas fa-trash fa-lg"></i
            ></a>
          </div>
        </div>
        <div class="text-end">
          <!-- <a href="#!" class="text-danger"><i class="fas fa-trash fa-lg"></i></a> -->
          <!-- <router-link to="/list_album_achat">    
                  <font-awesome-icon icon="fa-solid fa-edit" size="lg" :style="{ color: '#1B1464' }"/>
              </router-link> &nbsp;&nbsp; -->
          <router-link to="/list_album_achat">
            <font-awesome-icon
              icon="fa-solid fa-trash"
              size="lg"
              :style="{ color: 'red' }"
            />
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
