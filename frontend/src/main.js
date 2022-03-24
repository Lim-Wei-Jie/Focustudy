import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import 'bootstrap/dist/css/bootstrap.min.css';
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import VueChartkick from 'vue-chartkick'
import 'chartkick/chart.js'

library.add(fas);

createApp(App).use(store).use(router).use(VueChartkick).component('fa', FontAwesomeIcon).mount("#app");