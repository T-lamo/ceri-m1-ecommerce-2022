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
}

export interface IArtist {
  id?: number;
  firstname: string;
  lastname: string;
  date_of_birth?: string;
  cover?: string;
  list_album?: IAlbum[];
}

export interface ISong {
  id?: number;
  title: string;
  release_date: string;
  cover: string;
  album_id: number;
}

export interface ICategory {
  id?: number;
  label: string;
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
  created_at?: string;
}
export interface IOrderDetail {
  id?: number;
  total: number;
  user_id: number;
  created_at?: string;
}
export interface IOrderItem {
  id?: number;
  qty: number;
  order_detail_id: number;
  album_id: number;
  created_at?: string;
}
export interface IPaymentDetail {
  id?: number;
  amount: number;
  name: string;
  provider: string;
  credit_card_number: string;
  status: string;
  expiration_date: string;
  cvv: string;
  order_detail_id: number;
  created_at?: string;
}

export interface IShoppingSession {
  id?: number;
  total: number;
  user_id: number;
  created_at?: string;
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
  created_date?: string;
}

export interface ILogin {
  username: string;
  password: string;
}
