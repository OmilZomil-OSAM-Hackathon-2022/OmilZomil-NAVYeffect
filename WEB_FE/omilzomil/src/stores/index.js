import { createStore } from "vuex";

export default createStore({
  state: {
    darkMode:false,
  },
  getters: {
    getDarkMode(){
        return darkMode;
    }
  },
  mutations: {
    setDarkMode(){
        state.darkMode = !state.darkMode;
    }
  }
});