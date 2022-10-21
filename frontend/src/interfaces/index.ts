export interface IAlbum {
  _id?: number;
  title: string;
  release_date: string;
  cover?: string;
  artist_id: number;
  price: number;
  description: string;
  category_id: number;
}

export interface IArtist {
  _id?: number;
  firstname: string;
  lastname: string;
  date_of_birth?: string;
  cover?: string;
}

export interface ISong {
  _id?: number;
  title: string;
  release_date: string;
  like_qty: number;
  cover: string;
  album_id: number;
}

export interface ICategory {
  _id?: number;
  label: string;
}

export interface IPromo {
  _id?: number;
  start_date: string;
  end_date: string;
  rate: number;
  album_id: number;
}

export interface IUser {
  _id?: number;
  username: string;
  email: string;
  password?: string;
  is_admin: boolean;
}

export interface ILogin {
  username: string;
  password: string;
}
