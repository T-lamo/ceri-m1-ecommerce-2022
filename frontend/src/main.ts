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
faStar,faHeart,faAnglesRight, faAnglesDown, faCirclePlus, faTrash, faPenToSquare, faPlus, faMinus, faCircleCheck,
faHouseUser,
faChartPie,
faBagShopping,
faRecordVinyl,
faUserTie,
faUsers,
faGlobe,
faCheck,
faX,
faEye,
faCat,
faBars,
faChevronDown,
faMusic} from '@fortawesome/free-solid-svg-icons'
import { faFacebook, faTwitter, faTwitch, faLinkedin, faGoogle } from '@fortawesome/free-brands-svg-icons'
/* add icons to the library */
library.add(faUserSecret,faUser,faCommentSms,faMagnifyingGlass,
faArrowLeftLong,faArrowRightLong,faStar,faHeart,faAnglesRight,faAnglesDown,
faFacebook, faTwitch,faTwitter,faLinkedin,faGoogle,faCirclePlus,faCartShopping, faTrash,faPenToSquare,faPlus,faMinus,
faCircleCheck, faHouseUser, faChartPie, faBagShopping, faRecordVinyl, faUserTie, faUsers , faGlobe, faCheck,faX, faEye, faCat, faBars, faChevronDown, faMusic)

import router from "./router";

/* google oauth */
import vue3GoogleLogin from 'vue3-google-login'

/**toast plugin */
import ToastPlugin from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';

/** alert */
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

loadFonts()
// import "./assets/scss/base.scss";
// import "./assets/scss/_mixins.scss";
// import "./assets/scss/debug.scss";

/** algolia search */
// import algoliasearch from 'algoliasearch/lite';
// import * as VueInstantSearch from 'vue-instantsearch';


// const searchClient = algoliasearch(
//   'HWG44CLCK1',
//   '0b4f81889da3c4fa1304d66b18354fc4'
// );

/** datepicker */
import '@vuepic/vue-datepicker/dist/main.css'

const pinia = createPinia()
const app = createApp(App)
  .use(ToastPlugin)
  // .use(VueInstantSearch)
  .use(VueSweetalert2)
  .use(router)
  .use(pinia)
  .use(vue3GoogleLogin, {
    clientId: '203638889084-p1gjpddbcnmioc1id0leg9vk7n0jocj9.apps.googleusercontent.com'
  })
  .component(
    'font-awesome-icon', FontAwesomeIcon,
  )
  .mount("#app")
