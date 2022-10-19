import { createWebHistory, createRouter } from "vue-router";
import store from "@/stores";

const beforeAuth = allowAdmin => (from, to, next) => {
  const isAuthenticated = store.getters["isAuthenticated"]
  if (isAuthenticated) {
    if(allowAdmin){
      const isAdmin = store.getters["getUser"].role > 2;
      if(isAdmin){
        return next()
      }else{
        alert("권한이 부족합니다!")
        next("/")
      }
    }else{
      return next()
    }
  } else {
    // 홈 화면으로 이동
    alert("로그인을 해주세요!")
    next("/login")
  }
}


const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import('../views/LandingPage.vue'),
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
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    beforeEnter:beforeAuth(false),
    component: () => import('../views/DashBoardPage.vue'),
  },
  {
    path: "/totalDashboard",
    name: "TotalDashboard",

    component: () => import('../views/TotalDashBoardPage.vue'),
  },
  {
    path: "/vacation",
    name: "Vacation",
    beforeEnter:beforeAuth(false),

    component: () => import('../views/RegistVacationPage.vue'),
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
        name:'EditProfile',
        meta:{
          enterClass: "animate__animated animate__fadeInLeft",
          leaveClass: "animate__animated animate__fadeOutRight",
        },
        component:()=>import('../components/profile/EditProfile.vue'),
      },
      {
        path:'userManagement',
        name:'UserManagement',
        beforeEnter:beforeAuth(true),
        meta:{
          enterClass: "animate__animated animate__fadeInLeft",
          leaveClass: "animate__animated animate__fadeOutRight",
        },
        component:()=>import('../components/profile/UserManagement.vue'),
      },
      {
        path:'unitManagement',
        name:'UnitManagement',
        beforeEnter:beforeAuth(true),
        meta:{
          enterClass: "animate__animated animate__fadeInLeft",
          leaveClass: "animate__animated animate__fadeOutRight",
        },
        component:()=>import('../components/profile/UnitManagement.vue'),
      },
      {
        path:'guardroomManagement',
        name:'GuardroomManagement',
        beforeEnter:beforeAuth(true),
        meta:{
          enterClass: "animate__animated animate__fadeInLeft",
          leaveClass: "animate__animated animate__fadeOutRight",
        },
        component:()=>import('../components/profile/GuardroomManagement.vue'),
      },
      {
        path:'vacationManagement',
        name:'VacationManagement',
        beforeEnter:beforeAuth(true),
        meta:{
          enterClass: "animate__animated animate__fadeInLeft",
          leaveClass: "animate__animated animate__fadeOutRight",
        },
        component:()=>import('../components/profile/VacationManagement.vue'),
      }
    ]
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