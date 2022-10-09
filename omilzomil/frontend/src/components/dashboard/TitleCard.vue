<template>
  <div class="card title-card">
    <div class="title-wrap">
      <div class="title">
        필승! <h1>{{ title }}</h1> 입니다
      </div>
      <div class="sub-title">
        오늘도 전군 군기확립을 위해 노력하는 오밀조밀이 되겠습니다!
      </div>
    </div>
    <img
      class="thumb"
      src="@/assets/images/Thumb_up.svg"
    >
  </div>
</template>

<script>
export default {
  props:{
    title:{
      type:String,
      default:null,
    }
  }
}
</script>

<style scoped>
.title-card{
  box-sizing: border-box;
  display:flex;
  align-items: center;
  justify-content: flex-start;
  padding-left:44px;
  position:relative;
  overflow:hidden;
}
@keyframes moveLeft {
        0% {
            transform: translate3d(100px, 0, 0);
        }
        to {
            transform: translate3d(0,0,0);
        }
    }
.title-card .thumb{
  position:absolute;
  right:0px;
  animation:moveLeft 1.2s;
}
.title{
  display: flex;
  align-items: flex-end;
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 700;
  font-size: 14px;
  line-height: 16px;
  text-align: center;
  letter-spacing: 0.1px;
}
.title h1{
  margin:0px;
  color:#9155EB;
  margin:0px 5px;
  /* margin-bottom: 5px; */

  font-family: 'Roboto';
font-style: normal;
font-weight: 700;
font-size: 24px;
line-height: 28px;
text-align: center;
}
.sub-title{
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 0.25px;
}
</style>