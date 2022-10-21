import type {
  IAlbum,
  IArtist,
  ICategory,
  IPromo,
  ISong,
  IUser,
} from "@/interfaces/index";

export class Song implements ISong {
  _id?: number;
  title!: string;
  release_date!: string;
  like_qty!: number;
  cover!: string;
  album_id!: number;

  constructor(fields?: Partial<ISong>) {
    Object.assign(this, fields);
  }
}

export class Album implements IAlbum {
  _id?: number = -1;
  title!: string;
  release_date!: string;
  cover?: string = "default url";
  artist_id!: number;
  price!: number;
  description!: string;
  category_id!: number;
  list_song?: Song[] = [];

  constructor(fields?: Partial<IAlbum>) {
    Object.assign(this, fields);
  }

  set_list_song(songs: Song[]) {
    this.list_song = songs.filter((songs) => songs.album_id == this._id);
  }
}

export class Artist implements IArtist {
  _id?: number = -1;
  firstname: string;
  lastname: string;
  date_of_birth?: string = Date();
  cover?: string = "url";
  list_album?: Album[] = [];

  constructor(fields?: Partial<IArtist>) {
    Object.assign(this, fields);
  }

  set_list_album(albums: Album[]) {
    this.list_album = albums.filter((album) => album._id == this._id);
  }
}

export class Promo implements IPromo {
  _id?: number = -1;
  start_date!: string;
  end_date!: string;
  rate!: number;
  album_id!: number;

  constructor(fields?: Partial<IPromo>) {
    Object.assign(this, fields);
  }
}

export class Category implements ICategory {
  _id?: number = -1;
  label!: string;
  list_album?: Album[] = [];
  constructor(data: Partial<ICategory>) {
    Object.assign(this, data);
  }
  set_list_album(albums: Album[]) {
    this.list_album = albums.filter((album) => album._id == this._id);
  }
}

export class User implements IUser {
  _id?: number;
  username!: string;
  email!: string;
  password?: string | undefined = undefined;
  is_admin!: boolean;

  constructor(data: Partial<IUser>) {
    Object.assign(this, data);
  }
}
