<template>
  <div class="card">
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
          <div class="hair-state">
            {{ item.hairStatus }}
          </div>
          <div class="dress-state">
            {{ item.dressStatus }}
          </div>
          <a class="more">
            <img src="@/assets/icons/dots.svg">
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TshirtIcon from "../assets/icons/tshirt-icon.vue";
import IconBase from "./IconBase.vue";
export default {
    components: { TshirtIcon, IconBase },
    data() {
        return {
            dummy: [
                {
                    imageUrl: "@/assets/images/test.png",
                    division: "해군",
                    uClass: "일병",
                    uName: "나해군",
                    time: "2020-06-24 22:57:36",
                    dressType: "해군 군복",
                    hairStatus: true,
                    dressStatus: false
                },
                {
                    imageUrl: "@/assets/images/test.png",
                    division: "해군",
                    uClass: "일병",
                    uName: "나해군",
                    time: "2020-06-24 22:57:36",
                    dressType: "해군 군복",
                    hairStatus: true,
                    dressStatus: false
                },
                {
                    imageUrl: "@/assets/images/test.png",
                    division: "해군",
                    uClass: "일병",
                    uName: "나해군",
                    time: "2020-06-24 22:57:36",
                    dressType: "해군 군복",
                    hairStatus: true,
                    dressStatus: false
                }
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
        }
    }
}
</script>

<style scoped>
.card{
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
  box-sizing: border-box;
  padding: 4px 5px;
  gap: 10px;

  width: 100px;
  height: 24px;

  /* Dark9 */

  background: #F9F9FB;
  border-radius: 4px;

  font-family: 'Roboto';
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 0.25px;

  color: #528EE9;
}
.list-item .hair-state{
  width: 55px;
}
.list-item .dress-state{
  width:55px;
}
.list-item .more{
  width:32px;
  height: 32px;
  border-radius: 100%;
  background: #F9F9FB;
  display:flex;
  align-items: center;
  justify-content: center;
}
</style>