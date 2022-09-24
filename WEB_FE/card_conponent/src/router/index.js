import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('../views/HomePage.vue')
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: () => import('../views/DashboardPage.vue')
  },
  {
    path: '/ranking',
    name: 'ranking',
    component: () => import('../views/RankingPage.vue')
  },
  {
    path: '/tracking',
    name: 'tracking',
    component: () => import('../views/TrackingPage.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
