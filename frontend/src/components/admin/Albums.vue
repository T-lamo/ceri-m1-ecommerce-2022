
<script lang="ts" setup>

    import { useAppStore } from '@/stores';
    import { storeToRefs } from 'pinia';
    import { onMounted, ref } from 'vue';
    import { read_albums, read_categories, read_artists, create_album,
    read_song_by_albumid,update_album, toast_function, delete_album} from '@/services/crud';
    import type { Album, Artist, Category, Song } from '@/models';
    import Datepicker from '@vuepic/vue-datepicker';
    import '@vuepic/vue-datepicker/dist/main.css';
    import Swal from 'sweetalert2'

    // variables
    let display_edit = ref(false)
    let display_list_song = ref(false)
    let chosen_album = ref<Album>()
    let title_edit_or_add = ref("")
    let title_update_or_add = ref("")
    let id_choose = ref(0)
    let arr_songs = ref<Song[]>([])

    const { list_album,list_category, list_artist} = storeToRefs(useAppStore())

    // initialize list album, category, artist 
    const onLoad = async () => {
        list_album.value = await read_albums() as Album[]
        list_category.value = await read_categories() as Category[]
        list_artist.value = await read_artists() as Artist[]
    }
    onMounted( () => {
        onLoad()
    })

    // check category name by id_category
    const ckeck_me_category = (id_ca:number):string => {
        let cat_name = ""
        list_category.value.forEach((element) => {
            if (element.id == id_ca)
                cat_name = element.label
        })
        return cat_name
    }

    // check artist name by id_artist
    const check_me_artist = (id_artist:number):string => {
        let artist_name = ""
        list_artist.value.forEach((element) => {
            if (element.id == id_artist)
                artist_name = element.firstname+" "+element.lastname
        })
        return artist_name
    }

    // default values of album
    let title = ref("")
    let release_date = ref(""+(new Date()).toString())
    let cover = ref("")
    let artist_id = ref(0)
    let price = ref(0)
    let stock_qty = ref(0)
    let description = ref("")
    let category_id = ref(0)

    // click edit button
    const onCLickEdit = (item:Album) => {
        id_choose.value = 1
        chosen_album.value = item
        display_edit.value = true
        display_list_song.value = false
        title_edit_or_add.value = 'Edit'
        title_update_or_add.value = 'Update'
        // update local stores
        title.value = item.title
        release_date.value = item.release_date
        cover.value = item.cover!
        artist_id.value = item.artist_id
        price.value = item.price
        stock_qty.value = item.stock_qty
        description.value = item.description
        category_id.value = item.category_id

    }

    const onCLickShowSongs = async (item:Album) => {
        display_list_song.value = true
        arr_songs.value =  await read_song_by_albumid(item.id!)

    }

    // add a new album
    const onCLickAdd = () => {
        id_choose.value = 2
        display_edit.value = true
        display_list_song.value =false
        title_edit_or_add.value = 'Add an album'
        title_update_or_add.value = 'Create'
        // update local stores
        title.value = ""
        release_date.value = (new Date()).toString()
        cover.value = ""
        artist_id.value = 1
        price.value = 0
        stock_qty.value = 0
        description.value = ""
        category_id.value = 1
    }

    // update selected album
    const onUpdateAddAlbum = async () => {
        if (id_choose.value == 1 ) {
            let res = await update_album({
                "id" : chosen_album.value?.id,
                "artist_id" : artist_id.value,
                "category_id": category_id.value,
                "cover": cover.value,
                "description": description.value,
                "price": price.value,
                "stock_qty": stock_qty.value,
                "title": title.value,
                "release_date": "" + release_date.value.toString(),
                "created_date": new Date()
            })
            .then(res => 
                toast_function("Successfully update album #"+ chosen_album.value?.id +"","success")
            )
            .catch(error => 
                toast_function("Failed to update " + chosen_album.value?.id+ "","error")
            )
            
        } 
        else {
            let res = await create_album({
                "artist_id" : artist_id.value,
                "category_id": category_id.value,
                "cover": cover.value,
                "description": description.value,
                "price": price.value,
                "stock_qty": stock_qty.value,
                "title": title.value,
                "release_date": "" + release_date.value,
                "created_date": new Date()
            })
            .then(res => 
                toast_function("Successfully new album added","success")
            )
            .catch(error => 
                console.log(error)
            )
            
        }

        onLoad()

    }

    // delete selected album
    const onDeleteAlbum = (id_album:number) => {
        Swal.fire({
            title:'Are you sure ?',
            text: "This action is final ",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it !'

        }).then(async (result) => {
            if (result.isConfirmed) {
                Swal.fire(
                        'Deleted!',
                        'Album '+ id_album+' has been deleted!',
                        'success'
                    )
                let res = await delete_album(id_album)
            }
        })

        onLoad()
    }
       

    
