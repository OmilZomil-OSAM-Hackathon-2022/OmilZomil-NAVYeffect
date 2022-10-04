<template>
  <transition 
    name="overlay"
    appear
  >
    <div
      class="overlay"
      @click.self="$emit('close',event)"
    >
      <div class="overlay-card card">
        <img
          src="@/assets/images/test.png"
        >
        <div class="detail">
          <div class="info">
            <div class="division">
              소속 : 대한민군 {{ item.division }}
            </div>
            <div class="uClass">
              계급 : {{ item.uClass }}
            </div>
            <div class="uName">
              이름 : {{ item.uName }}
            </div>
          </div>
          <div class="time">
            시간 : {{ item.time }}
          </div>
          <div class="dress-type">
            복장 : 
          </div>
        </div>
        <img
          class="close"
          src="@/assets/icons/close-thick.svg"
          @click="$emit('close')"
        >
      </div>
    </div>
  </transition>
</template>

<script>
export default {
    props:{
        item:{
            type:Object,
            default:null,
        },
    },
    emits:["close"]
}
</script>

<style scoped>

.overlay{
  position: fixed;
  /* display:none; */
  display:flex;
  justify-content: center;
  align-items: center;
  width:100%;
  height:100%;
  top:0;
  left:0;
  right:0;
  bottom:0;
  background-color:rgba(0,0,0,0.5);
  z-index:30;
}
.overlay-card{
  position: relative;
  box-sizing: border-box;
  width:1080px;
  height:600px;
  padding:40px;
  display:flex;
  gap:40px;
}
.overlay-card img{
  width:380px;
  height:100%;
}
.overlay-card .detail{
  width:580px;
  height:100%;
  display:flex;
  flex-direction: column;
  align-items: flex-start;
}
.overlay-card .detail .info{
  display:flex;
  gap:30px;
}
.overlay-card .close{
  position:absolute;
  right:20px;
  top:20px;
  width:16px;
  height:16px;
}

.overlay-enter-active, .overlay-leave-active {
    transition: opacity 0.4s;
}
.overlay-enter-active .overlay-card, .overlay-leave-active .overlay-card {
    transition: opacity 0.4s, transform 0.4s;
}
.overlay-leave-active {
    transition: opacity 0.6s ease 0.4s;
}

.overlay-enter, .overlay-leave-to {
    opacity: 0;
}
.overlay-enter .overlay-card, .overlay-leave-to .overlay-card {
    opacity: 0;
    transform: translateY(-20px);
}
</style>