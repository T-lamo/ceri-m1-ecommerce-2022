<script lang="ts" setup>
    import OneCommand from './OneCommand.vue'
    import { computed, ref } from "vue"
    import { read_one_album, toast_function } from '@/services/crud';
    import { useAppStore } from '@/stores';
    import { storeToRefs } from 'pinia';

    const {list_cart_item, last_shopping_session} = storeToRefs(useAppStore())
    console.log("last_shopping_session: ")
    console.log(last_shopping_session.value)
    
    
</script>

<template>
            <div class="col-md-8">
                <div class="card mb-4">
                    <div class="card-header">
                        Liste des commandes
                    </div>
                    <OneCommand
                        v-for="item in list_cart_item" :key="item.id"
                        :item=item
                        />
                    
                </div>
            </div>

</template>
