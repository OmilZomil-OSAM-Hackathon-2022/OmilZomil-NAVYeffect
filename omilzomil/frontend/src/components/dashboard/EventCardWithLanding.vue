<template>
  <div class="card">
    <button class="x" />
    <div
      class="textbox"
      :style="{ 'margin-top': photo != 1 ? '30px' : '' }"
    >
      <div
        class="text1"
        :style="{ 'font-size': photo != 1 ? '16px' : '' }"
      >
        {{ photo == 1 ? "계룡대근무지원단 본부대대" : "김민섭" }}
      </div>
      <div
        class="text2"
        :style="{ 'font-size': photo != 1 ? '12px' : '' }"
      >
        {{
          photo == 1
            ? "전체 부대 중 외적 군기 1등을 축하합니다."
            : "이번 달 소속 부대의 으뜸 병사입니다!"
        }}
      </div>
    </div>
    <div
      v-if="photo == 1"
      class="image"
    >
      <img
        class="back"
        src="@/assets/images/fire/back.svg"
      >
      <img
        class="one"
        src="@/assets/images/fire/one.svg"
      >
      <img
        class="two"
        src="@/assets/images/fire/two.svg"
      >
      <img
        class="three"
        src="@/assets/images/fire/three.svg"
      >
      <img
        class="four"
        src="@/assets/images/fire/four.svg"
      >
      <img
        class="five"
        src="@/assets/images/fire/red.svg"
      >
      <img
        class="six"
        src="@/assets/images/fire/yellow.svg"
      >
      <img
        class="seven"
        src="@/assets/images/fire/red.svg"
      >
      <img
        class="eight"
        src="@/assets/images/fire/yellow.svg"
      >
      <img
        class="nine"
        src="@/assets/images/fire/blue.svg"
      >
    </div>
    <div
      v-else
      class="photoclap"
    >
      <img class="photoback">
      <img
        class="photo"
        src="@/assets/images/test.png"
      >
      <img
        class="backhand"
        src="@/assets/images/clap/back.svg"
      >
      <img
        class="fronthand"
        src="@/assets/images/clap/front.svg"
      >
      <img
        class="clapeffect"
        src="@/assets/images/clap/effect.svg"
      >
    </div>
  </div>
</template>

<script>
export default {
  props: {
    photo: {
      type: Number,
      default: 1,
    },
  },
};
</script>

