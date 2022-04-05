import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SignIn from "../views/SignIn.vue";
import ActivitiesView from "../views/ActivitiesView.vue";

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
  // Analytics
  {
    path: "/activity",
    name: "activity",
    component: ActivitiesView
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
