import { Album, Artist, Category, Promo, Song } from "@/models";
import {
  create_album,
  create_artist,
  create_category,
  create_promo,
  create_song,
} from "@/services/crud";

export async function seed10artist(collection: string) {
  console.log("inside send messages", collection);
  try {
    await fetch(`https://restapi.fr/generator`, {
      method: "POST",
      body: JSON.stringify({
        times: 10,
        resourceName: collection,

        cover: {
          type: "image",
          theme: "person",
          height: 1000,
          width: 500,
        },
        firstname: "name",
        lastname: "name",
        date_of_birth: {
          range: ["1990-01-04T15:55:21.229Z", "2022-12-12T15:55:21.229Z"],
          type: "date",
        },
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
  } catch (e) {
    console.log(e);
  }
}

export async function seed10category(collection: string) {
  console.log("inside send category", collection);
  try {
    await fetch(`https://restapi.fr/generator`, {
      method: "POST",
      body: JSON.stringify({
        times: 10,
        resourceName: collection,
        label: {
          type: "sentence",
          range: [1, 2],
        },
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
  } catch (e) {
    console.log(e);
  }
}

export async function seed40Album(collection: string) {
  console.log("inside send album", collection);

  try {
    await fetch(`https://restapi.fr/generator`, {
      method: "POST",
      body: JSON.stringify({
        times: 40,
        resourceName: collection,
        title: {
          type: "sentence",
          range: [2, 3],
        },
        release_date: {
          range: ["2022-01-04T15:55:21.229Z", "2022-12-12T15:55:21.229Z"],
          type: "date",
        },
        price: {
          type: "number",
          range: [85, 200],
        },
        description: {
          type: "sentence",
          range: [14, 16],
        },
        cover: {
          type: "image",
          theme: "music",
          height: 1000,
          width: 500,
        },
        category_id: {
          type: "number",
          range: [0, 10],
        },
        artist_id: {
          type: "number",
          range: [0, 10],
        },
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
  } catch (e) {
    console.log(e);
  }
}

export async function seed50song(collection: string) {
  console.log("inside send song", collection);

  try {
    await fetch(`https://restapi.fr/generator`, {
      method: "POST",
      body: JSON.stringify({
        times: 50,
        resourceName: collection,

        title: {
          type: "sentence",
          range: [2, 3],
        },

        release_date: {
          range: ["2022-01-04T15:55:21.229Z", "2022-12-12T15:55:21.229Z"],
          type: "date",
        },
        cover: {
          type: "image",
          theme: "person",
          height: 1000,
          width: 500,
        },
        like_qty: {
          type: "number",
          range: [7000, 40000],
        },
        album_id: {
          type: "number",
          range: [0, 40],
        },
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
  } catch (e) {
    console.log(e);
  }
}

export async function seed20promo(collection: string) {
  console.log("inside send promo", collection);
  try {
    await fetch(`https://restapi.fr/generator`, {
      method: "POST",
      body: JSON.stringify({
        times: 20,
        resourceName: collection,
        start_date: {
          range: ["2022-07-04T15:55:21.229Z", "2022-12-12T15:55:21.229Z"],
          type: "date",
        },
        end_date: {
          range: ["2022-07-04T15:55:21.229Z", "2022-12-12T15:55:21.229Z"],
          type: "date",
        },
        album_id: {
          type: "number",
          range: [0, 40],
        },
        rate: {
          type: "number",
          range: [12, 30],
        },
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
  } catch (e) {
    console.log(e);
  }
}

export function seed_db() {
  //seed10artist("artist");
  //seed10category("category");
  //seed40Album("album");
   //seed20promo("promo");
  //seed50song("song");
}

export function insert_seed_to_db() {
  //   fetch("https://restapi.fr/api/category").then(async (data) => {
  //     const res = data.json().then((data) => {
  //       console.log(data);
  //       const arr: Category[] = data.map((data) => {
  //         return new Category({ label: data.label });
  //       });

  //       arr.map(async (data) => {
  //         create_category(data);
  //       });
  //     });
  //   });

  // fetch("https://restapi.fr/api/artist").then(async (data) => {
  //   const res = data.json().then((data) => {
  //     console.log(data);
  //     const arr: Artist[] = data.map((data) => {
  //       return new Artist({
  //         firstname: data.firstname,
  //         lastname: data.lastname,
  //         date_of_birth: data.date_of_birth,
  //         cover: data.cover,
  //       });
  //     });
  //     console.log("array artist", arr);
  //     arr.map(async (data) => {
  //       create_artist(data);
  //     });
  //   });
  // });

  // fetch("https://restapi.fr/api/album").then(async (data) => {
  //   const res = data.json().then((data) => {
  //     console.log(data);
  //     const arr: Album[] = data.map((data) => {
  //       return new Album({
  //         title: data.title,
  //         release_date: data.release_date,
  //         price: data.price,
  //         description: data.description,
  //         artist_id: data.artist_id,
  //         category_id: data.category_id,
  //         cover: data.cover,
  //       });
  //     });

  //     arr.map(async (data) => {
  //       create_album(data);
  //     });
  //   });
  // });

  // fetch("https://restapi.fr/api/song").then(async (data) => {
  //   const res = data.json().then((data) => {
  //     console.log(data);
  //     const arr: Song[] = data.map((data) => {
  //       return new Song({
  //         title: data.title,
  //         release_date: data.release_date,
  //         cover: data.cover,
  //         like_qty: data.like_qty,
  //         album_id: data.album_id
  //       });
  //     });

  //     arr.map(async (data) => {
  //       create_song(data);
  //     });
  //   });
  // });

  fetch("https://restapi.fr/api/promo").then(async (data) => {
    const res = data.json().then((data) => {
      console.log(data);
      const arr: Promo[] = data.map((data) => {
        return new Promo(data);
      });

      arr.map(async (data) => {
        create_promo(data);
      });
    });
  });
}

// statut: {
//   type: "collection",
//   values: ["true", "false"],
//   unique: false,
// },
