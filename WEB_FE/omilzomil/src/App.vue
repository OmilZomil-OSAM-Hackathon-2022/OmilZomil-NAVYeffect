<template>
  <AppBar/>
  <!-- <router-view></router-view> -->
  <!-- <login-page /> -->
</template>

<script>
import AppBar from './components/AppBar.vue';
// import LoginPage from "./views/LoginPage.vue";
export default {
  name: "App",
  components: { AppBar },
};
</script>

<style>
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
