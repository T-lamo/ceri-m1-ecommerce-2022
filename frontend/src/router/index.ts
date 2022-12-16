<<<<<<< HEAD
import HomepageVue from "@/components/Homepage.vue";
import { createRouter, createWebHistory } from "vue-router";
import AlbumDetail from "../components/album/AlbumDetail.vue";
import ListAlbumAchat from "../components/album/ListAlbumAchat.vue";
import ArtistDetail from "../components/artist/ArtistDetail.vue";
import Authentification from "../components/auth/Authentification.vue";
import Panier_Multistep from "../components/panier/Panier_Multistep.vue";
=======
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

const UserInfo = {
  template: '<div><p>User {{ $route.params.id }}</p></div>'
}
>>>>>>> 4c53016a5beb63e2692781dcbb5b39b5abb0458e

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
<<<<<<< HEAD
      path: "/",
      name: "home",
      component: HomepageVue,
=======
      path: '/home',
      name: 'home',
      component: Homepage
>>>>>>> 4c53016a5beb63e2692781dcbb5b39b5abb0458e
    },
    {
      path: "/album_detail",
      name: "album_detail",
      component: AlbumDetail,
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import('../views/DetailAlbumView.vue')
    },
    {
      path: "/list_album_achat",
      name: "list_album_achat",
      component: ListAlbumAchat,
    },
    {
<<<<<<< HEAD
      path: "/panier_step",
      name: "panier_step",
      component: Panier_Multistep,
=======
      path: '/panier',
      name: 'panier',
      component: Panier_Multistep
>>>>>>> 4c53016a5beb63e2692781dcbb5b39b5abb0458e
    },
    {
      path: "/artist_selected/:id",
      name: "artist",
      component: ArtistDetail,
    },
    {
<<<<<<< HEAD
      path: "/login",
      name: "login",
      component: Authentification,
    },
=======
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
    }
>>>>>>> 4c53016a5beb63e2692781dcbb5b39b5abb0458e
  ],
  strict: true,
});

export default router;
