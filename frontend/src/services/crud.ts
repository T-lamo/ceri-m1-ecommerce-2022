import type {
  IAlbum,
  IArtist,
  ICartItem,
  ICategory,
  ILogin,
  IOrderDetail,
  IOrderItem,
  IPaymentDetail,
  IPromo,
  IShoppingSession,
  ISong,
  IUser,
  IUserAddress,
} from "@/interfaces";
import { useToast } from "vue-toast-notification";

// const api_url = import.meta.env.VITE_API_URL;
// const api_url = "http://localhost:80";

// console.log("api url", api_url);
const content_type = {
  "Content-Type": "application/json",
};

export async function read_artists(): Promise<IArtist[]> {
  return await (await fetch(`/api/artist`)).json();
}

export async function read_albums(): Promise<IAlbum[]> {
  return await (await fetch(`/api/album`)).json();
}

export async function read_songs(): Promise<ISong[]> {
  return await (await fetch(`/api/song`)).json();
}

export async function read_cart_items(): Promise<ICartItem[]> {
  return await (await fetch(`/api/cart_item`)).json();
}

export async function read_cart_items_by_sessionid(data:number): Promise<ICartItem[]> {
  return await (await fetch(`/api/cart_item_by_shopsess/${data}`)).json();
}

export async function read_order_details(): Promise<IOrderDetail[]> {
  return await (await fetch(`/api/order_detail`)).json();
}

export async function read_pie_order_details(): Promise<[]> {
  return await(await fetch(`/api/pie_orders_per_category`)).json()
}

export async function read_turnover_per_month(data:number): Promise<[]> {
  return await(await fetch(`/api/turnover_per_month/${data}`)).json()
}

export async function read_payment_details(): Promise<IPaymentDetail[]> {
  return await (await fetch(`/api/payment_detail`)).json();
}

export async function read_shopping_sessions(): Promise<IShoppingSession[]> {
  return await (await fetch(`/api/shopping_session`)).json();
}

export async function read_order_items(): Promise<IOrderItem[]> {
  return await (await fetch(`/api/order_item`)).json();
}

export async function read_order_items_by_orderdetail_id(data:number): Promise<IOrderDetail> {
  return await (await fetch(`/api/order_item_by_orderdetailid/${data}`)).json();
}

export async function read_user_addresses(): Promise<IUserAddress[]> {
  return await (await fetch(`/api/user_address`)).json();
}

export async function read_promos(): Promise<IPromo[]> {
  return await (await fetch(`/api/promo`)).json();
}

export async function read_categories(): Promise<ICategory[]> {
  return await (await fetch(`/api/category`)).json();
}

export async function read_users(): Promise<IUser[]> {
  return await (await fetch(`/api/user`)).json();
}

export async function read_one_artist(data: number): Promise<IArtist> {
  return await (await fetch(`/api/artist/${data}`)).json();
}

export async function read_one_album(data: number): Promise<IAlbum> {
  return await (await fetch(`/api/album/${data}`)).json();
}

export async function read_one_song(data: number): Promise<ISong> {
  return await (await fetch(`/api/song/${data}`)).json();
}

export async function read_one_cart_item(data: number): Promise<ICartItem> {
  return await (await fetch(`/api/cart_item/${data}`)).json();
}

export async function read_one_order_detail(
  data: number
): Promise<IOrderDetail> {
  return await (await fetch(`/api/order_detail/${data}`)).json();
}

export async function read_lastone_order_detail_byuserid(
  data: number
): Promise<IOrderDetail> {
  return await (await fetch(`/api/order_detail_byid/${data}`)).json();
}

export async function read_one_payment_detail(
  data: number
): Promise<IPaymentDetail> {
  return await (await fetch(`/api/payment_detail/${data}`)).json();
}

export async function read_one_shopping_session(
  data: number
): Promise<IShoppingSession> {
  return await (await fetch(`/api/shopping_session/${data}`)).json();
}

export async function read_last_one_shopping_session_byuser(
  data: number
): Promise<IShoppingSession> {
  return await (await fetch(`/api/shopping_session_byuserid/${data}`)).json();
}

export async function read_one_order_item(data: number): Promise<IOrderItem> {
  return await (await fetch(`/api/order_item/${data}`)).json();
}

export async function read_one_user_addresses(
  data: number
): Promise<IUserAddress> {
  return await (await fetch(`/api/user_address/${data}`)).json();
}

export async function read_one_user(data: number): Promise<IUser> {
  return await (await fetch(`/api/user/${data}`)).json();
}

export async function login(data: ILogin): Promise<ILogin> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/user`, config)).json();
}

export async function create_artist(data: IArtist): Promise<IArtist> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/artist`, config)).json();
}

