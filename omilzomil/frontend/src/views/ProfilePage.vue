<template>
  <div class="wrap">
    <div class="card">
      <div class="nav">
        <router-link to="/profile">
          프로필 수정
        </router-link>
        <router-link
          v-if="user.role > 2"
          to="/profile/userManagement"
        >
          사용자 관리
        </router-link>
        <router-link
          v-if="user.role > 2"
          to="/profile/unitManagement"
        >
          부대 관리
        </router-link>
        <router-link
          v-if="user.role > 2"
          to="/profile/GuardroomManagement"
        >
          위병소 관리
        </router-link>
        <router-link
          v-if="user.role > 2"
          to="/profile/VacationManagement"
        >
          휴가 관리
        </router-link>
      </div>
      <router-view v-slot="{Component, route}">
        <transition
          :enter-active-class="route.meta.enterClass"
          :leave-active-class="route.meta.leaveClass"
        >
          <component :is="Component" />
        </transition>
      </router-view>
    </div>
  </div>
</template>

<script>
import 'animate.css'; 
export default {
  computed:{
    user(){
        return this.$store.getters.getUser;
    }
  }
}
</script>

<style scoped>
.card{
    overflow: hidden;
    height:812px;
    padding:0px 76px;
    box-sizing: border-box;
    flex-direction:column;
    position:relative;
    margin-bottom:40px;
    justify-content: flex-start;
}
.nav{
    display:flex;
    width:100%;
    justify-content: space-around;
    border-bottom: 1.5px solid #F9F9FB;
}

a{
    font-weight: 700;
    font-size: 16px;
    line-height: 19px;
    letter-spacing: 0.15px;

    color: #ABACC0;

    padding:20px 0px;
    box-sizing: border-box;
}

.router-link-exact-active{
    color:#9155EB;
    border-bottom: #9155EB solid 4px;
}
/* .fade-enter-from,
.fade-leave-to{
    opacity:0;
}

.fade-enter-active,
.fade-leave-active{
    transition: opacity 0.5s ease-out;
} */

.page{
    width:100%;
    position:absolute;
    top:60px;
    display:flex;
    box-sizing: border-box;
    height:100%;
}
</style>
<!-- <style>
.page{
    position:absolute;
    top:0px;
}
</style> -->