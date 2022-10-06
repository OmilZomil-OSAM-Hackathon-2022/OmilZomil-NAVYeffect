<template>
  <div class="card-list card">
    <div class="list">
      <div
        class="list-header"
        :style="{gap:gap+'px'}"
      >
        <div style="width:80px">
          사진
        </div>
        <div style="width:65px;display: flex;justify-content: center;">
          소속 / 계급 / 이름
        </div>
        <div style="width:45px">
          시간
        </div>
        <div style="width:95px">
          복장
        </div>
        <div style="width:35px">
          두발상태
        </div>
        <div style="width:10px">
          복장상태
        </div>
        <div style="width:30px">
          관리자 확인
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
          :style="{gap:gap+'px'}"
        >
          <div class="left">
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
          </div>
          <div class="right">
            <GoodBadTag :is-good="item.hairStatus" />
            <GoodBadTag :is-good="item.dressStatus" />
            <CheckTag :is-check="item.managerStatus" />
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
  </div>

  <DetailCard
    v-if="isDetail"
    :item="detail"
    @close="closeDetail"
  />
</template>

<script>
import TshirtIcon from "../assets/icons/tshirt-icon.vue";
import IconBase from "./IconBase.vue";
import GoodBadTag from "./GoodBadTag.vue";
import CheckTag from "./CheckTag.vue";
import DetailCard from "./DetailCard.vue";

class Item{
  constructor(){
    this.imageUrl = "@/assets/images/test.png",
    this.division ="해군",
    this.uClass = "일병",
    this.uName= "나해군",
    this.time= "2020-06-24 22:57:36",
    this.dressType= "해군 전투복",
    this.hairStatus= true,
    this.dressStatus= false,
    this.managerStatus=true
  }
}

export default {
    components: { TshirtIcon, IconBase, GoodBadTag, DetailCard, CheckTag },
    props:{
      gap: {
        type:String,
        default:"100"
      },
    },
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
    height:100%;
    min-height: 500px;
    align-items: flex-start;
}

.list-header{
  display: flex;
  /* gap:100px; */
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
  width: 1066px;
  height: 80px;
}
.list-item{
  display: flex;
  gap:75px;
  align-items: center;
  width: 1066px;
  height: 80px;
}
.list-item .left{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 0px;
  gap: 90px;
  width: 581px;
  height: 80px;
}
.left .thumb{
  width:80px;
  height:80px;
  border-radius: 82px;
}
.left .info{
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0px;
  gap: 8px;

  width: 79px;
  height: 41px;
}
.left .info .division{
  width: 72px;
  height: 14px;

  font-family: 'Roboto';
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 14px;

  letter-spacing: 0.4px;

  color: #528EE9;
}
.left .info .name{
  width: 79px;
  height: 19px;

  font-family: 'Roboto';
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;

  letter-spacing: 0.15px;

  color: #585767;
}
.left .time{
  width: 65px;
  height: 28px;
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
.left .dress-type{
  display:flex;
  align-items: center;
  justify-content:center;
  box-sizing: border-box;
  /* padding: 4px 5px; */
  gap: 3px;

  width: 87px;
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
.list-item .right{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 0px;
  gap: 80px;
  width: 410px;
  height: 32px;
}
/* .right .hair-state,.dress-state{
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
} */
/* .list-item .dress-state{
  width:55px;
  background: var(--color-state-card);
} */
.right .more{
  width:32px;
  height: 32px;
  border-radius: 100%;
  background: var(--color-state-card);
  display:flex;
  align-items: center;
  justify-content: center;
}
</style>