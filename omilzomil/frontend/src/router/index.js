import { createWebHistory, createRouter } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import('../views/DashBoardPage.vue'),
    // component: () => import('../views/DashBoardPage.vue'),
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
    meta:{
      hideAppBar:true,
    },
  },
  {
    path: "/register",
    name: "Register",
    component: () => import('../views/RegisterPage.vue'),
    meta:{
      hideAppBar:true,
    },
  },
  {
    path: "/listup",
    name: "ListUp",
    component: () => import('../views/ListUpPage.vue'),
  },
  {
    path: "/ranking",
    name: "Ranking",
    component: () => import('../views/DashBoardPage.vue'),
    // component: () => import('../views/ListUpPage.vue'),
  },
  {
    path: "/dashboard",
    name: "Dashboard",

    component: () => import('../views/DashBoardPage.vue'),
    // component: () => import('../views/ListUpPage.vue'),
  },
  {
    path: "/totalDashboard",
    name: "TotalDashboard",

    component: () => import('../views/TotalDashBoardPage.vue'),
    // component: () => import('../views/ListUpPage.vue'),
  },
  {
    path: "/vacation",
    name: "Vacation",

    component: () => import('../views/VacationPage.vue'),
    // component: () => import('../views/ListUpPage.vue'),
  },
  
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;