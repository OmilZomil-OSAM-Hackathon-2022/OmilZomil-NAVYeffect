import axios from "axios";
import stores from '@/stores'

const http = axios.create({baseURL:''});
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