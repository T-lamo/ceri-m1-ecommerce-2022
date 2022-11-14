<script lang='ts' setup>
    import type { isTemplateNode } from "@vue/compiler-core";
import { reactive, ref, computed } from "vue"
    let id = 0
    let id_index = 0
    let total_index = 4
    let active_arrow = ref(false)
    const list_category = ref([
        {id: id++, 'name':'Rock'},
        {id: id++, 'name':'Country'},
        {id: id++, 'name':'Rap'},
        {id: id++, 'name':'Classic'},
        {id: id++, 'name':'Rap'},
        // {id: id++, 'name':'Classic'},
    ])
    const list_users = ref([
        {id: id++,'name': "fara",'age': 45,'sexe':'F'},
        {id: id++, 'name': "fara",'age': 45,'sexe':'F'},
        {id: id++, 'name': "fara",'age': 45,'sexe':'F'},
        {id: id++, 'name': "fara",'age': 45,'sexe':'F'},
        {id: id++, 'name': "fara",'age': 45,'sexe':'F'},
        {id: id++, 'name': "fara",'age': 45,'sexe':'F'},
        {id: id++, 'name': "fara",'age': 45,'sexe':'F'},
        {id: id++, 'name': "fara",'age': 45,'sexe':'F'},
        {id: id++, 'name': "fara",'age': 45,'sexe':'F'},
        {id: id++, 'name': "fara",'age': 45,'sexe':'F'},
    ])
    const showelement = () => {
        console.log('test')
    }

    const changeDirection = computed(() => {
        active_arrow.value =! active_arrow.value
        console.log(active_arrow.value)
    })

</script>

<template>
    <div class="card_container container-fluid py-2 px-5 my-3">
            <span><i>List des categories</i></span>
            <hr class="dropdown-divider">
        <div class="row"> 
            <div class="card m-3"  style="width: 14rem;"  v-for="item in list_category" :key="item.id">
                <img src="https://cdn.pixabay.com/photo/2020/01/31/19/26/vinyl-4808792_960_720.jpg" class="rounded"/>
                <button>{{item.name}}</button>
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