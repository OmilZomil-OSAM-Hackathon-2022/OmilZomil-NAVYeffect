import { createStore } from "vuex";

export default createStore({
  state: {
    darkMode:false,
  },
  getters: {
    getDarkMode(state){
        return state.darkMode;
    }
  },
  mutations: {
    setDarkMode(state){
        state.darkMode = !state.darkMode;
    }
  }
});