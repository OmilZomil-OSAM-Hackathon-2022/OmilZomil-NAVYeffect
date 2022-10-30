<template>
  <div class="wrap">
    <div class="load-map">
      <h1>영상처리 AI의 이미지 분석 과정</h1>
      <img
        src="@/assets/images/curve-background.svg"
        class="curve-background"
      >
      <div
        ref="viewport"
        class="video-wrap"
      >
        <video
          v-if="inViewport"
          class="ai-video"
          autoplay
          preload="auto"
        >
          <source src="@/assets/videos/AI_Proccess.mp4">
          브라우저가 영상을 지원하지 않습니다.
        </video>
      </div>
      <div class="desc desc1">
        <div class="desc-title">
          <img
            src="@/assets/icons/keycap1.svg"
            width="32"
          >사람 및 얼굴 인식
        </div>
        <div class="desc-content">
          정문 앞 카메라가 사람을 인식하는 순간부터 얼굴 인식 시행
        </div>
      </div>
      <div
        v-if="inViewport"
        class="result-card card"
      >
        <div class="img-stack">
          <img
            v-if="step2"
            src="@/assets/images/close-back.png"
            width="340"
            class="dress-image"
          >
          <div style="height:225px;border-radius: 19px;overflow: hidden;">
            <img
              v-if="!step2"
              src="@/assets/images/loading.gif"
              width="340"
              class="loading"
            >
          </div>
          <check-tag :is-check="step2" />
        </div>
        <div 
          v-if="!step2"
        >
          <h2>인식중...</h2>
        </div>
        <div
          v-if="step2" 
          class="progress-wrap"
        >
          <div class="progress sam">
            <div class="title">
              샘브레이
            </div>
            <div class="progress-back">
              <div class="progress-bar" />
            </div>
            <div style="display:flex;align-items:center;width:31px;justify-content:flex-end">
              <number
                :from="0"
                :to="11"
                :duration="2"
              />
              %
            </div>
          </div>
          <div class="progress jung">
            <div class="title">
              해군정복
            </div>
            <div class="progress-back">
              <div class="progress-bar" />
            </div>
            <div style="display:flex;align-items:center;width:31px;justify-content:flex-end">
              <number
                :from="0"
                :to="82"
                :duration="2"
              />
              %
            </div>
          </div>
          <div class="progress goon">
            <div class="title">
              전투복
            </div>
            <div class="progress-back">
              <div class="progress-bar" />
            </div>
            <div style="display:flex;align-items:center;width:31px;justify-content:flex-end">
              <number
                :from="0"
                :to="7"
                :duration="2"
              />
              %
            </div>
          </div>
        </div>
      </div>
      <div class="desc desc2">
        <div class="desc-title">
          <img
            src="@/assets/icons/keycap2.svg"
            width="32"
          >복장 분류
        </div>
        <div class="desc-content">
          현재 병사가 어느 복장을 착용하고 있는지 분류
        </div>
      </div>
      <div class="parts-wrap">
        <div class="card item">
          <div style="display:flex;align-items:center;gap:43px;">
            <img
              src="@/assets/icons/rank.png"
              width="56"
            >
            계급장
          </div>
          <check-tag
            :is-check="rank"
            :is-big="true"
          />
        </div>
        <div class="card item">
          <div style="display:flex;align-items:center;gap:43px;">
            <img
              src="@/assets/icons/name-tag.png"
              width="56"
            >
            이름표
          </div>
          <check-tag
            :is-check="nameTag"
            :is-big="true"
          />
        </div>
        <div class="card item">
          <div style="display:flex;align-items:center;gap:43px;">
            <img
              src="@/assets/icons/naka.png"
              width="56"
            >
            네카치프
          </div>
          <check-tag
            :is-check="naka"
            :is-big="true"
          />
        </div>
        <div class="card item">
          <div style="display:flex;align-items:center;gap:43px;">
            <img
              src="@/assets/icons/mahoo.png"
              width="56"
            >
            머플러
          </div>
          <check-tag
            :is-check="mahoo"
            :is-big="true"
          />
        </div>
      </div>
      <div class="desc desc3">
        <div class="desc-title">
          <img
            src="@/assets/icons/keycap3.svg"
            width="32"
          >군복 부착물 여부 검사
        </div>
        <div class="desc-content">
          분류된 복장에 따라 다른 AI모델을 사용하여 더욱 정확하게 군복 부착물을 검사
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import { useElementVisibility } from "@vueuse/core";
import CheckTag from '../CheckTag.vue';
export default {
  components: { CheckTag },
  setup() {
    const viewport = ref();
    const inViewport = useElementVisibility(viewport);
    return {
      viewport,
      inViewport,
    };
  },
  data(){
    return{
        step2:false,
        rank:true,
        nameTag:true,
        naka:true,
        mahoo:true,
    }
  },
  watch:{
    inViewport(){
        if(this.inViewport){
            setTimeout(()=>{
                this.step2 = true;
            }, 6000);
            setTimeout(()=>{
                this.naka = false;
            }, 4000);
            setTimeout(()=>{
                this.mahoo = false;
            }, 8000);
            setTimeout(()=>{
                this.nameTag = false;
            }, 13000);
        }else{
            this.naka = true;
            this.mahoo = true;
            this.nameTag = true;
            this.rank = true;
            this.step2 = false;
        }
    }
  },
};
</script>

