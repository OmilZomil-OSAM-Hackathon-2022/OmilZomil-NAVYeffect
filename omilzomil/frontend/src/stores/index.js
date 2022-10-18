import jwt from "@/common/jwt";
import userInfo from "@/common/userInfo";
import { createStore } from "vuex";

export default createStore({
  state: {
    darkMode:false,
    token:{
      accessToken:jwt.getToken(),
    },
    isAuthenticated: !!jwt.getToken(),
    user:userInfo.getUserInfo(),
  },
  getters: {
    getAccessToken(state) {
      return state.token.accessToken;
    },
    isAuthenticated(state) {
      return state.isAuthenticated
    },
    getUser(state){
      return state.user;
    },
    getDarkMode(state){
        return state.darkMode;
    }
  },
  mutations: {
    setDarkMode(state){
        state.darkMode = !state.darkMode;
    },
    logout(state) {
      state.token.accessToken = "";
      state.isAuthenticated = false;
      jwt.destroyToken();
      userInfo.destroyUser();
    },
    login(state, payload = {}) {
      state.token.accessToken = payload.accessToken;
      state.isAuthenticated = true;
      jwt.saveToken(payload.accessToken);
    },
    setUser(state, payload = {}){
      state.user = payload;
      userInfo.saveUser(payload);
    }
  },
});