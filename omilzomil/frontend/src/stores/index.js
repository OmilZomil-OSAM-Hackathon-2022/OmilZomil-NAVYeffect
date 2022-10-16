import jwt from "@/common/jwt";
import userInfo from "@/common/userInfo";
import { createStore } from "vuex";

export default createStore({
  state: {
    darkMode:false,
    toekn:{
      accessToken:jwt.getToken(),
    },
    isAuthenticated: !!jwt.getToken(),
    userInfo:userInfo.getUser(),
  },
  getters: {
    getAccessToken(state) {
      return state.token.accessToken;
    },
    isAuthenticated(state) {
      return state.isAuthenticated
    },
    getUserInfo(state){
      return state.userInfo;
    },
    getDarkMode(state){
        return state.darkMode;
    }
  },
  mutations: {
    setDarkMode(state){
        state.darkMode = !state.darkMode;
    },
    logout: function (state) {
      state.token.accessToken = "";
      state.isAuthenticated = false;
      jwt.destroyToken();
      userInfo.destroyUser();
    },
    login: function (state, payload = {}) {
      state.token.accessToken = payload.accessToken;
      state.isAuthenticated = true;
      jwt.saveToken(payload.accessToken);
    },
  },
  actions:{
    
  }
});