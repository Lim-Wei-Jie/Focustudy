import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SignIn from "../views/SignIn.vue";
import AnalyticsView from "../views/AnalyticsView.vue";

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
    path: "/analytics",
    name: "analytics",
    component: AnalyticsView
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
