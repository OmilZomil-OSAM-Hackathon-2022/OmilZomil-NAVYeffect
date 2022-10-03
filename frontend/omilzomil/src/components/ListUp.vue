<template>
  <div class="card-list card">
    <div class="list">
      <div class="list-header">
        <div style="width:80px">
          사진
        </div>
        <div style="width:80px;display: flex;justify-content: center;">
          소속 / 계급 / 이름
        </div>
        <div style="width:65px">
          시간
        </div>
        <div style="width:100px">
          복장
        </div>
        <div style="width:55px">
          두발상태
        </div>
        <div style="width:55px">
          복장상태
        </div>
        <div style="width:43px;display: flex;justify-content: flex-end;">
          자세히보기
        </div>
      </div>
      <div class="list-body">
        <div
          v-for="(item,index) in dummy"
          :key="index"
          class="list-item"
        >
          <img
            class="thumb"
            src="@/assets/images/test.png"
          >
          <div class="info">
            <div
              class="division"
              :style="{color:getDivisionColor(item.division)}"
            >
              대한민국 {{ item.division }}
            </div>
            <div class="name">
              {{ item.uClass }} {{ item.uName }}
            </div>
          </div>
          <div class="time">
            {{ item.time }}
          </div>
          <div class="dress-type">
            <IconBase
              :width="16"
              :height="16"
              :viewBox="'0 0 16 16'"
            >
              <TshirtIcon />
            </IconBase>
            {{ item.dressType }}
          </div>
          <div
            class="hair-state"
            :style="{color:item.hairStatus?'#3FC6B8':'#FF5467'}"
          >
            <img
              v-if="item.hairStatus"
              src="@/assets/icons/check-circle.svg"
            >
            <img
              v-if="!item.hairStatus"
              src="@/assets/icons/error-circle.svg"
            >
            {{ item.hairStatus ? "양호":"불량" }}
          </div>
          <div
            class="dress-state"
            :style="{color:item.dressStatus?'#3FC6B8':'#FF5467'}"
          >
            <img
              v-if="item.dressStatus"
              src="@/assets/icons/check-circle.svg"
            >
            <img
              v-if="!item.dressStatus"
              src="@/assets/icons/error-circle.svg"
            >
            {{ item.dressStatus ? "양호":"불량" }}
          </div>
          <a
            class="more"
            @click="openDetail(item)"
          >
            <img src="@/assets/icons/dots.svg">
          </a>
        </div>
      </div>
    </div>
  </div>

  <div
    v-show="isDetail"
    class="overlay"
  >
    <div class="overlay-card card">
      <img
        src="@/assets/images/test.png"
      >
      <div class="detail">
        <div class="info">
          <div class="division">
            소속 : 대한민군 {{ detail.division }}
          </div>
          <div class="uClass">
            계급 : {{ detail.uClass }}
          </div>
          <div class="uName">
            이름 : {{ detail.uName }}
          </div>
        </div>
        <div class="time">
          시간 : {{ detail.time }}
        </div>
        <div class="dress-type">
          복장 : 
        </div>
      </div>
      <img
        class="close"
        src="@/assets/icons/close-thick.svg"
        @click="closeDetail"
      >
    </div>
  </div>
</template>

<script>
import TshirtIcon from "../assets/icons/tshirt-icon.vue";
import IconBase from "./IconBase.vue";

class Item{
  constructor(){
    this.imageUrl = "@/assets/images/test.png",
    this.division ="해군",
    this.uClass = "일병",
    this.uName= "나해군",
    this.time= "2020-06-24 22:57:36",
    this.dressType= "해군 군복",
    this.hairStatus= true,
    this.dressStatus= false
  }
}

export default {
    components: { TshirtIcon, IconBase },
    data() {
        return {
            detail: new Item(),
            isDetail: false,
            dummy: [
                new Item(),
                new Item(),
                new Item(),
            ]
        };
    },
    methods: {
        getDivisionColor(division) {
            if (division == "해군")
                return "#528EE9";
            else if (division == "육군")
                return "#";
            else if (division == "공군")
                return "#";
            else if (division == "해병대")
                return "#";
            else
                return "#";
        },
        closeDetail(){
          this.isDetail = false;
        },
        openDetail(item){
          this.detail = item;
          this.isDetail = true;
        }
    }
}
</script>

<style scoped>
.card-list{
    box-sizing: border-box;
    padding: 28px 61px;
    /* height:100%; */

    height: 500px;
    align-items: flex-start;
}
.list-header{
  display: flex;
  gap:100px;
  white-space: nowrap;
  height: 61px;
  align-items: center;
  border-bottom: 1px solid #E1E2E9;
  margin-bottom: 8px;


  font-family: 'Roboto';
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 0.25px;

  /* Dark2 */

  /* color: #585767; */
}
.list-body{
  display:flex;
  flex-direction: column;
  gap:16px;
}
.list-item{
  display: flex;
  gap:100px;
  align-items: center;
}
.list-item .thumb{
  width:80px;
  height:80px;
  border-radius: 100%;
}
.list-item .info{
  width:80px;
}
.list-item .info .division{
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 14px;
  /* identical to box height */

  letter-spacing: 0.4px;

  color: #528EE9;
  
  margin-bottom: 8px;
}
.list-item .time{
  width:65px;
  word-break: normal;
  /* Caption */

  font-family: 'Roboto';
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 14px;
  letter-spacing: 0.4px;

  /* Dark4 */

  color: #78798D;
}
.list-item .dress-type{
  display:flex;
  align-items: center;
  justify-content:center;
  box-sizing: border-box;
  /* padding: 4px 5px; */
  gap: 5px;

  width: 100px;
  height: 24px;

  /* Dark9 */

  background: var(--color-state-card);
  border-radius: 4px;

  font-family: 'Roboto';
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 0.25px;

  color: #528EE9;
}
.list-item .hair-state,.dress-state{
  width: 55px;
  height:28px;
  background: var(--color-state-card);
  display:flex;
  align-items: center;
  justify-content: center;
  gap:5px;
  border-radius: 4px;
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 0.25px;
}
/* .list-item .dress-state{
  width:55px;
  background: var(--color-state-card);
} */
.list-item .more{
  width:32px;
  height: 32px;
  border-radius: 100%;
  background: var(--color-state-card);
  display:flex;
  align-items: center;
  justify-content: center;
}
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
  z-index:2;
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
</style>