export async function create_album(data: IAlbum): Promise<IAlbum> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/album`, config)).json();
}

export async function create_song(data: ISong): Promise<ISong> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/song`, config)).json();
}

export async function create_cart_item(data: ICartItem): Promise<ICartItem> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/cart_item`, config)).json();
}

export async function create_order_detail(
  data: IOrderDetail
): Promise<IOrderDetail> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/order_detail`, config)).json();
}



export async function create_payment_detail(
  data: IPaymentDetail
): Promise<IPaymentDetail> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/payment_detail`, config)).json();
}

export async function create_shopping_session(
  data: IShoppingSession
): Promise<IShoppingSession> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/shopping_session`, config)).json();
}

export async function create_order_item(data: IOrderItem): Promise<IOrderItem> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/order_item`, config)).json();
}

export async function create_user_address(
  data: IUserAddress
): Promise<IUserAddress> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/user_address`, config)).json();
}

export async function create_promo(data: IPromo): Promise<IPromo> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/promo`, config)).json();
}

export async function create_category(data: ICategory): Promise<ICategory> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/category`, config)).json();
}



export async function create_user(data: IUser): Promise<IUser> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/user`, config)).json();
}

// Update
export async function update_artist(data: IArtist): Promise<IArtist> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/artist`, config)).json();
}

export async function update_category(data:ICategory): Promise<ICategory> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/category`, config)).json()
}

export async function update_album(data: IAlbum): Promise<IAlbum> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/album`, config)).json();
}

export async function update_song(data: ISong): Promise<ISong> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/song/${data.id}`, config)).json();
}

export async function update_cart_item(data: ICartItem): Promise<ICartItem> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/cart_item`, config)).json();
}

export async function update_order_detail(
  data: IOrderDetail
): Promise<IOrderDetail> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/order_detail`, config)).json();
}

export async function update_payment_detail(
  data: IPaymentDetail
): Promise<IPaymentDetail> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/payment_detail`, config)).json();
}

export async function update_shopping_session(
  data: IShoppingSession
): Promise<IShoppingSession> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/shopping_session`, config)).json();
}

export async function update_order_item(data: IOrderItem): Promise<IOrderItem> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/order_item`, config)).json();
}

export async function update_user_address(
  data: IUserAddress
): Promise<IUserAddress> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/user_address`, config)).json();
}

export async function update_user(data: IUser): Promise<IUser> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/user`, config)).json();
}
// Delete
export async function delete_artist(data: number): Promise<any> {
  const config = {
    method: "DELETE",
  };
  return await (await fetch(`/api/artist/${data}`, config)).json();
}

export async function delete_album(data: number): Promise<any> {
  const config = {
    method: "DELETE",
  };
  return await (await fetch(`/api/album/${data}`, config)).json();
}

export async function delete_song(data: number): Promise<any> {
  const config = {
    method: "DELETE",
  };
  return await (await fetch(`/api/song/${data}`, config)).json();
}

export async function delete_cart_item(data: number): Promise<any> {
  const config = {
    method: "DELETE",
  };
  return await (await fetch(`/api/cart_item/${data}`, config)).json();
}

export async function delete_cart_item_by_shopsession_albumid(shopping_session: number, album_id:number): Promise<any> {
  const config = {
    method: "DELETE",
  };
  return await (await fetch(`/api/cart_item_shopsessalbum/${shopping_session}/${album_id}`, config)).json();
}

export async function delete_order_detail(data: number): Promise<any> {
  const config = {
    method: "DELETE",
  };
  return await (await fetch(`/api/order_detail/${data}`, config)).json();
}

export async function delete_payment_detail(data: number): Promise<any> {
  const config = {
    method: "DELETE",
  };
  return await (await fetch(`/api/payment_detail/${data}`, config)).json();
}

export async function delete_shopping_session(data: number): Promise<any> {
  const config = {
    method: "DELETE",
  };
  return await (await fetch(`/api/shopping_session/${data}`, config)).json();
}

export async function delete_order_item(data: number): Promise<any> {
  const config = {
    method: "DELETE",
  };
  return await (await fetch(`/api/order_item/${data}`, config)).json();
}

export async function delete_user_address(data: number): Promise<any> {
  const config = {
    method: "DELETE",
  };
  return await (await fetch(`/api/user_address/${data}`, config)).json();
}

export async function delete_user(data: number): Promise<any> {
  const config = {
    method: "DELETE",
  };
  return await (await fetch(`/api/user/${data}`, config)).json();
}

export function toast_function (message:string,type:string) {
  const $toast = useToast();
  let instance =  
        $toast.open({
        message: message,
        type:type,
        duration: 2500,
        position: "bottom-left"
      })

  return instance
}

