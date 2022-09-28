<template>
  <div :style="{background: (getDarkMode? '#32313F':'#F4F5FA')}">
    <AppBar/>
    <router-view></router-view>
  </div>
  <!-- <login-page /> -->
</template>

<script>
import AppBar from './components/AppBar.vue';
// import { useStore } from "vuex"

// import LoginPage from "./views/LoginPage.vue";
export default {
  name: "App",
  components: { AppBar },
  computed: {
    getDarkMode () {
      return this.$store.getters.getDarkMode;
    }
  },
};
</script>

<style>
@import '@/assets/styles/common.css';
/* background: #32313F; */
html,
body,
#app {
  margin: 0px;
  height: 100%;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