</script>
<template>
    <div class="container-fluid pt-4">
        <button class="btn btn-outline-warning" @click="onCLickAdd">Add album</button>
        <div class="row d-flex ">
                <div class="col-md-8">
                    <div class="table-responsive">
                        <table class="table table-striped text-center">
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Cover</th>
                                    <th>title</th>
                                    <th>Stock</th>
                                    <th>Description</th>
                                    <th>Aritst</th>
                                    <th></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="item in list_album">
                                    <th>#{{item.id}}</th>
                                    <td>
                                        <img :src="item.cover"
                                            style="height:80px; width:120px;"
                                            class="img-fluid rounded-3" alt="Cotton T-shirt"
                                            />
                                        Category: <br>
                                        <b>{{ckeck_me_category(item.category_id!)}}</b> <br>
                                        Price: <br>
                                        <b>$ {{item.price}}</b>
                                    </td>
                                    <td>
                                        {{item.title}} <br>
                                        <center>released in: </center>
                                        <i>{{item.release_date}}</i>
                                
                                    </td>
                                    <td>{{item.stock_qty}}</td>
                                    <td>{{item.description}}</td>
                                    <td>{{check_me_artist(item.artist_id)}}</td>
                                    <td>
                                        <button @click="onDeleteAlbum(item.id!)">
                                            <font-awesome-icon icon="fa-solid fa-trash" :style="{ color: '#e17055'}"/> 
                                        </button>&nbsp;
                                        <button @click="onCLickEdit(item) ">
                                            <font-awesome-icon icon="fa-solid fa-edit" :style="{ color: '#2980b9'}" />
                                        </button>
                                        <button @click="onCLickShowSongs(item) ">
                                            <font-awesome-icon icon="fa-solid fa-music" :style="{ color: '#2980b9'}" />
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            <div class="col-md-4" v-if="display_edit">
                <div class="card text-center">
                    <div class="card-header">
                        {{ title_edit_or_add }}
                    </div>

                    <div class="card-body">
                        <!-- input title -->
                        <div class="form-floating mb-3">
                            <input type="text" class="form-control" v-model="title" id="title_float"/>
                            <label for="title_float">Title</label>
                        </div>

                        <!-- input cover  -->
                        <div class="form-floating mb-3">
                            <textarea class="form-control" v-model="cover" id="cover_float" style="height:150px;"/>
                            <label for="cover_float">Cover</label>
                        </div>
                        <!-- input description -->
                        <div class="form-floating mb-3">
                            <textarea  class="form-control" v-model="description" id="desc_float" style="height:150px;"/>
                            <label for="desc_float">Description</label>
                        </div>
                        <!-- input price  -->
                        <div class="form-floating mb-3">
                            <input type="number" class="form-control" v-model="price" id="price_float"/>
                            <label for="price_float">Price ($)</label>
                        </div>
                        <!-- input stock -->
                        <div class="form-floating mb-3">
                            <input type="number" class="form-control" v-model="stock_qty" id="stock_float"/>
                            <label for="stock_float">Stock quantity</label>
                        </div>
                        <!-- input artist id -->
                        <div class="mb-3">
                            <label class="form-label">Artist</label>
                            <select v-model="artist_id" class="form-select" aria-label="Select an artist ">
                                <option disabled value="">Please select one artist</option>
                                <option v-for="option in list_artist" :value="option.id">
                                    {{ option.firstname }} {{ option.lastname }}
                                </option>
                            </select> 
                        </div>
                        <!-- input category id -->
                        <div class="mb-3">
                            <label class="form-label">Category</label>
                            <select v-model="category_id" class="form-select" aria-label="Select a category">
                                <option disabled value="">Please select one category</option>
                                <option v-for="option_cat in list_category" :value="option_cat.id">
                                    {{ option_cat.label }}
                                </option>
                            </select>
                        </div>
                        <!-- input released date -->
                        <div class="mb-3">
                            <label for="release_float" class="form-label">Release date</label>
                            <Datepicker v-model="release_date" id="release_float"/>
                        </div>

                        <div class="text-center pt-1 mb-5 pb-1">
                            <button  class="btn btn-outline-warning btn-block" @click="onUpdateAddAlbum()">
                                {{title_update_or_add}}
                            </button>
                        </div>
                    </div>

                </div>
            </div>

            <div class="col-md-4" v-if="display_list_song">
                <div class="table-responsive">
                    <table class="table table-striped text-center">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Cover</th>
                                <th>title</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item in arr_songs">
                                <th>#{{item.id}}</th>
                                <td>
                                    <img :src="item.cover"
                                        style="height:80px; width:120px;"
                                        class="img-fluid rounded-3" alt="Cotton T-shirt"
                                        />
                                </td>
                                <td>
                                    {{item.title}} <br>
                                    <center>released in: </center>
                                    <i>{{item.release_date}}</i>

                                </td>
                                
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

        </div>
    </div>
</template>