<style scoped>
@keyframes boom {
  0% {
    transform: scale(0.8);
    transform-origin: 0% 100%;
  }
  50% {
    transform: scale(1);
    transform-origin: 0% 100%;
  }
  /* 100% {
              transform: scale(0.9);
              transform-origin: 0% 100%;    
          } */
}
@keyframes scale-up-br {
  0% {
    transform: scale(0.2);
    transform-origin: 100% 100%;
  }
  100% {
    transform: scale(1);
    transform-origin: 100% 100%;
  }
}
@keyframes scale-up-bl {
  0% {
    transform: scale(0.2);
    transform-origin: 0% 100%;
  }
  100% {
    transform: scale(1);
    transform-origin: 0% 100%;
  }
}
@keyframes slide-tr {
  0% {
    transform-origin: 0% 100%;
    transform: scale(0.2) translateY(80px) translateX(-60%);
  }
  100% {
    transform-origin: 100% 100%;
    transform: scale(1) translateY(0) translateX(0);
  }
}
@keyframes slide-right {
  0% {
    transform-origin: 0% 0%;
    transform: scaleX(0.3) translateY(40px) translateX(-80px);
  }
  100% {
    transform-origin: 0% 0%;
    transform: scaleX(1) translateY(0) translateX(0px);
  }
}
@keyframes ball {
  0% {
    left: 34.62%;
    right: 57.87%;
    top: 52.99%;
    bottom: 39.49%;
  }
}
@keyframes shake1 {
  from {
    transform: scale(0.9) rotate(-5deg);
    /* transform: translateY(100px); */
    /* opacity: 0; */
  }
  to {
    transform: scale(1) rotate(0);
    /* transform: translateY(0); */
    /* opacity: 1; */
  }
}
@keyframes shake2 {
  from {
    transform: scale(1.1) rotate(5deg);
    /* transform: translateY(100px); */
    /* opacity: 0; */
  }
  to {
    transform: scale(1) rotate(0);
    /* transform: translateY(0); */
    /* opacity: 1; */
  }
}
.card {
  position: relative;
  display: flex;
  width: 400px;
  height: 600px;
  gap: 50px;
  flex-direction: column;

  background: linear-gradient(180deg, #47237d 0%, #623fac 49.83%, #47237d 100%);
}
.card .textbox {
  display: flex;
  width: 100%;
  gap: 5px;
  z-index: 1;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0px 10px;
  box-sizing: border-box;
}
.card .textbox .text1 {
  font-family: "Roboto";
  font-style: normal;
  font-weight: 700;
  font-size: 20px;
  line-height: 28px;
  text-align: center;
  word-break: normal;
  color: #f9f9fb;
  width: 100%;
}
.card .textbox .text2 {
  font-family: "Roboto";
  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  line-height: 23px;
  text-align: center;
  letter-spacing: -0.055em;
  color: #f9f9fb;
  white-space: nowrap;
  /* word-break:normal; */
}
.card .image {
  position: relative;
  width: 234px;
  height: 234px;
}
.card .image .back {
  position: absolute;
  left: 8.04%;
  right: 38.33%;
  top: 38.05%;
  bottom: 6.37%;
  animation: boom 2.5s cubic-bezier(0.39, 0.575, 0.565, 1) both;
}
.card .image .one {
  position: absolute;
  z-index: 1;
  left: 23.08%;
  right: 61.34%;
  top: 6.41%;
  bottom: 49.74%;
  animation: scale-up-br 1.5s cubic-bezier(0.39, 0.575, 0.565, 1) both;
}
.card .image .two {
  position: absolute;
  z-index: 2;
  left: 43.16%;
  right: 1.1%;
  top: 44.87%;
  bottom: 28.61%;
  animation: scale-up-bl 1.5s cubic-bezier(0.39, 0.575, 0.565, 1) both;
}
.card .image .three {
  position: absolute;
  left: 39.61%;
  right: 37.47%;
  top: 6.5%;
  bottom: 58.82%;
  animation: slide-tr 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}
.card .image .four {
  position: absolute;
  left: 61.5%;
  right: 8.89%;
  top: 33.87%;
  bottom: 52.7%;
  animation: slide-right 1.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}
.card .image .five {
  position: absolute;
  left: 11.64%;
  right: 80.84%;
  top: 21.58%;
  bottom: 70.9%;
  animation: ball 1.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}
.card .image .six {
  position: absolute;
  left: 40.17%;
  right: 52.31%;
  top: 6.41%;
  bottom: 86.07%;
  animation: ball 1.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}
.card .image .seven {
  position: absolute;
  left: 70.69%;
  right: 21.79%;
  top: 18.16%;
  bottom: 74.32%;
  animation: ball 1.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}
.card .image .eight {
  position: absolute;
  left: 73.84%;
  right: 18.64%;
  top: 67.82%;
  bottom: 24.66%;
  animation: ball 1.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}
.card .image .nine {
  position: absolute;
  left: 42.98%;
  right: 49.5%;
  top: 46.24%;
  bottom: 46.24%;
  animation: ball 1.5s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}
.card .x {
  background: url("@/assets/images/x.svg") no-repeat;
  position: absolute;
  border: none;
  cursor: pointer;
  top: 14px;
  right: 15px;
  width: 24px;
  height: 24px;
}
.card .photoclap {
  position: relative;
  width: 400px;
  height: 236px;
}
.card .photoclap .photoback {
  position: absolute;
  width: 136px;
  height: 136px;
  top: 0;
  left: 135px;
  filter: blur(16px);
  border-radius: 165px;
  background: rgba(255, 255, 255, 0.5);
  animation: blink 1.5s ease-in-out infinite alternate;
}
.card .photoclap .photo {
  position: absolute;
  width: 136px;
  height: 136px;
  top: 0;
  left: 135px;
  border-radius: 165px;
}
.card .fronthand {
  position: absolute;
  z-index: 3;
  /* height: 93.42px; */
  width: 40.06px;
  left: 238px;
  top: 110px;
  animation: shake2 0.2s infinite alternate;
}
.card .backhand {
  position: absolute;
  /* height:92.23px; */
  width: 30px;
  left: 230px;
  top: 100px;
  z-index: 2;
  animation: shake1 0.2s infinite alternate;
}
.card .clapeffect {
  position: absolute;
  width: 17.79px;
  /* height:30.03px; */
  left: 230px;
  top: 90px;
  z-index: 2;
  animation: effect 0.2s infinite alternate;
}
</style>
