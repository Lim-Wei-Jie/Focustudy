import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AnalyticsView from "../views/AnalyticsView.vue";

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
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
