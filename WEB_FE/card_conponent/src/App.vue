<template>
  <nav>
    <router-link to="/"><img src="@/assets/NavBarImage/home.svg" /></router-link> 
    <router-link to="/dashboard"><img src="@/assets/NavBarImage/dashboard.svg" /></router-link> 
    <router-link to="/tracking"><img src="@/assets/NavBarImage/tracking.svg" /></router-link> 
    <router-link to="/ranking"><img src="@/assets/NavBarImage/ranking.svg" /></router-link>
  </nav>
  <router-view />
</template>

<script>
</script>

<style>
  nav {
    position: absolute;
    height: 48px;
    left: 0%;
    right: 0%;
    top: 64px;

    background: #FFFFFF;
    box-shadow: 0px 4px 25px rgba(145, 85, 235, 0.03);
  }
</style>
