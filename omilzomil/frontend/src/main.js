import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import axios from 'axios'
import store from "./stores";
import VueNumber from 'vue-number-animation'
import VueApexCharts from 'vue3-apexcharts';
import http from './common/http';
import {
    Chart,
    registerables,
  } from 'chart.js'
  Chart.register(...registerables);
  
// Vue
const app = createApp(App)
app.config.globalProperties.$axios = http; 
app.use(store)
app.use(VueApexCharts)
app.use(VueNumber)
app.use(router).mount('#app')

