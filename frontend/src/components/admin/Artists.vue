<script lang="ts" setup>
    import { useAppStore } from '@/stores';
    import { storeToRefs } from 'pinia';
    import { onMounted, ref } from 'vue';
    import { read_artists, read_albums, read_categories, update_artist, toast_function, create_artist} from '@/services/crud';
    import type { Album, Artist, Category } from '@/models';
    import Datepicker from '@vuepic/vue-datepicker';
    import '@vuepic/vue-datepicker/dist/main.css';
    
    // display edit forms or list of albums
    let display_info_or_edit = ref(false)
    let title_edit_or_add = ref("")
    let title_update_or_add = ref("")
    let id_choose = ref(0)

    // artist clicked by a button to edit or to show
    let chosen_artist = ref<Artist>()

    const { list_artist, list_album , list_category} = storeToRefs(useAppStore())

    // initialize list of album, category and artist in the store
    const onLoad = (async () => {
        list_artist.value = await read_artists() as Artist[]
        list_album.value = await read_albums() as Album []
        list_category.value = await read_categories() as Category []
    })

    onMounted(() => {
        onLoad()
    })

    // check correponding albums for an id_artist
    const check_me_album_by_artist = (id_artist:number):Album[] => {
        let corres_list_albums = Array<Album>()

        list_album.value.forEach((element) => {
            if (element.artist_id == id_artist)
                corres_list_albums.push(element)
        })

        return corres_list_albums

    }
    // check category name for an id-category
    const ckeck_me_category = (id_ca:number):string => {
        let cat_name = ""
        list_category.value.forEach((element) => {
            if (element.id == id_ca)
                cat_name = element.label
        })
        return cat_name
    }

    // default values for artist
    let firstname = ref("")
    let lastname = ref("")
    let cover = ref("")
    let date_of_birth = ref("" + (new Date()).toString())

    //on click edit button
    const edit_artist = (artist:Artist) => {
        id_choose.value = 1
        title_update_or_add.value = "Update artist"
        title_edit_or_add.value = "Edit artist # "+artist.id
        display_info_or_edit.value = false;
        chosen_artist.value = artist
        firstname.value = artist.firstname
        lastname.value = artist.lastname
        cover.value = artist.cover!
        date_of_birth.value = "" + artist.date_of_birth?.toString()
    }

    // update artist
    const onUpdateAddArtist = async() => {
           
        if (id_choose.value == 1) { // update

            let res = await update_artist({
            "id": chosen_artist.value?.id,
            "cover": cover.value,
            "firstname": firstname.value,
            "lastname": lastname.value,
            "date_of_birth": "" + date_of_birth.value,
            "created_date": new Date()
            // "list_album": chosen_artist.value?.list_album
           })
           .then( res => 
                toast_function("Artist " + chosen_artist.value?.firstname + " successfully updated", "success")
           )
           .catch(
            error => 
                toast_function("Artist" + chosen_artist.value?.firstname + " failed to be updated","error")
           )

        } else {
            let res = await create_artist({
                "id": chosen_artist.value?.id,
                "cover": cover.value,
                "firstname": firstname.value,
                "lastname": lastname.value,
                "date_of_birth": "" + date_of_birth.value,
                "created_date": new Date()
            })
            .then( res => 
                toast_function("Artist created successfully ", "success")
           )
           .catch(
            error => 
                toast_function("Artist failed to be created","error")
           )
        }
        
           onLoad()
    }

    // add an artist
    const onClickAddArtist_btn = () => {
        title_update_or_add.value = "Create"
        title_edit_or_add.value = "# Create a new artist"
        display_info_or_edit.value = false;
        firstname.value = ""
        lastname.value = ""
        cover.value = ""
        date_of_birth.value = (new Date()).toString()

    }
    
</script>
<template>
    <div class="container-fluid pt-4">
        <button class="btn btn-outline-warning" @click="onClickAddArtist_btn">Add artist</button>
        <div class="row d-flex">
            
            <!-- list of artist -->
            <div class="col-md-6">
                <div class="table-responsive">
                    <table class="table table-striped text-center">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Cover</th>
                                <th>Name</th>
                                <th> </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="item in list_artist">
                                <th>#{{item.id}}</th>
                                <td>
                                    <img :src="item.cover"
                                    style="height:80px; width:120px;"
                                    class="img-fluid rounded-3" alt="Cotton T-shirt"
                                    />
                                </td>
                                <td>
                                    {{item.firstname}} {{item.lastname}} <br>
                                     <center>born in</center> <br>
                                     <i>{{item.date_of_birth}}</i> </td>
                                <td>
                                    <button @click="display_info_or_edit = true;chosen_artist = item;">
                                        <font-awesome-icon icon="fa-solid fa-eye" :style="{ color: '#e17055'}"/> 
                                    </button>&nbsp;
                                    <button  @click="edit_artist(item)">
                                        <font-awesome-icon icon="fa-solid fa-edit" :style="{ color: '#2980b9'}"/>
                                    </button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <!-- corresponding list of albums -->
            <div class="col-md-6" v-if="display_info_or_edit">
                <div class="table-responsive text-center">
                    <div class="card">
                        <div class="card-header">
                            Albums for artitst # {{chosen_artist?.id }}
                        </div>

                        <table class="table table-striped">
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Cover</th>
                                    <th>title</th>
                                    <th>Description</th>
                                    <th></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="item in check_me_album_by_artist(chosen_artist?.id!)">
                                    <th># {{item.id}} </th>
                                    <td>
                                        <img :src="item.cover"
                                            style="height:80px; width:120px;"
                                            class="img-fluid rounded-3" alt="Cotton T-shirt"
                                            />
                                        <p>Category: <b>{{ckeck_me_category(item.category_id)}}</b></p>
                                    </td>
                                    <td>
                                        <center>{{item.title}}</center> 
                                        <br>
                                        <center>released in </center>
                                        <i>{{item.release_date}}</i>
                                    </td>
                                    <td>{{item.description}}</td>
                                    <!-- <td>{{ckeck_me_category(item.category_id)}}</td> -->
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- display edit or add form -->
            <div class="col-md-6 pt-2" v-else>
                <div class="card text-center">
                    <div class="card-header">
                        {{title_edit_or_add}}
                    </div>
                    <div class="card-body">
                            <!-- input firstname -->
                            <div class="form-floating mb-3">
                                <input type="text" class="form-control" v-model="firstname" id="firstname_float"/>
                                <label for="firstname_float">Firstname</label>
                            </div>

                            <!-- input lastname -->
                            <div class="form-floating mb-3">
                                <input type="text" class="form-control" v-model="lastname" id="lastname_float"/>
                                <label for="lastname_float">Lastname</label>
                            </div>

                            <!-- input cover url -->
                            <div class="form-floating mb-3">
                                <textarea class="form-control" v-model="cover" id="cover_float" style="height: 150px"></textarea>
                                <label for="cover_float">Cover url</label>
                            </div>

                            <!-- input date of birth  -->
                            <div class="form-control mb-3">
                                <label for="dateofbirth_float"> Date of birth </label>
                                <Datepicker v-model="date_of_birth" id="dateofbirth_float"/>
                            </div>

                            <div class="text-center pt-1 mb-5 pb-1">
                                <button  class="btn btn-outline-warning btn-block" @click="onUpdateAddArtist()">
                                    {{title_update_or_add}}
                                </button>
                            </div>
                            
                        <!-- </form> -->
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>