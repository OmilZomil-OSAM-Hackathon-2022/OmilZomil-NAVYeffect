import axios from "axios";
import stores from '@/stores'

const http = axios.create({
    baseURL:'https://127.0.0.1:8080',
    // headers: { "content-type": "application/json" },
})

http.interceptors.request.use(
    config => {
      const isAuthenticated = stores.getters["isAuthenticated"]
      if (isAuthenticated) {
        config.headers.common["Authorization"] = stores.getters["getAccessToken"]
      }
      return config
    },
    error => {
      Promise.reject(error)
    }
  );

// http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";

export default http;