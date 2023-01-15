<script lang="ts" setup>
    import { useAppStore } from '@/stores';
    import { storeToRefs } from 'pinia';
    import { read_users } from '@/services/crud';
    import { onMounted } from 'vue';
    import type { User } from '@/models';

    const { list_user } = storeToRefs(useAppStore())
    
    onMounted(async () => {
        list_user.value = await read_users() as User[]
    })
   

</script>
<template>
    <div class="container-fluid pt-4">
        <div class="row d-flex ">
                <p class="text-center">Curstomers </p>
                <div class="table-responsive">
                    <table class="table table-striped text-center">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Firstname</th>
                                <th>Username</th>
                                <th>Email</th>
                                <th>Telephone</th>
                                <th>Admin</th>
                            </tr>
                        </thead>

                        <tbody class="table-group-divider">
                            <tr v-for="item in list_user">
                                <th scope="row">{{item.id}}</th>
                                <td>{{item.firstname}}</td>
                                <td>{{item.username}}</td>
                                <td>{{item.email}}</td>
                                <td>{{item.telephone}}</td>
                                <td v-if="item.is_admin">
                                    <font-awesome-icon icon="fa-solid fa-check" size="lg" :style="{ color: '#27ae60' }"/>
                                </td>
                                <td v-else>

                                </td>
                            </tr>
                        </tbody>
                        <tfoot>
                            <td>    
                                <p>1 of 1 entries</p>
                            </td>
                            <td></td>
                            <td></td>
                            <td>
                                <button>Prev</button>
                            </td>
                            <td>
                                <button>4</button>
                            </td>
                            <td>
                                <button>Next</button>
                            </td>
                            <td></td>
                            <td></td>
                        </tfoot>
        
                    </table>
                </div>
            </div>
    </div>
</template>