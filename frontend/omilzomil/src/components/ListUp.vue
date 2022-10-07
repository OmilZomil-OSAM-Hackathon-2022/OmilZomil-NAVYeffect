<template>
  <div
    class="card-list card"
    :style="{'min-height': minHeight}"
  >
    <CardHead
      v-if="isInDash"
      title="위병소 실시간 감지현황"
      target="/ListUp"
    />
    <div
      class="list"
      :style="{padding:padding}"
    >
      <div
        class="list-header"
        :style="{gap:gap+'px'}"
      >
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
        <div
          v-if="!isInDash"
          style="width:26px;display: flex;justify-content: center;"
        >
          관리자 확인
        </div>
        <div style="width:43px;display: flex;justify-content: flex-end;">
          자세히보기
        </div>
      </div>
      <div class="list-body">
        <div
          v-for="(item,index) in isInDash ? dummy.slice(0,4):dummy"
          :key="index"
          class="list-item"
          :style="{gap:gap+'px'}"
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

          <GoodBadTag :is-good="item.hairStatus" />
          <GoodBadTag :is-good="item.dressStatus" />
          <CheckTag
            v-if="!isInDash"
            :is-check="item.check"
          />
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
import DetailCard from "./DetailCard.vue";
import CardHead from "./CardHead.vue";
import CheckTag from "./CheckTag.vue";

class Item{
  constructor(){
    this.imageUrl = "@/assets/images/test.png",
    this.division ="해군",
    this.uClass = "일병",
    this.uName= "나해군",
    this.time= "2020-06-24 22:57:36",
    this.dressType= "해군 전투복",
    this.hairStatus= true,
    this.dressStatus= false
    this.check = true
  }
}

export default {
    components: { TshirtIcon, IconBase, GoodBadTag, DetailCard, CardHead, CheckTag },
    props:{
      gap: {
        type:String,
        default:"80"
      },
      padding:{
        type:String,
        default:"28px 61px",
      },
      minHeight:{
        type:String,
        default:"1112px",
      },
      isInDash:{
        type:Boolean,
        default:false,
      }
    },
    data() {
        return {
            detail: new Item(),
            isDetail: false,
            dummy: [
                new Item(),
                new Item(),
                new Item(),
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
    height:100%;
    display:flex;
    flex-direction:column;
    justify-content: flex-start;
    align-items: center;
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
}
.list-item{
  display: flex;
  /* gap:100px; */
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
</style>