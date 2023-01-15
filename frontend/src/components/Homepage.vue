<script lang="ts" setup>
  import { useAppStore } from "@/stores";
  import { storeToRefs } from "pinia";

  import { onMounted, ref, watch } from "vue";
  import { read_albums, read_promos } from "@/services/crud";
  import { Album, type Promo } from "@/models";
  import SearchComponent from "@/components/search/SearchComponent.vue";
  import { RouterLink } from "vue-router";

  const user_from_localstorage = localStorage.getItem("userId");
  

  const { list_promo, list_album, isAdminStore } = storeToRefs(useAppStore());
  let is_data_search_items = ref<Boolean>(false);
  const { searchItems } = storeToRefs(useAppStore());
  watch(searchItems, (newVal, oldVal) => {
    console.log(newVal.values);
    const arr: any[] = Object.entries(newVal).map((value) => value);
    if (arr.length > 0) {
      is_data_search_items.value = true;
    } else {
      is_data_search_items.value = false;
    }

  });
  onMounted(async () => {
    list_promo.value = (await read_promos()) as Promo[];
    list_album.value = (await read_albums()) as Album[];
   
  });

  const check_me_album = (id_album: number) => {
    let my_selected_album = new Album();
    list_album.value.forEach((element: Album) => {
      if (element.id == id_album) {
        my_selected_album = element;
      }
    });
    return my_selected_album;
  };

  /** handle dates **/

  const monthNames = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  const getMonthName = (month: number): string => {
    return monthNames[month];
  };

  const handleDate = (stringdate: string): string => {
    const date = new Date(stringdate);

    return (
      "" +
      date.getDate() +
      " " +
      getMonthName(date.getMonth()) +
      " " +
      date.getFullYear()
    );
  };
</script>
<template>
  <div v-if="isAdminStore == false">
    <div
      id="carouselExampleCaptions"
      class="carousel slide"
      data-bs-ride="true"
    >
      <div class="carousel-inner">
        <div
          v-for="(item, index) in list_promo"
          :key="index"
          :class="{ 'carousel-item': true, active: index === 0 }"
        >
          <img
            src="https://ziked.fr/wp-content/uploads/2020/12/platine-1140x760.jpeg"
            :style="{ width: 800 + 'px', height: 500 + 'px' }"
            class="d-block w-100"
          />
          <div class="carousel-caption">
            <!--d-none d-md-block-->
            <h1>{{ check_me_album(item.album_id).title }}</h1>
            <button class="btn btn-secondary ancient_price">
              $ {{ check_me_album(item.album_id).price }}
            </button>
            <button class="btn btn-secondary">
              $
              {{
                check_me_album(item.album_id).price -
                (item.rate / 100) * check_me_album(item.album_id).price
              }}
            </button>
            <button class="btn btn-secondary">
              De {{ handleDate(item.start_date) }} à
              {{ handleDate(item.end_date) }}
            </button>
            <button class="btn btn-warning">SHOW DETAILS</button>
          </div>
        </div>
      </div>
      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
  <!-- Choose an option -->
  <section
    class="page-section bg-light py-4 text-center"
    id="offer"
    v-if="isAdminStore == false"
  >
    <div class="container">
      <div class="text-center">
        <h2 class="section-heading text-uppercase">OFFER</h2>
        <h3 class="section-subheading text-muted">What we offer you today</h3>
      </div>
      <div class="row">
        <div class="col-lg-4 col-sm-6 mb-4">
          <!-- Categories -->
          <div class="offer-item">
            <a class="offer-link">
              <router-link
                to="/categories"
                style="color: black; text-decoration: none"
              >
                <img
                  class="img-fluid"
                  src="https://p4.wallpaperbetter.com/wallpaper/252/974/552/music-wallpaper-preview.jpg"
                  alt="..."
                />
              </router-link>
            </a>
            <div class="offer-caption">
              <div class="offer-caption-heading">Categories</div>
              <div class="offer-caption-subheading text-muted">Which one ?</div>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-sm-6 mb-4">
          <!-- Albums -->
          <div class="offer-item">
            <a class="offer-link">
              <router-link
                to="/albums"
                style="color: black; text-decoration: none"
              >
                <img
                  class="img-fluid"
                  src="https://www.laposte.fr/medias/sys_master/images/hda/h01/11505336287262.jpg"
                  alt="..."
                />
              </router-link>
            </a>
            <div class="offer-caption">
              <div class="offer-caption-heading">Albums</div>
              <div class="offer-caption-subheading text-muted">
                Listen to me
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-sm-6 mb-4">
          <!-- Artists -->
          <div class="offer-item">
            <a class="offer-link">
              <router-link
                to="/artists"
                style="color: black; text-decoration: none"
              >
                <img
                  class="img-fluid"
                  src="https://img.freepik.com/photos-premium/image-noir-blanc-du-microphone-microphone-scene-est-gros-plan-bar-bar-restaurant-musique-classique-musique_116317-1969.jpg"
                  alt="..."
                />
              </router-link>
            </a>
            <div class="offer-caption">
              <div class="offer-caption-heading">Artists</div>
              <div class="offer-caption-subheading text-muted">Identity</div>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-sm-6 mb-4 mb-lg-0">
          <!-- Songs -->
          <div class="offer-item">
            <a class="offer-link">
              <img
                class="img-fluid auto"
                src="https://media.istockphoto.com/id/857464782/vector/colorful-music-notes-vector-illustration-abstract-black-background.jpg?s=170667a&w=0&k=20&c=ahXfyRwKAoJ4xdvLthfoLR6HUVQHa0nfZpTlBt8ObrQ="
                alt="..."
              />
            </a>
            <div class="offer-caption">
              <div class="offer-caption-heading">Songs</div>
              <div class="offer-caption-subheading text-muted">Tracks</div>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-sm-6 mb-4 mb-sm-0">
          <!-- Promos-->
          <div class="offer-item">
            <a class="offer-link">
              <router-link
                to="/promo"
                style="color: black; text-decoration: none"
              >
                <img
                  class="img-fluid"
                  src="https://media.istockphoto.com/id/883622612/vector/luxury-golden-glittering-dark-background-vector-vip-background-for-posters-banners-or-cards.jpg?s=612x612&w=0&k=20&c=UVCHTFEm72ZDogpDtWhiOs7MVgw83TdNp-yOt7J9gtU="
                  alt="..."
                />
              </router-link>
            </a>
            <div class="offer-caption">
              <div class="offer-caption-heading">Promos</div>
              <div class="offer-caption-subheading text-muted">
                Promotions for this week
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-4 col-sm-6">
          <!-- About -->
          <div class="offer-item">
            <a class="offer-link">
              <img
                class="img-fluid"
                src="https://media.istockphoto.com/id/883622612/vector/luxury-golden-glittering-dark-background-vector-vip-background-for-posters-banners-or-cards.jpg?s=612x612&w=0&k=20&c=UVCHTFEm72ZDogpDtWhiOs7MVgw83TdNp-yOt7J9gtU="
                alt="..."
              />
            </a>
            <div class="offer-caption">
              <div class="offer-caption-heading">About</div>
              <div class="offer-caption-subheading text-muted">About</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <div :v-if="is_data_search_items">
    <SearchComponent />
    {{ is_data_search_items }}
  </div>
 
</template>
<style scoped>

h1 {
  line-height: 1.5;
  font-weight: 400;
  color: #ffffff;
}
.ancient_price {
  color: red;
  text-decoration: line-through;
}
p {
  color: #240606;
  font-weight: 300;
}
button {
  color: white;
}
#offer img {
  width: 380px;
  height: 250px;
}
</style>
