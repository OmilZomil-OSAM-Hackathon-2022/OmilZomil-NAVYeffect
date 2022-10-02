import { createWebHistory, createRouter } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import('../views/DashBoardPage.vue'),
    // redirect: '/login',
  },
  {
    path: "/api",
    name: "api",

    component: () => import('../views/APITestPage.vue'),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import('../views/LoginPage.vue'),
  },
  {
    path: "/register",
    name: "Register",
    component: () => import('../views/RegisterPage.vue'),
  },
  {
    path: "/listup",
    name: "ListUp",
    component: () => import('../views/ListUpPage.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;