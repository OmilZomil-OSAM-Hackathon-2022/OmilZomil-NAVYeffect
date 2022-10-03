<template>
  <div :class="[getDarkMode ? 'dark-mode':'','main']">
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
/* :root{
} */
:root{
  --color-background:#F4F5FA;
  --color-appbar:#FFFFFF;
  --color-card:#FFFFFF;
  --color-input:#FFFFFF;
  --color-input-border:#D9D8E8;
}
.dark-mode{
  --color-background:#28243D;
  --color-appbar:#312D4B;
  --color-card:#312D4B;
  --color-input:#585767;
  --color-input-border:#78798D;
  color:white;
}
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
.main{
  display:flex;
  flex-direction: column;
  align-items: center;
  height: 100%;
  background:var(--color-background);
  width:100%;
}
</style>
