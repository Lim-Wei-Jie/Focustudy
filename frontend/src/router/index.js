import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SignIn from "../views/SignIn.vue";
import DisplaySessionsView from "../views/DisplaySessionsView.vue";

const routes = [
  // Homepage
  {
    path: "/home",
    name: "home",
    component: HomeView,
  },
  // Sign In
  {
    path: "/",
    name: "auth",
    component: SignIn
  },
  // Display Sessions
  {
    path: "/sessions",
    name: "sessions",
    component: DisplaySessionsView,
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
