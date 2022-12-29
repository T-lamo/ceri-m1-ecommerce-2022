import { createRouter, createWebHistory } from 'vue-router'
import Homepage from '../components/Homepage.vue'
import AlbumDetail from '../components/album/AlbumDetail.vue'
import ListAlbumAchat from '../components/album/ListAlbumAchat.vue'
import ArtistDetail from '../components/artist/ArtistDetail.vue'
import Authentification from '../components/auth/Authentification.vue'
import Panier_Multistep from '../components/panier/Panier_Multistep.vue'
import OneArticle from '../components/album/OneArticle.vue'
import LoginssotestVue from '../components/auth/Loginssotest.vue'
import Promo from '../components/promo/Promo.vue'
import Charts from '@/components/admin/Charts.vue'
import Customers from '@/components/admin/Customers.vue'
import Orders from '@/components/admin/Orders.vue'
import Albums from '@/components/admin/Albums.vue'
import Artists from '@/components/admin/Artists.vue'
import Category from '@/components/admin/Category.vue'

const UserInfo = {
  template: '<div><p>User {{ $route.params.id }}</p></div>'
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: Homepage
    },
    {
      path: '/album_detail',
      name: 'album_detail',
      component: AlbumDetail
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import('../views/DetailAlbumView.vue')
    },
    {
      path: '/list_album_achat',
      name: 'list_album_achat',
      component: ListAlbumAchat
    },
    {
      path: '/panier',
      name: 'panier',
      component: Panier_Multistep
    },
    {
      path: '/artist_selected/:id',
      name:  'artist',
      component: ArtistDetail
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
      path: '/loginsso',
      name:'loginsso',
      component:LoginssotestVue
    },
    {
      path: '/promo',
      name:'promo',
      component:Promo
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
          path: 'orders',
          name: 'orders',
          components : {
            orders_name: Orders,
          } 
    
        },
        { 
          path:'customers',
          name: 'customers',
          components: {
            customers_name: Customers 
          } 
          
        },
        { 
          path:'admin_albums',
          name: 'admin_albums',
          components: {
            albums_name: Albums 
          } 
          
        },
        { 
          path:'admin_artists',
          name: 'admin_customers',
          components: {
            artists_name: Artists 
          } 
          
        },
        { 
          path:'admin_cat',
          name: 'admin_cat',
          components: {
            cat_name: Category 
          } 
          
        },
        { 
          path:'admin_charts',
          name: 'admin_charts',
          components: {
            charts_name: Charts 
          } 
          
        },

      ]
    },
    
    
  ],
  strict: true,
})

export default router;
