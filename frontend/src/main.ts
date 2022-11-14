import { createApp  } from 'vue'
import App from './App.vue'
import router from './router'
import { loadFonts } from './plugins/webfontloader'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret, faUser, faCartShopping,faCommentSms,faMagnifyingGlass, faArrowLeftLong,faArrowRightLong,
faStar,faHeart,faAnglesRight, faAnglesDown, faCirclePlus, faTrash, faPenToSquare, faPlus, faMinus} from '@fortawesome/free-solid-svg-icons'
import { faFacebook, faTwitter, faTwitch, faLinkedin, faGoogle } from '@fortawesome/free-brands-svg-icons'
/* add icons to the library */
library.add(faUserSecret,faUser,faCartShopping,faCommentSms,faMagnifyingGlass,
faArrowLeftLong,faArrowRightLong,faStar,faHeart,faAnglesRight,faAnglesDown,
faFacebook, faTwitch,faTwitter,faLinkedin,faGoogle,faCirclePlus,faCartShopping, faTrash,faPenToSquare,faPlus,faMinus)

loadFonts()

const app = createApp(App)
  .use(router)
  .component('font-awesome-icon', FontAwesomeIcon)
  .mount('#app')
