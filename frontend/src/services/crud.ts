import type {
  IAlbum,
  IArtist,
  ICategory,
  ILogin,
  IPromo,
  ISong,
  IUser,
} from "@/interfaces";

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

export async function read_promos(): Promise<IPromo[]> {
  return await (await fetch(`/api/promo`)).json();
}

export async function read_categories(): Promise<ICategory[]> {
  return await (await fetch(`/api/category`)).json();
}

export async function read_users(): Promise<IUser> {
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
  return await (await fetch(`/api/artist/${data.id}`, config)).json();
}
export async function update_album(data: IAlbum): Promise<IAlbum> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/album/${data.id}`, config)).json();
}

export async function update_song(data: ISong): Promise<ISong> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`/api/song/${data.id}`, config)).json();
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
