import { createRouter, createWebHistory } from 'vue-router'
import Homepage from '../components/Homepage.vue'
import ArtistDetail from '../components/artist/ArtistDetail.vue'
import Authentification from '../components/auth/Authentification.vue'
import Panier_Multistep from '../components/panier/Panier_Multistep.vue'
import OneArticle from '../components/album/OneArticle.vue'
import OneAlbumDetail from '@/components/album/OneAlbumDetail.vue'
import Promo from '../components/promo/Promo.vue'
import Charts from '@/components/admin/Charts.vue'
import Customers from '@/components/admin/Customers.vue'
import Orders from '@/components/admin/Orders.vue'
import Albums from '@/components/admin/Albums.vue'
import Artists from '@/components/admin/Artists.vue'
import Category from '@/components/admin/Category.vue'
import ListArtist from '@/components/artist/ListArtist.vue'
import ListAlbum from '@/components/album/ListAlbum.vue'
import ListCategory from '@/components/category/ListCategory.vue'
import { Chart } from 'chart.js'


const UserInfo = {
  template: "<div><p>User {{ $route.params.id }}</p></div>",
};

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/home",
      name: "home",
      component: Homepage,
    },
    {
      path: '/album_selected/:id',
      name: 'album_selected',
      component: OneAlbumDetail
    },
    {
      path: "/panier",
      name: "panier",
      component: Panier_Multistep,
    },
    {
      path: "/artist_selected/:id",
      name: "artist",
      component: ArtistDetail,
    },
    {
      path: "/",
      name: "login",
      component: Authentification,
    },
    {
      path: '/',
      name: 'login',
      component: Authentification
    },
    {
      path: '/onearticle',
      name: 'onearticle',
      component: OneArticle
    },
    {
      path: '/promo',
      name:'promo',
      component:Promo
    },
    {
      path: '/albums',
      name:'albums',
      component: ListAlbum
    },
    {
      path: '/artists',
      name: 'artists',
      component: ListArtist
    },
    {
      path: '/categories',
      name: 'categories',
      component: ListCategory
    },
    {
      path:'/user/:id', 
      name: 'user',
      component: UserInfo
    },
    {
      path:'/admin', 
      name: 'admin',
      
      children: [
        {
          path: "orders",
          name: "orders",
          components: {
            orders_name: Orders,
          },
        },
        {
          path: "customers",
          name: "customers",
          components: {
            customers_name: Customers,
          },
        },
        {
          path: "admin_albums",
          name: "admin_albums",
          components: {
            albums_name: Albums,
          },
        },
        {
          path: "admin_artists",
          name: "admin_customers",
          components: {
            artists_name: Artists,
          },
        },
        {
          path: "admin_cat",
          name: "admin_cat",
          components: {
            cat_name: Category,
          },
        },
        {
          path: "admin_charts",
          name: "admin_charts",
          components: {
            charts_name: Charts,
          },
        },
      ],
    },
    
  ],
  strict: true,
});

export default router;
