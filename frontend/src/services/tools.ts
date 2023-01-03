import { Album } from "@/models";
import { useAppStore } from "@/stores";
import { storeToRefs } from "pinia";

const { list_album } = storeToRefs(useAppStore());

export const getImage = (imagePath: string) => {
  return imagePath;
};
export const check_me_album = (album_id: number) => {
  let my_selected_album = new Album();
  list_album.value.forEach((element: Album) => {
    if (element.id == album_id) {
      my_selected_album = element;
    }
  });
  return my_selected_album;
};
