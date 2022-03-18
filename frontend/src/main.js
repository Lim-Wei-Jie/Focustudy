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
    "611802935306-9gjli8l6qcr5vbh150g0q60iqnv52u85.apps.googleusercontent.com",
  scope: "email",
  prompt: "consent",
  fetch_basic_profile: true,
};

app.use(GAuth, gAuthOptions);

app.use(store).use(router).mount("#app");