<style scoped>
@keyframes fadein{
    from{
        opacity: 0;
    }to{
        opacity: 1;
    }
}
@keyframes move1{
    from{
        transform: translateX(-100px);
    }to{
        transform: translateX(0px);
    }
}
@keyframes move2{
    from{
        transform: translateX(-300px);
    }to{
        transform: translateX(0px);
    }
}
@keyframes move3{
    from{
        transform: translateX(-30px);
    }to{
        transform: translateX(0px);
    }
}
.item .check-tag{
    width:50px;
    height:46px;
    border-radius: 8px;
}
.item .check-tag img{
    width:24px !important;
}
.item{
    display:flex;
    flex-direction: row;
    width:500px;
    height:100px;
    justify-content: space-between;
    padding:0px 33px;
    box-sizing:border-box;
    font-weight: 600;
    font-size: 24px;
    line-height: 28px;
    letter-spacing: 0.15px;
}
.parts-wrap{
    display:flex;
    flex-direction: column;
    gap:25px;
    position:absolute;
    top:670px;
    left:100px;
}
.progress-wrap{
    margin-top:20px;
    display:flex;
    flex-direction: column;
    align-items: flex-end;
    gap:20px;
}
.sam{
    color:#4471FB;
}
.sam .progress-bar{
    height:22px;
    width:30px;
    background:#4471FB;
    border-radius: 5px;
    animation: move1 2s;
}
.jung{
    color:#585767;
}
.jung .progress-bar{
    height:22px;
    width:180px;
    background: #585767;
    border-radius: 5px;
    animation:move2 2s;
}
.goon{
    color:#1DCB9D;
}
.goon .progress-bar{
    background:#1DCB9D;
    border-radius: 5px;
    height:22px;
    width:15px;
    animation: move3 2s;
}
.progress{
    display:flex;
    align-items: center;
    font-weight: 600;
    font-size: 16px;
    line-height: 19px;

    letter-spacing: 0.15px;
    font-size: 16px;
}
.progress .title{
    margin-right:15px;
}
.progress-back{
    width: 220px;
    height: 22px;
    background: #F4F5FA;
    border-radius: 5px;
    overflow: hidden;

    margin-right:5px;
}
.dress-image{
    animation: fadein 2s;
}
.loading{
    border-radius: 19px;;
}
.img-stack{
    position: relative;
    display:flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
}
.img-stack .check-tag{
    position:absolute;
    right:15px;
    top:15px;
}
.result-card{
    width:400px;
    height:450px;
    position:absolute;
    top:380px;
    right:80px;
    box-sizing:border-box;
    padding:30px;
    display:flex;
    flex-direction: column;
    justify-content: flex-start;
}
.video-wrap {
  position: absolute;
  z-index: 10;
  height: 420px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.04), 0px 4px 8px rgba(0, 0, 0, 0.05);
  border-radius: 20px;
  overflow: hidden;
  display: flex;
  align-items: flex-end;
  top: 100px;
  left: 100px;
}
.ai-video {
  /* width: 420px; */
  height: 500px;
}
h1 {
  font-weight: 700;
  font-size: 32px;
  line-height: 150%;
  width: 100%;
  color: #9155eb;
  display: flex;
  margin: 87px 0px 0px 0px;
}
.load-map {
  height: 1425px;
  position: relative;
}
.curve-background {
  position: absolute;
  top: 300px;
  left: 120px;
}

.desc{
    position:absolute;
    display:flex;
    flex-direction: column;
    align-items: flex-start;
    gap:12px;
}
.desc1{
    top:200px;
    left:450px;
}
.desc2{
    top:900px;
    right:70px;
}
.desc3{
    top: 1180px;
    left:100px;
}
.desc-title{
    font-weight: 700;
    font-size: 24px;
    line-height: 28px;
    letter-spacing: 0.15px;
    display:flex;
    align-items:center;
    gap:12px;
}
.desc-content{
    font-weight: 500;
    font-size: 20px;
    line-height: 23px;
    letter-spacing: 0.15px;
    margin-left:44px;
}
</style>
