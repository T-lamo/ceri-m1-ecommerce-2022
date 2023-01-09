<script lang="ts" setup>
    import SearchOneAlbum from './SearchOneAlbum.vue';
    import type { Album } from '@/models';

    const props = defineProps<{
        searchItems: Album[]
    }>()

    
</script>

<template>
    <div class="container-fluid">
        <ul class="dropdown-menu dropdown-menu-dark text-small shadow" aria-labelledby="dropdownUser1">
            <li>
                <p>hello</p>
                <!-- <a class="dropdown-item" href="#">
                    <SearchOneAlbum
                        v-for="item in props.searchItems"
                        :key="item.id"
                        :item=item
                            />
                </a> -->
            </li>
            <li>
                <p>Goodbye</p>
            </li>
        </ul>
        
    </div>
</template>