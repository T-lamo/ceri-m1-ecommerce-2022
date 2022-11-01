<script setup lang="ts">
import type {
  ISong,
  IArtist,
  IAlbum,
  ICategory,
  IPromo,
  IUser,
} from "@/interfaces";
import { Artist, Album, Song, Category, Promo } from "@/models";
import {
  read_artists,
  read_albums,
  read_songs,
  read_categories,
  read_promos,
} from "@/services/crud";

import { insert_seed_to_db, seed_db } from "@/utils/data/seed";

import { onMounted } from "vue";

import { storeToRefs } from "pinia";
import { useAppStore } from "@/stores";

onMounted(async () => {
  const { list_artist, list_album, list_song, list_promo, list_category } =
    storeToRefs(useAppStore());

  // list_artist.value = (await read_artists()).map((res: any) => {
  //   return new Artist({
  //     id: res[0],
  //     firstname: res[1],
  //     lastname: res[2],
  //     date_of_birth: res[3],
  //     cover: res[4],
  //   });
  // });

  // list_album.value = (await read_albums()).map((res: any) => {
  //   return new Album({
  //     id: res[0],
  //     title: res[1],
  //     price: res[2],
  //     description: res[3],
  //     cover: res[4],
  //     artist_id: res[5],
  //     category_id: res[6],
  //   });
  // });

  list_song.value = (await read_songs()).map((res: any) => {
    return new Song({
      id: res.id,
      title: res.title,
      release_date: res.release_date,
      like_qty: res.like_qty,
      cover: res.cover,
      album_id: res.album_id,
    });
  });

  // list_promo.value = (await read_promos()).map((res: any) => {
  //   return new Promo({
  //     id: res[0],
  //     start_date: res[1],
  //     end_date: res[2],
  //     rate: res[3],
  //     album_id: res[4],
  //   });
  // });

  // list_category.value = (await read_categories()).map((res: any) => {
  //   console.log(res);
  //   return res;
  // });

  console.log("list category", list_song.value);

  // seed_db();
  // insert_seed_to_db();
});
</script>


<style scoped></style>
