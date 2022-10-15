import { createWebHistory, createRouter } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import('../views/LandingPage.vue'),
    // component: () => import('../views/DashBoardPage.vue'),
    // redirect: '/login',
    meta:{
      isLanding:true,
    },
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
    component: () => import('../views/RankingPage.vue'),
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

    component: () => import('../views/RegistVacationPage.vue'),
    // component: () => import('../views/RegistVacationPage.vue'),
  },
  {
    path:"/unregister",
    name:"Unregister",
    component: () => import('../views/UnregisterPage.vue'),
  },
  {
    path: "/profile",
    name: "Profile",

    component: () => import('../views/ProfilePage.vue'),
    children:[
      {
        path:'',
        name:'editProfile',
        meta:{
          enterClass: "animate__animated animate__fadeInLeft",
          leaveClass: "animate__animated animate__fadeOutRight",
        },
        component:()=>import('../components/profile/editProfile.vue'),
      },
      {
        path:'userManagement',
        name:'userManagement',
        meta:{
          enterClass: "animate__animated animate__fadeInLeft",
          leaveClass: "animate__animated animate__fadeOutRight",
        },
        component:()=>import('../components/profile/userManagement.vue'),
      },
      {
        path:'unitManagement',
        name:'unitManagement',
        meta:{
          enterClass: "animate__animated animate__fadeInLeft",
          leaveClass: "animate__animated animate__fadeOutRight",
        },
        component:()=>import('../components/profile/unitManagement.vue'),
      }
    ]
    // component: () => import('../views/ListUpPage.vue'),
  },
  {
    path: "/api",
    name: "api",

    component: () => import('../views/APITestPage.vue'),
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;