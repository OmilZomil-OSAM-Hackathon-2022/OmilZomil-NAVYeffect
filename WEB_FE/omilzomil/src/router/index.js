import { createWebHistory, createRouter } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    redirect: '/login',
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
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;