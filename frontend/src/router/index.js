import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import  rating from "../views/RatingView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/rating",
    name: "rating",
    component: rating,
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
