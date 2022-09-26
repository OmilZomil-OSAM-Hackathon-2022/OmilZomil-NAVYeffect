<template>
  <div class="app-bar">
    <div class="wrap">
        <div class="top">
            <div class="logo">
                <img width="30" src="@/assets/logo.svg"/>
                <h1>OMIL-ZOMIL</h1>
            </div>
            <div></div>
        </div>
        <div></div>
    </div>
  </div>
</template>

<script>
export default {
    name:"AppBar",
}
// src="@/assets/styles/common.css"
</script>

<style scoped >
@import '@/assets/styles/common.css';
.app-bar{
    /* width:100%; */
    background: #FFFFFF;
    box-shadow: 0px 4px 25px rgba(145, 85, 235, 0.03);
    height:48px;
    display:flex;
    flex-direction: column;
    align-items: center;
}
.top{
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
</style>