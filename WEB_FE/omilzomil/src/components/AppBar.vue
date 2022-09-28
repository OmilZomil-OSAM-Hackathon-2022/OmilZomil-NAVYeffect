<template>
  <!-- :style="{background: (getDarkMode? '#312D4B':'#FFFFFF')}" -->
  <div class="app-bar">
    <div class="wrap">
        <div class="top">
            <router-link to="/" style="text-decoration:none;" class="logo">
                <img width="30" src="@/assets/logo.svg"/>
                <h1>OMIL-ZOMIL</h1>
            </router-link>
            <div class="options">
                <div>
                    <input type="checkbox" id="toggle" @change="setDarkMode" hidden> 
                    <label for="toggle" class="toggleSwitch">
                        <span class="toggleButton"></span>
                        <img class="toogleIcon"/>
                    </label>
                </div>

                <button>
                  <img width="16" src="@/assets/icons/bell-outline.svg"/>
                </button>
                <button>
                  <img width="16" src="@/assets/icons/mdi_magnify.svg"/>
                </button>
                <input type="text" class="search" placeholder="검색"/>
                <router-link class="profile" to="/">
                  <img width="32" src="@/assets/icons/mdi_account-circle.svg"/>
                  <div class="user-name">
                    {{userName}}님
                  </div>
                </router-link>
            </div>
        </div>
        <div class="nav-menu">
          <router-link class="nav-item" to="/">
            <img src="@/assets/icons/mdi_home.svg"/>홈
          </router-link>
          <router-link class="nav-item" to="/">
            <img src="@/assets/icons/mdi_view-dashboard.svg"/>대쉬보드
          </router-link>
          <router-link class="nav-item" to="/">
            <img src="@/assets/icons/account-group.svg"/>부대인원조회
          </router-link>
          <router-link class="nav-item" to="/">
            <img src="@/assets/icons/trophy-variant.svg"/>랭킹
          </router-link>
        </div>
    </div>
  </div>
</template>

<script>
export default {
    name:"AppBar",
    data(){
      return {
        userName: "김민섭",
      }
    },
    methods:{
      setDarkMode(){
        // console.log("test");
        return this.$store.commit('setDarkMode');
      },
    },
    computed: {
      getDarkMode () {
        return this.$store.getters.getDarkMode;
      }
    },
}
// src="@/assets/styles/common.css"
</script>

<style scoped >
/* @import '@/assets/styles/common.css'; */
.app-bar{
    /* width:100%; */
    background: var(--color-appbar);
    box-shadow: 0px 4px 25px rgba(145, 85, 235, 0.03);
    height:112px;
    display:flex;
    flex-direction: column;
    align-items: center;
}
.top{
    height:64px;
    display:flex;
    justify-content: space-between;
    align-items: center;
}
.top h1{
    width: 111px;
    height: 22px;

    font-family: 'Inter';
    font-style: normal;
    font-weight: 700;
    font-size: 18px;
    line-height: 22px;

    color: #9155EB;
}
.top .logo{
    display:flex;
    align-items: center;
}
.top .logo img{
    margin-right:5px;
}
.top .options{
    height:100%;
    display:flex;
    align-items: center;
    gap:8px;
}


/* 토글 스위치 */
.toggleSwitch {
  width: 64px;
  /* margin: 2rem; */
  height: 28px;
  display: block;
  position: relative;
  border-radius: 40px;
  background-color: #fff;
  /* box-shadow: 0 0 1rem 3px rgba(0 0 0 / 15%); */
  border: 1px solid #D9D8E8;
  cursor: pointer;
  /* background: url("@/assets/icons/weather-sunny.svg") no-repeat scroll 20px center; */
  /* background-position: right 4px center; */
}

.toggleSwitch .toggleButton {
  width: 20px;
  height: 20px;
  position: absolute;
  top: 50%;
  left: 4px;
  transform: translateY(-50%);
  border-radius: 50%;
  background: rgba(145, 85, 235, 0.2);
  border:#9155EB solid 2px;
}

.toggleSwitch .toogleIcon{
  width: 20px;
  height: 20px;
  position: absolute;
  top: 50%;
  right: 4px;
  transform: translateY(-50%);
  content: url("@/assets/icons/weather-sunny.svg")
}

#toggle:checked ~ .toggleSwitch {
  /* background: url("@/assets/icons/weather-night.svg") no-repeat scroll 20px center; */
  /* background-position: right 4px center; */
  background: #32313F;
}


#toggle:checked ~ .toggleSwitch .toggleButton {
  left: calc(100% - 28px);
  background: rgba(183, 134, 255, 0.2);

  border: #B786FF solid 2px;
}

#toggle:checked ~ .toggleSwitch .toogleIcon{
  left: 4px;
  content: url("@/assets/icons/weather-night.svg")
}


.toggleSwitch, .toggleButton {
  transition: all 0.2s ease-in;
}

/* 버튼 */
button{
  width:28px;
  height:28px;
  background: rgba(145, 85, 235, 0.2);
  border-radius: 4px;
  border:none;
  display:flex;
  align-items:center;
  justify-content: center;
}

.profile{
  display:flex;
  height:100%;
  align-items: center;
  
  text-decoration: none;
}

.profile .user-name{
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 700;
  font-size: 16px;
  line-height: 19px;
  /* identical to box height */

  display: flex;
  align-items: center;
  text-align: right;
  letter-spacing: 0.15px;

  /* Primary */

  color: #9155EB;


  /* Inside auto layout */

  /* flex: none;
  order: 1;
  flex-grow: 0; */
  margin-left:4px;
}

.search{
  box-sizing: border-box;

  /* Auto layout */

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 7px 10px;

  width: 224px;
  height: 28px;

  background: var(--color-input);
  /* Dark8 */

  border: 1px solid var(--color-input-border);
  border-radius: 4px;

  /* Inside auto layout */

  /* flex: none;
  order: 1;
  flex-grow: 0; */
}
.search::placeholder{
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  /* line-height: 14px; */
  /* identical to box height */

  /* letter-spacing: 0.4px; */

  /* Dark5 */

  color: #9C9DB2;
}

.nav-menu{
  height:48px;
  display:flex;
  gap:36px;
  align-items:center;
}

.nav-menu .nav-item{
  /* box-sizing:border-box; */
  padding:12px;
  text-decoration:none;
  gap:8px;
  /* Subtitle 1 */

  font-family: 'Roboto';
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
  /* identical to box height */

  display: flex;
  align-items: center;
  letter-spacing: 0.15px;

  /* Dark6 */

  color: #ABACC0;
}
</style>