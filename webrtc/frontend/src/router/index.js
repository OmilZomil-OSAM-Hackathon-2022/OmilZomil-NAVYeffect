import { createRouter, createWebHistory } from "vue-router";
import CameraView from "../views/CameraView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: CameraView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
