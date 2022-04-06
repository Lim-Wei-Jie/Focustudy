import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import 'bootstrap/dist/css/bootstrap.min.css';
import "bootstrap";
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faGoogle } from "@fortawesome/free-brands-svg-icons";
import VueChartkick from 'vue-chartkick'
import GAuth from "vue3-google-oauth2";
import 'chartkick/chart.js'

library.add(fas);

// FontAwesome
library.add(faGoogle);

const app = createApp(App);

const gAuthOptions = {
  clientId:
    "1085222991075-8id5dael3f6kb876kvl7dh7mi9pdvuvs.apps.googleusercontent.com",
  scope: "email profile",
  prompt: "consent",
  fetch_basic_profile: true,
};

app.use(GAuth, gAuthOptions).use(VueChartkick)
app.component("font-awesome-icon", FontAwesomeIcon).component('fa', FontAwesomeIcon)
app.use(store).use(router).mount("#app");
