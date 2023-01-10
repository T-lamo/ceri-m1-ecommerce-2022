export interface IAlbum {
  id?: number;
  title: string;
  release_date: string;
  cover?: string;
  artist_id: number;
  price: number;
  stock_qty: number;
  description: string;
  category_id: number;
  list_song?: ISong[];
  created_date?: Date;
}

export interface IArtist {
  id?: number;
  firstname: string;
  lastname: string;
  date_of_birth?: string;
  cover?: string;
  list_album?: IAlbum[];
  created_date?: Date;
}

export interface ISong {
  id?: number;
  title: string;
  release_date: string;
  cover: string;
  album_id: number;
  created_date?: Date;
}

export interface ICategory {
  id?: number;
  label: string;
  created_date?: Date;
}

export interface IPromo {
  id?: number;
  start_date: string;
  end_date: string;
  rate: number;
  album_id: number;
}

export interface ICartItem {
  id?: number;
  qty: number;
  album_id: number;
  shopping_session_id: number;
  created_date?: Date;
}
export interface IOrderDetail {
  id?: number;
  total: number;
  user_id: number;
  payment_status: boolean;
  delivery_status: boolean;
  send_status: boolean;
  orders_status: string;
  created_date?: Date;
}
export interface IOrderItem {
  id?: number;
  qty: number;
  order_detail_id: number;
  album_id: number;
  created_date?: Date;
}
export interface IPaymentDetail {
  id?: number;
  amount: number;
  name: string;
  provider: string;
  order_detail_id: number;
  credit_card_number: string;
  status: string;
  created_date?: Date;
}

export interface IShoppingSession {
  id?: number;
  total: number;
  user_id: number;
  created_date?: Date;
}
export interface IUser {
  id?: number;
  username: string;
  firstname?: string;
  email?: string;
  telephone?: string;
  password?: string;
  is_admin: boolean;
  created_date?: Date;
}
export interface IUserAddress {
  id?: number;
  adress_line1: string;
  adress_line2?: string;
  city: string;
  country: string;
  postal_code: string;
  mobile?: string;
  user_id: number;
  created_date?: Date;
}

export interface ILogin {
  username: string;
  password: string;
}
