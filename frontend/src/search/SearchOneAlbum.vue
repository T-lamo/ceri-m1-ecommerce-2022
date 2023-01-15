<script lang="ts" setup>
  import type { Album } from "@/models";

  const props = defineProps<{
    album: Album;
  }>();
</script>
<template>
  <div class="one-album">
    <div
      class="image"
      :style="{ 'background-image': `url(${props.album.cover})` }"
    />
    <div class="info">
      <h6>{{ props.album.title }}</h6>
      <h6>{{ props.album.price }}</h6>
    </div>
  </div>
</template>

<style scoped>
.one-album {
  display: flex;
  flex-direction: row;
  width: 100%;
  color: black;
  border: 1px solid gray;
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
}
.image {
  background-size: cover;
  background-position: center;
  width: 90px;
  height: 60px;
  display: flex;
  align-self: center;
}

.info {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  align-self: center;
  margin-left: 1rem;
}

h6 {
  font-size: small;
  padding: 0px;
  margin: 0px;
}
</style>
