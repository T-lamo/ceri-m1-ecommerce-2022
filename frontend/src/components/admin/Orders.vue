<script lang="ts" setup>
    import { useAppStore } from '@/stores';
    import { storeToRefs } from 'pinia';
    import { read_order_details , read_users, read_order_items_by_orderdetail_id, read_albums, update_order_detail} from '@/services/crud';
    import { onMounted, ref } from 'vue';
    import { Album, type OrderDetail,type User,OrderItem } from '@/models';

    let choose_me_edit_or_show = ref(true)
    let chosen_order_items = ref<OrderItem[]>()
    let chosen_order_detail = ref<OrderDetail>()

    const { list_order_detail, list_user , list_album} = storeToRefs(useAppStore())
    
    const get_order_details = async () => {
        let list_order_details = await read_order_details()
        list_order_detail.value =  list_order_details as OrderDetail[]
        console.log(list_order_detail.value)
    }

    const read_all_albums = async() => {
        list_album.value = await read_albums() as Album[]
    }
    // fill list_user store to users in db
    const get_user_detail = async () => {
        list_user.value = await read_users() as User[]
        // console.log("list user: ")
        // console.log(list_user.value)
    }
    onMounted(() => {
        read_all_albums()
        get_order_details()
        get_user_detail()
    })
    // return name of user by id_user

    const get_name_user = (id_user:number):string => {
        let fullname = ""
        list_user.value.forEach(element => {
            if (element.id == id_user) {
                fullname = element.firstname +" "+element.username
            }
        });

        return fullname
    }

    // display infos
    const display_info = async (order_detail:OrderDetail) => {
        choose_me_edit_or_show.value = true
        chosen_order_detail.value= order_detail
        // console.log("id order: ",order_detail.id)
        let orders_items = await read_order_items_by_orderdetail_id(order_detail.id!)
        // orders_items.forEach(element => {
        //     chosen_order_items.value!.push(element)
        // });
        chosen_order_items.value! = orders_items
        // chosen_order_items.value = orders_items
        // console.log('corresponding order items: ')
        // console.log(chosen_order_items.value)
        // return orders_items
    }

     // get image source
     const getImage = (imagePath:string) => {
        return (imagePath);
    }

    // check me album
    const check_me_album = (id_album:number) => {
        let my_selected_album = new Album;
        list_album.value.forEach((element:Album) => {
            if (element.id == id_album) {
                my_selected_album = element
            }
        })
        // console.log(my_selected_album)
        return my_selected_album
    }
    // reactive values to update
    const comment_status = ref("")
    const checked_delivery_status = ref(false)
    const checked_payment_status = ref(false)
    const checked_send_status = ref(false)

    // click button edit order details
    const edit_order_details = (order_detail:OrderDetail)=> {
        chosen_order_detail.value= order_detail
        checked_delivery_status.value = order_detail.delivery_status
        checked_payment_status.value = order_detail.payment_status
        checked_send_status.value = order_detail.send_status
        choose_me_edit_or_show.value = false
        comment_status.value = order_detail.orders_status
        

    }

    //update an order detail
    const onUpdateOrderDetail = async () => {
        console.log("update values: ")
        console.log("comments: ",comment_status.value)
        // chosen_order_detail.value?.orders_status = comment_status.value
        console.log("delivery_status: ",checked_delivery_status.value)
        console.log("payment_status: ",checked_payment_status.value)
        let res = await update_order_detail({
            "id": chosen_order_detail.value?.id,
            "created_date": new Date(),
            "delivery_status": checked_delivery_status.value,
            "payment_status": checked_payment_status.value,
            "orders_status": comment_status.value,
            "send_status": checked_send_status.value,
            "total": chosen_order_detail.value?.total!,
            "user_id": chosen_order_detail.value?.user_id!
        })
        .then(res => console.log("update successfull"))
        .catch(error => console.log(error))
        // update order_detail
        get_order_details()
        

        
    }

    
</script>

