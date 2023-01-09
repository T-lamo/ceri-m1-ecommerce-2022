<script lang="ts" setup>
    import { storeToRefs } from 'pinia'
    import { read_artists } from '../../services/crud'
    import { useAppStore } from '../../stores';
    import { onMounted } from 'vue';
    import OneArtistDetail from './OneArtistDetail.vue';

    const { list_artist } = storeToRefs(useAppStore())
    onMounted(async() => {
        list_artist.value = (await read_artists()).map((res:any) => {
            return res;
        })
    })

</script>

<template>
    <div class="container-fluid py-2 px-5 my-3 text-center">
        <span><i>List of singers</i></span>
        <hr class="dropdown-divider">
        <div class="row">
            <OneArtistDetail
                v-for="item in list_artist" :key="item.id"
                :item = item
                />
        </div>
    </div>
</template>
