import axios from "axios";
import stores from '@/stores'

// const http = process.env.VUE_APP_LOCAL !== null ? axios.create({
//     baseURL:'https://127.0.0.1:80',
// }):axios.create({});

const http = axios.create();
http.interceptors.request.use(
    config => {
      const isAuthenticated = stores.getters["isAuthenticated"]
      if (isAuthenticated) {
        config.headers.common["Authorization"] = `Bearer ${stores.getters["getAccessToken"]}`
      }
      return config
    },
    error => {
      Promise.reject(error)
    }
  );

export default http;