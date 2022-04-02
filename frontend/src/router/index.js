import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AnalyticsView from "../views/AnalyticsView.vue";
import RatingView from "../views/RatingView.vue";

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
  // Rating
  {
    path: "/rating",
    name: "rating",
    component: RatingView,
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
