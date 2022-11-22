<script lang="ts" setup>
    import { ref } from "vue"
</script>
<template>
<div>
    <!-- First item -->
    <div class="card rounded-3 mb-4">
          <div class="card-body p-4">
            <div class="row d-flex justify-content-between align-items-center">
              <div class="col-md-2 col-lg-2 col-xl-2">
                <img
                  src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4bUXItViL4G-uiUzFZojy78OZhBGb5K8i5w&usqp=CAU"
                  class="img-fluid rounded-3" alt="Cotton T-shirt">
              </div>
              <div class="col-md-3 col-lg-3 col-xl-3">
                <p class="lead fw-normal mb-2">Bike</p>
                <p><span class="text-muted">Size: </span>M <span class="text-muted">Color: </span>Grey</p>
              </div>
              <div class="col-md-3 col-lg-3 col-xl-2 d-flex">
                <button class="btn btn-link px-2"
                  onclick="this.parentNode.querySelector('input[type=number]').stepDown()">
                  <i class="fas fa-minus"></i>
                </button>

                <input id="form1" min="0" name="quantity" value="1" type="number"
                  class="form-control form-control-sm"/>

                <button class="btn btn-link px-2"
                  onclick="this.parentNode.querySelector('input[type=number]').stepUp()">
                  <i class="fas fa-plus"></i>
                </button>
              </div>
              <div class="col-md-3 col-lg-2 col-xl-2 offset-lg-1">
                <h5 class="mb-0">$499.00</h5>
              </div>
              <div class="col-md-1 col-lg-1 col-xl-1 text-end">
                <a href="#!" class="text-danger"><i class="fas fa-trash fa-lg"></i></a>
              </div>
            </div>
            <div class="text-end">
            <!-- <a href="#!" class="text-danger"><i class="fas fa-trash fa-lg"></i></a> -->
                <router-link to="/list_album_achat">    
                    <font-awesome-icon icon="fa-solid fa-edit" size="lg" :style="{ color: '#1B1464' }"/>
                </router-link> &nbsp;&nbsp;
                <router-link to="/list_album_achat">    
                    <font-awesome-icon icon="fa-solid fa-trash" size="lg" :style="{ color: 'red' }"/>
                </router-link>
            </div>
        </div>
          
    </div>
</div>
        
</template>