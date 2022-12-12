import { defineStore } from "pinia";
import type {
  Album,
  Artist,
  CartItem,
  Category,
  OrderDetail,
  OrderItem,
  PaymentDetail,
  Promo,
  ShoppingSession,
  Song,
  User,
} from "@/models";

import { ref } from "vue";

export const useAppStore = defineStore("app", () => {
  // const list_artist = ref<number[]>([1, 3]);
  const current_user = ref<User>()
  // const one_command = ref<Album>();
  // const temporary_command = ref<String>([]);
  const total_price = ref(0);
  const list_artist = ref<Artist[]>([]);
  const list_album = ref<Album[]>([]);
  const isLoggedIn = ref<boolean>()
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
    current_user,
    // one_command,
    total_price,
    isLoggedIn,
    // temporary_command,
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
  };
});
