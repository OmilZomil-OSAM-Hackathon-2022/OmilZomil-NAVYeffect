<template>
  <div class="card">
    <img
      src="@/assets/images/total-background.png"
      class="background-image"
    >
    <div class="content">
      <div class="title">
        불량 적발 인원
      </div>
      <div class="count">
        총&nbsp;<number
          :from="0"
          :to="totalCount"
          :duration="2"
          easing="Expo.easeOut"
        />
      </div>
      <div class="percent">
        지난 달 대비 <PercentTag
          :percent="percent"
          :reverse="true"
        />
      </div>
      <img
        class="face"
        src="@/assets/images/face-icon.png"
      >
      <img
        class="hand"
        src="@/assets/images/hand-icon.png"
      >
    </div>
  </div>
</template>

<script>
import PercentTag from '../common/PercentTag.vue';
export default {
    components: { PercentTag },
    props: {
        totalCount: {
            type: Number,
            default: 0
        },
        percent: {
            type: Number,
            default: 0
        }
    }
}
</script>

<style scoped>
.card{
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    position:relative;
}
.background-image{
    position:absolute;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius:20px;
    z-index:1;
}
.content{
    position:absolute;
    left:0px;
    top:0px;
    width:100%;
    height:100%;
    box-sizing: border-box;
    padding: 48px 44px;
    display:flex;
    flex-direction: column;
    align-items: flex-start;
    position:relative;
}
.title{
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 600;
    font-size: 24px;
    line-height: 28px;
    margin-bottom:38px
}
.count{
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 600;
    font-size: 20px;
    line-height: 23px;
    letter-spacing: 0.25px;
    margin-bottom:5px;
}
.percent{
    color:#9C9DB2;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 500;
    font-size: 10px;
    line-height: 12px;
    /* identical to box height */

    letter-spacing: 1.5px;
}
.face{
    position:absolute;
    right:70px;
    bottom:56px;
    z-index:90;
}
@keyframes salute {
        0% {
            /* transform: rotate(-30deg); */
            transform: skew(-20deg) rotate(-40deg);;
        }
        to {
            transform: skew(0deg) rotate(0deg);
            /* transform: rotate(0deg) */
        }
    }
.hand{
    position:absolute;
    z-index:100;
    right:130px;
    bottom:150px;
    animation:salute 2s;
}
</style>