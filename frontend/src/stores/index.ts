import { defineStore } from "pinia";
import {
  Album,
  type Artist,
  type CartItem,
  type Category,
  type OrderDetail,
  type OrderItem,
  type PaymentDetail,
  type Promo,
  type ShoppingSession,
  type Song,
  type User,
  type UserAddress,
} from "@/models";

import { ref } from "vue";

const searches: Album[] = [
  new Album({
    title: "album1",
    price: 10,
    cover:
      "https://images.unsplash.com/photo-1603884574615-7b6ec4198a8c?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwzNDF8fG1vdmllfGVufDB8fHx8MTY2ODY0MjgyMQ&ixlib=rb-4.0.3&w=500&h=1000",
  }),
  new Album({
    title: "album2",
    price: 10,
    cover:
      "https://images.unsplash.com/photo-1603884574615-7b6ec4198a8c?ixid=MnwxMDkyNjJ8MHwxfHNlYXJjaHwzNDF8fG1vdmllfGVufDB8fHx8MTY2ODY0MjgyMQ&ixlib=rb-4.0.3&w=500&h=1000",
  }),
];

export const useAppStore = defineStore("app", () => {
  const searchItems = ref<Album[]>(searches);
  const isElementInSearchItem = ref<Boolean>(false);
  const isAdminStore = ref(Boolean(localStorage.getItem("isAdmin")));
  const current_user = ref<User>();
  const last_shopping_session = ref<ShoppingSession>();
  const current_shopping_session = ref<ShoppingSession>();
  const shipping_chosen = ref<UserAddress>();
  const current_order_detail = ref<OrderDetail>();
  const current_payement = ref<PaymentDetail>();
  const one_artist = ref<Artist>();
  const total_price = ref(0);
  const list_artist = ref<Artist[]>([]);
  const list_album = ref<Album[]>([]);
  const list_song = ref<Song[]>([]);
  const list_cart_item = ref<CartItem[]>([]);
  const list_order_detail = ref<OrderDetail[]>([]);
  const list_payment_detail = ref<PaymentDetail[]>([]);
  const list_shopping_Session = ref<ShoppingSession[]>([]);
  const list_order_item = ref<OrderItem[]>([]);
  const list_user = ref<User[]>([]);
  const list_user_address = ref<CartItem[]>([]);

  const list_promo = ref<Promo[]>([]);

  const list_category = ref<Category[]>([]);

  return {
    isAdminStore,
    current_user,
    one_artist,
    total_price,
    last_shopping_session,
    current_shopping_session,
    current_order_detail,
    current_payement,
    shipping_chosen,
    list_artist,
    list_album,
    list_song,
    list_promo,
    list_category,
    list_cart_item,
    list_order_detail,
    list_payment_detail,
    list_shopping_Session,
    list_order_item,
    list_user,
    list_user_address,
    searchItems,
    isElementInSearchItem,
  };
});
