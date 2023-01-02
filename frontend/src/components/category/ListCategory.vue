<script lang='ts' setup>
    import { read_categories } from '../../services/crud'

    import { storeToRefs } from "pinia";
    import { useAppStore } from "../../stores";

    import {onMounted } from "vue"
    const { list_category } = storeToRefs(useAppStore())
    
    onMounted(async () => {
        
        list_category.value = (await read_categories()).map((res:any) => {
            return res;
        })
    })
    // console.log(list_category.value)
    
    
</script>

<template>
    <div class="card_container container-fluid py-2 px-5 my-3">
            <span><i>List des categories</i></span>
            <hr class="dropdown-divider">
        <div class="row"> 
            <div class="card m-3"  style="width: 14rem;" v-for="item in list_category" :key="item.id"><!-- v-for="item in list_category.value" :key="item.id"-->
                <img src="https://cdn.pixabay.com/photo/2020/01/31/19/26/vinyl-4808792_960_720.jpg" class="rounded"/>
                <button>{{item.label}}</button>
            </div> 
        </div>
        
    </div>
</template>
<style scoped>
.card_container button {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    background-color: transparent;
    color: #fff;
    font-size: 16px;
    font-weight: 800;
    padding: 12px 24px;
    border: none;
    cursor: pointer;
    border-radius: 5px;
}

.card_container card img{
    cursor: pointer;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
.card_container  button:hover ,:focus {
    box-shadow: inset 0 0 0 2em  #273c75;
    transition: color .3s;
}
.card_container img:hover, :focus {
    opacity: .9;
}

</style>