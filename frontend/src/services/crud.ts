import type {
  IAlbum,
  IArtist,
  ICategory,
  ILogin,
  IPromo,
  ISong,
  IUser,
} from "@/interfaces";

const api_url = import.meta.env.VITE_API_URL;
const content_type = {
  "Content-Type": "application/json",
};

export async function read_artists(): Promise<IArtist[]> {
  return await (await fetch(`${api_url}/artist`)).json();
}

export async function read_albums(): Promise<IAlbum[]> {
  return await (await fetch(`${api_url}/album`)).json();
}

export async function read_songs(): Promise<ISong[]> {
  return await (await fetch(`${api_url}/song`)).json();
}

export async function read_promos(): Promise<IPromo[]> {
  return await (await fetch(`${api_url}/promo`)).json();
}

export async function read_categories(): Promise<ICategory[]> {
  return await (await fetch(`${api_url}/category`)).json();
}

export async function read_users(): Promise<IUser> {
  return await (await fetch(`${api_url}/user`)).json();
}

export async function read_one_artist(data: number): Promise<IArtist> {
  return await (await fetch(`${api_url}/artist/${data}`)).json();
}

export async function read_one_album(data: number): Promise<IAlbum> {
  return await (await fetch(`${api_url}/album/${data}`)).json();
}

export async function read_one_song(data: number): Promise<ISong> {
  return await (await fetch(`${api_url}/song/${data}`)).json();
}

export async function login(data: ILogin): Promise<ILogin> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`${api_url}/user`, config)).json();
}

export async function create_artist(data: IArtist): Promise<IArtist> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`${api_url}/artist`, config)).json();
}

export async function create_album(data: IAlbum): Promise<IAlbum> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`${api_url}/album`, config)).json();
}

export async function create_song(data: ISong): Promise<ISong> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`${api_url}/song`, config)).json();
}

export async function create_promo(data: IPromo): Promise<IPromo> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`${api_url}/promo`, config)).json();
}

export async function create_category(data: ICategory): Promise<ICategory> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`${api_url}/category`, config)).json();
}

export async function create_user(data: IUser): Promise<IUser> {
  const config = {
    method: "POST",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`${api_url}/user`, config)).json();
}

// Update
export async function update_artist(data: IArtist): Promise<IArtist> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`${api_url}/artist/${data._id}`, config)).json();
}
export async function update_album(data: IAlbum): Promise<IAlbum> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`${api_url}/album/${data._id}`, config)).json();
}

export async function update_song(data: ISong): Promise<ISong> {
  const config = {
    method: "PUT",
    body: JSON.stringify(data),
    headers: content_type,
  };
  return await (await fetch(`${api_url}/song/${data._id}`, config)).json();
}
// Delete
export async function delete_artist(data: number): Promise<any> {
  const config = {
    method: "DELETE",
  };
  return await (await fetch(`${api_url}/artist/${data}`, config)).json();
}

export async function delete_album(data: number): Promise<any> {
  const config = {
    method: "DELETE",
  };
  return await (await fetch(`${api_url}/album/${data}`, config)).json();
}

export async function delete_song(data: number): Promise<any> {
  const config = {
    method: "DELETE",
  };
  return await (await fetch(`${api_url}/song/${data}`, config)).json();
}
