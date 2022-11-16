import type {
  IAlbum,
  IArtist,
  ICategory,
  IPromo,
  ISong,
  IUser,
} from "@/interfaces/index";

export class Song implements ISong {
  id?: number;
  title!: string;
  release_date!: string;
  cover!: string;
  album_id!: number;

  constructor(fields?: Partial<ISong>) {
    Object.assign(this, fields);
  }
}

export class Album implements IAlbum {
  id?: number;
  title!: string;
  release_date!: string;
  cover?: string = "default url";
  artist_id!: number;
  price!: number;
  stock_qty!: number;
  description!: string;
  category_id!: number;
  list_song?: ISong[] = [];

  constructor(fields?: Partial<IAlbum>) {
    Object.assign(this, fields);
  }

  set_list_song(songs: Song[]) {
    this.list_song = songs.filter((songs) => songs.album_id == this.id);
  }
}

export class Artist implements IArtist {
  id?: number = -1;
  firstname: string = "";
  lastname: string = "";
  date_of_birth?: string = Date();
  cover?: string = "url";
  list_album?: Album[] = [];

  constructor(fields?: Partial<IArtist>) {
    Object.assign(this, fields);
  }

  set_list_album(albums: Album[]) {
    this.list_album = albums.filter((album) => album.id == this.id);
  }
}

export class Promo implements IPromo {
  id?: number = -1;
  start_date!: string;
  end_date!: string;
  rate!: number;
  album_id!: number;

  constructor(fields?: Partial<IPromo>) {
    Object.assign(this, fields);
  }
}

export class Category implements ICategory {
  id?: number = -1;
  label!: string;
  list_album?: Album[] = [];
  constructor(data: Partial<ICategory>) {
    Object.assign(this, data);
  }
  set_list_album(albums: Album[]) {
    this.list_album = albums.filter((album) => album.id == this.id);
  }
}

export class User implements IUser {
  id?: number;
  username!: string;
  email!: string;
  password?: string | undefined = undefined;
  is_admin!: boolean;

  constructor(data: Partial<IUser>) {
    Object.assign(this, data);
  }
}
