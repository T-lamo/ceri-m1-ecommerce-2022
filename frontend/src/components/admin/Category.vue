<script lang="ts" setup>
    import { useAppStore } from '@/stores';
    import { storeToRefs } from 'pinia';
    import { onMounted, ref } from 'vue';
    import { read_categories, create_category, update_category, toast_function} from '@/services/crud';
    import type { Category } from '@/models';

    let show = ref(false)
    let title_edit_or_add = ref("")
    let title_update_or_add =ref("")
    let chosen_cat = ref<Category>()
    let id_choose = ref(0)

    const { list_category } = storeToRefs(useAppStore())

    const onLoad = async () => {
        list_category.value = await read_categories() as Category[]
    }

    onMounted(() => {
        onLoad()
    })

    // input value 
    let label_cat = ref ("")

    // on click button add category
    const onClickAddCat_btn = () => {
        id_choose.value = 2
        label_cat.value = ""
        title_update_or_add.value = "Create"
        show.value = true
    }

    // on click button edit category
    const edit_category = (item:Category) => {
        chosen_cat.value = item
        id_choose.value = 1
        label_cat.value = item.label
        title_update_or_add.value = "Update"
        show.value = true
    }
    // add or update category
    const onUpdateAddCat = async () => {
        // update category
        if (id_choose.value == 1) {
            let res = await update_category({
                "id": chosen_cat.value?.id,
                "label": label_cat.value,
                "created_date": new Date()
            })
                .then( 
                    res => 
                        toast_function("Category "+ chosen_cat.value?.id+" updated successfully ", "success")
                )
                .catch(
                        error => 
                            toast_function("Category "+chosen_cat.value?.id+" failed to be updated","error")
                    )
                
        } 
        // add a new category
        else {
            let res = await create_category({
                "label": label_cat.value,
                "created_date": new Date()
            })
            .then( 
                res => 
                    toast_function("Category created successfully ", "success")
            )
           .catch(
                error => 
                    toast_function("Category failed to be created","error")
            )

        }

        onLoad()
    }

</script>
<template>
    <div class="container-fluid pt-4">
        <button class="btn btn-outline-warning" @click="onClickAddCat_btn">Add Category</button>
        <div class="row d-flex">
            <!-- list of categories -->
            <div class="col-md-6">
                <div class="table-responsive">
                    <table class="table table-striped text-center">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Label</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item in list_category">
                                <th>#</th>
                                <td>{{item.label}}</td>
                                <td>
                                    <button  @click="edit_category(item)">
                                        <font-awesome-icon icon="fa-solid fa-edit" :style="{ color: '#2980b9'}"/>
                                    </button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="col-md-6" v-if="show">
                <div class="card text-center">
                    <div class="card-header">
                        Category # {{ chosen_cat?.id}}
                    </div>
                    <div class="card-body">
                        <!-- input firstname -->
                        <div class="form-floating mb-3">
                            <input type="text" class="form-control" v-model="label_cat" id="label_cat_float"/>
                            <label for="label_cat_float">Label</label>
                        </div>

                        <div class="text-center pt-1 mb-5 pb-1">
                            <button  class="btn btn-outline-warning btn-block" @click="onUpdateAddCat()">
                                {{title_update_or_add}}
                            </button>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>