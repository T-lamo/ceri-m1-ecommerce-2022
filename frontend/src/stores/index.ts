import { defineStore } from "pinia";
import type { Album, Artist, Category, Promo, Song } from "@/models";
import {
  read_albums,
  read_artists,
  read_categories,
  read_promos,
  read_songs,
} from "@/services/crud";
import { ref } from "vue";

export const useAppStore = defineStore("app", () => {
  // const list_artist = ref<number[]>([1, 3]);
  const list_artist = ref<Artist[]>([]);
  const list_album = ref<Album[]>([]);

  const list_song = ref<Song[]>([]);

  const list_promo = ref<Promo[]>([]);

  const list_category = ref<Category[]>([]);


  return { list_artist, list_album, list_song, list_promo, list_category };
});
