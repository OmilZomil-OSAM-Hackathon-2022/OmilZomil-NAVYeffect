<template>
  <head>
    <!-- <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
    > -->
  </head>
  <div
    :class="[getDarkMode ? 'dark-mode' : '', 'main']"
  >
    <AppBar v-if="!$route.meta.hideAppBar" />
    <router-view />
  </div>
  <!-- <login-page /> -->
</template>

<script>
import AppBar from "./components/AppBar.vue";
// import { useStore } from "vuex"

// import LoginPage from "./views/LoginPage.vue";
export default {
  name: "App",
  components: { AppBar },
  computed: {
    getDarkMode() {
      return this.$store.getters.getDarkMode;
    },
  },
};
</script>

<style>
@import "@/assets/styles/common.css";
@import url("http://fonts.googleapis.com/css?family=Roboto:400,300,100,500,700");
/* background: #32313F; */
/* :root{
} */
:root {
  color:#585767;
  --color:#585767;
  --color-background: #f4f5fa;
  --color-appbar: #ffffff;
  --color-card: #ffffff;
  --color-input: #ffffff;
  --color-input-border: #d9d8e8;
  --color-state-card:#F9F9FB;
}
.dark-mode {
  --color-background: #28243d;
  --color-appbar: #312d4b;
  --color-card: #312d4b;
  --color-input: #312D4B;
  --color-input-border: #78798D;
  --color-state-card:#2C2845;
  color: white;
  --color:white;
}
html,
body,
#app {
  margin: 0px;
  height: 100%;
}
#app {
  font-family: 'Roboto', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: auto;
  min-height: 100%;

  background: var(--color-background);
  width: 100%;
}


a{
  text-decoration:none;
}
</style>
