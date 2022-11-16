<script lang="ts">
export default {
  data() {
    return {
      promo_text: "10$ offers sur les 3 premiers vinyls achetes"
    }
  }
}
</script>

<template>
   <div class="promo">
    <span>
        <i>{{promo_text}}</i>
    </span>
   </div>     
</template>
<style scoped>
.promo {
    background-color: #c23616;
    float: center;
    text-align: center;
    color: aliceblue;
}

</style>