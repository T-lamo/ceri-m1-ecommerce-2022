import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

import "./assets/scss/base.scss";
import "./assets/scss/_mixins.scss";
import "./assets/scss/debug.scss";

const app = createApp(App);

app.use(createPinia());
app.use(router);

app.mount("#app");
