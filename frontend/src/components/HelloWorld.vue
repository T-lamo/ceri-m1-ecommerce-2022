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

  list_artist.value = (await read_artists()).map((res: any) => {
    return new Artist({
      id: res.id,
      firstname: res.firstname,
      lastname: res.lastname,
      date_of_birth: res.date_of_birth,
      cover: res.cover,
      list_album: res.list_album,
    });
  });
  console.log("list artist", list_artist.value);

  list_album.value = (await read_albums()).map((res: any) => {
    return new Album({
      id: res.id,
      title: res.title,
      price: res.price,
      stock_qty: res.stock_qty,
      description: res.description,
      cover: res.cover,
      artist_id: res.artist_id,
      category_id: res.category_id,
      list_song: res.list_song,
    });
  });
  console.log("list album", list_album.value);

  list_song.value = (await read_songs()).map((res: any) => {
    return new Song({
      id: res.id,
      title: res.title,
      release_date: res.release_date,
      cover: res.cover,
      album_id: res.album_id,
    });
  });
  console.log("list song", list_song.value);

  list_promo.value = (await read_promos()).map((res: any) => {
    return new Promo({
      id: res.id,
      start_date: res.start_date,
      end_date: res.end_date,
      rate: res.rate,
      album_id: res.album_id,
    });
  });
  console.log("list promo", list_promo.value);

  list_category.value = (await read_categories()).map((res: any) => {
    return res;
  });

  console.log("list category", list_category.value);

  // seed_db();
  // insert_seed_to_db();
});
</script>

<template>
  <div></div>
</template>

<style scoped></style>
