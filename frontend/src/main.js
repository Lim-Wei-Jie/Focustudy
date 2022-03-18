import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import GAuth from "vue3-google-oauth2";

const app = createApp(App);

const gAuthOptions = {
  clientId:
    "1085222991075-8id5dael3f6kb876kvl7dh7mi9pdvuvs.apps.googleusercontent.com",
  scope: "email",
  prompt: "consent",
  fetch_basic_profile: true,
};

app.use(GAuth, gAuthOptions);

app.use(store).use(router).mount("#app");
