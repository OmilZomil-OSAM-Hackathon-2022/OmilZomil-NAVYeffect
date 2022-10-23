<template>
  <div
    :class="[getDarkMode ? 'dark-mode' : '', 'main']"
  >
    <AppBar
      v-if="!$route.meta.hideAppBar"
      :style="{'margin-bottom':$route.meta.isLanding ? '0px':''}"
    />
    <router-view />
  </div>
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

@font-face {
  font-family:'Roboto';
  src: url('assets/fonts/Roboto-Thin.ttf') format('truetype');
  font-weight: 100;
}
@font-face {
  font-family:'Roboto';
  src: url('assets/fonts/Roboto-Light.ttf') format('truetype');
  font-weight: 300;
}
@font-face {
  font-family:'Roboto';
  src: url('assets/fonts/Roboto-Regular.ttf') format('truetype');
  font-weight: 400;
}
@font-face {
  font-family:'Roboto';
  src: url('assets/fonts/Roboto-Medium.ttf') format('truetype');
  font-weight: 500;
}
@font-face {
  font-family:'Roboto';
  src: url('assets/fonts/Roboto-Bold.ttf') format('truetype');
  font-weight: 700;
}
@font-face {
  font-family:'Roboto';
  src: url('assets/fonts/Roboto-Black.ttf') format('truetype');
  font-weight: 900;
}
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
  font-family: 'Roboto', Avenir, Helvetica, Arial, sans-serif !important;
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
