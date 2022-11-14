import { createRouter, createWebHistory } from 'vue-router'
import Homepage from '../components/HomePage.vue'
import AlbumDetail from '../components/AlbumDetail.vue'
import ListAlbumAchat from '../components/ListAlbumAchat.vue'
import Panier from '../components/Panier.vue'
import Panier_Multistep from '../components/Panier_Multistep.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
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
      component: Panier
    }
  ]
})

export default router
