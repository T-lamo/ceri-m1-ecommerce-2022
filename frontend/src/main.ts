import { createApp  } from 'vue'
import App from './App.vue'
import { loadFonts } from './plugins/webfontloader'
import { createPinia } from "pinia";

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUserSecret, faUser, faCartShopping,faCommentSms,faMagnifyingGlass, faArrowLeftLong,faArrowRightLong,
faStar,faHeart,faAnglesRight, faAnglesDown, faCirclePlus, faTrash, faPenToSquare, faPlus, faMinus, faCircleCheck} from '@fortawesome/free-solid-svg-icons'
import { faFacebook, faTwitter, faTwitch, faLinkedin, faGoogle } from '@fortawesome/free-brands-svg-icons'
/* add icons to the library */
library.add(faUserSecret,faUser,faCartShopping,faCommentSms,faMagnifyingGlass,
faArrowLeftLong,faArrowRightLong,faStar,faHeart,faAnglesRight,faAnglesDown,
faFacebook, faTwitch,faTwitter,faLinkedin,faGoogle,faCirclePlus,faCartShopping, faTrash,faPenToSquare,faPlus,faMinus,
faCircleCheck)

import router from "./router";

loadFonts()
// import "./assets/scss/base.scss";
// import "./assets/scss/_mixins.scss";
// import "./assets/scss/debug.scss";

const pinia = createPinia()
const app = createApp(App)
  .use(router)
  .use(pinia)
  .component('font-awesome-icon', FontAwesomeIcon)
  .mount("#app")