<template>
    <div class="container-fluid pt-4">
        <div class="row d-flex ">
            <!-- list all order details -->
            <div class="col-md-8 justify-content-start">
                <p class="text-center">Orders </p>
                <div class="table-responsive">
                    <table class="table table-striped text-center">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Name</th>
                                <th>Total ($)</th>
                                <th>Delivered</th>
                                <th>Paid</th>
                                <th>Sent</th>
                                <th>Comments</th>
                                <th>Date</th>
                                <th></th>
                            </tr>
                        </thead>

                        <tbody class="table-group-divider">
                            <tr v-for="order_item_detail in list_order_detail">
                                <th scope="row">{{order_item_detail.id}}</th>
                                <td>{{get_name_user(order_item_detail.user_id)}}</td>
                                <td>{{order_item_detail.total}}</td>
                                <td v-if="order_item_detail.delivery_status">
                                    <font-awesome-icon icon="fa-solid fa-check" size="lg" :style="{ color: '#27ae60' }"/>
                                </td>
                                <td v-else>
                                    <font-awesome-icon icon="fa-solid fa-x" size="lg" :style="{ color: '#c0392b' }"/>
                                </td>
                                <td v-if="order_item_detail.payment_status">
                                    <font-awesome-icon icon="fa-solid fa-check" size="lg" :style="{ color: '#27ae60'}"/>
                                </td>
                                <td v-else>
                                    <font-awesome-icon icon="fa-solid fa-x" size="lg" :style="{ color: '#c0392b' }"/>
                                </td>
                                <td v-if="order_item_detail.send_status">
                                    <font-awesome-icon icon="fa-solid fa-check" size="lg" :style="{ color: '#27ae60'}"/>
                                </td>
        
                                <td v-else>
                                    <font-awesome-icon icon="fa-solid fa-x" size="lg" :style="{ color: '#c0392b' }"/>
                                </td>
                                <td>{{order_item_detail.orders_status}}</td>
                                <td>{{order_item_detail.created_date}}</td>
                                <td>
                                    <button @click="display_info(order_item_detail)">
                                        <font-awesome-icon icon="fa-solid fa-eye" :style="{ color: '#e17055'}"/> 
                                    </button>&nbsp;
                                    <button @click="edit_order_details(order_item_detail)">
                                        <font-awesome-icon icon="fa-solid fa-edit" :style="{ color: '#2980b9'}"/>
                                    </button>
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
            <!-- list my corresponding order items -->
            <div class="col-md-4 justify-content-end" v-if="choose_me_edit_or_show" >
                <h5 class="text-center">Recap</h5>
                <div class="card">
                    <div class="card-header text-center">
                        Order # {{chosen_order_detail?.id}}
                    </div>
                        <div class="card-body">
                                <div class="table-responsive">
                                    <table class="table-striped">
                                        <thead>
                                            <tr>
                                                <th>#</th>
                                                <th>Cover</th>
                                                <th>Title</th>
                                                <th>Quantity</th>
                                            
                                                <!-- <th>Date</th> -->
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="item in chosen_order_items">
                                                <th>{{item.id}}</th>
                                                <td>
                                                    <img
                                                        :src=getImage((check_me_album(item.album_id)).cover!)
                                                        style="height:80px; width:120px;"
                                                        class="img-fluid rounded-3" alt="Cotton T-shirt">
                                                    <p></p>
                                                </td>
                                                <td>{{(check_me_album(item.album_id)).title}}</td>
                                                <td>{{item.qty}}</td>
                                            
                                                <!-- <td>{{item.created_date}}</td> -->
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                        </div>    
                </div>
            </div>
            <div class="col-md-4 justify-content-end" v-else>
                <div class="card">
                    <div class="card-header text-center">
                        <h5>Update order # {{ chosen_order_detail?.id }} </h5>
                    </div>
                    <div class="card-body">
                       
                            <!-- comments and status of the order detail -->
                            <div class="mb-3">
                                <label for="status_label" class="form-label">Comment (status)</label>
                                <input type="text" class="form-control" v-model="comment_status">
                                <!-- <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div> -->
                            </div>
                            <div class="mb-3 form-check">
                                <input type="checkbox" class="form-check-input" id="exampleCheck2" v-model="checked_payment_status"> <!--="chosen_order_detail?.payment_status"-->
                                <label class="form-check-label" for="exampleCheck2">Paid</label>
                            </div>
                            <div class="mb-3 form-check">
                                <input type="checkbox" class="form-check-input" id="exampleCheck1" v-model="checked_send_status"> <!-- :checked="chosen_order_detail?.delivery_status" -->
                                <label class="form-check-label" for="exampleCheck1">Sent</label>
                            </div>
                            <div class="mb-3 form-check">
                                <input type="checkbox" class="form-check-input" id="exampleCheck1" v-model="checked_delivery_status"> <!-- :checked="chosen_order_detail?.delivery_status" -->
                                <label class="form-check-label" for="exampleCheck1">Delivered</label>
                            </div>
                            <div class="text-center pt-1 mb-5 pb-1">
                                <button class="auth-btn btn btn-outline-warning btn-block" type="submit" @click="onUpdateOrderDetail"> <!--@click="addUser()"-->
                                    Update
                                </button>
                              </div>
                            
                    </div>
                </div>
            </div>

            <!-- edit my order detail-->
        </div>

    </div>
    
</template>
<style scoped>
.table {
    cursor: pointer;
}
</style>