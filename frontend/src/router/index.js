import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AnalyticsView from "../views/AnalyticsView.vue";
import SignIn from "../views/SignIn.vue";

const routes = [
  // Homepage
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  // Analytics
  {
    path: "/analytics",
    name: "analytics",
    component: AnalyticsView
  },
  // Sign In
  {
    path: "/auth",
    name: "auth",
    component: SignIn
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
