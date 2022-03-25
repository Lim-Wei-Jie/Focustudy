import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import { library } from "@fortawesome/fontawesome-svg-core";
// import { faUserSecret } from "@fortawesome/free-solid-svg-icons";
import { faGoogle } from "@fortawesome/free-brands-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import GAuth from "vue3-google-oauth2";

// FontAwesome
library.add(faGoogle);

const app = createApp(App);

const gAuthOptions = {
  clientId:
    "1085222991075-8id5dael3f6kb876kvl7dh7mi9pdvuvs.apps.googleusercontent.com",
  scope: "https://www.googleapis.com/auth/calendar.readonly",
  prompt: "consent",
  fetch_basic_profile: true,
};

app.use(GAuth, gAuthOptions);
app.component("font-awesome-icon", FontAwesomeIcon);
app.use(store).use(router).mount("#app");
