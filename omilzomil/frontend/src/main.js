import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import store from "./stores";
import VueNumber from 'vue-number-animation'
import VueApexCharts from 'vue3-apexcharts';

import {
    Chart,
    registerables,
  } from 'chart.js'
  Chart.register(...registerables);
  
// Vue
const app = createApp(App)
axios.defaults.baseURL = 'https://127.0.0.1:8080';
app.config.globalProperties.$axios = axios; 
app.use(store)
app.use(VueApexCharts)
// app.componentx
app.use(VueNumber)
app.use(router).mount('#app')

