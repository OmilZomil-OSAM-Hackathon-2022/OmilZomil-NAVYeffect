<template>
  <div class="wrap">
    <h1>대시보드</h1>
    <div
      class="c1"
    >
      <div
        class="f1"
        style="
    height:196px;"
      >
        <div class="title">
          👀실시간 소속 부대 불량 상태 변화
        </div>
        <div class="sub-title">
          실시간으로 상태를 체크하여 소속 부대의 상태를 파악 가능
        </div>
        <router-link
          class="go-dash"
          to="/dashboard"
        >
          대시보드 바로가기
        </router-link>
      </div>
      <div
        ref="titleCard"
        style="height:196px;"
        class="f1"
      >
        <title-card
          v-if="isTitleCard"
          :is-in-landing="true"
        />
      </div>
    </div>
    <div
      ref="parts" 
      class="c2"
    >
      <div
        v-if="isParts"
        class="f2"
      >
        <parts-card
          style="height:196px;"
          :parts-type="0"
          :is-in-landing="true"
        />
        <parts-card
          style="height:196px;"
          :parts-type="1"
          :is-in-landing="true"
        />
        <parts-card
          style="height:196px;"
          :parts-type="2"
          :is-in-landing="true"
        />
      </div>
      <div class="f2">
        <img
          src="@/assets/images/mini-dash.png"
          class="mini-dash"
        >
      </div>
    </div>
    <div class="wrap">
      <div class="event-section">
        <div class="card-content-wrap">
          <div class="title">
            🎉장병 동기부여를 위한 순위 이벤트
          </div>
          <div class="sub-title">
            소속 부대의 순위, 병사 순위를 이벤트적 요소로 변화
          </div>
          <event-card
            :type="0"
            :is-in-landing="true"
            style="height:196px;width:384px;margin:35px 0px 25px 0px;"
          />
          <event-card
            :type="1"
            :is-in-landing="true"
            style="height:196px;width:384px"
          />
        </div>
        <div class="event-wrap">
          <div class="circle-deco" />
          <event-card-with-landing
            :photo="1"
            class="unit-card"
          />
          <event-card-with-landing
            :photo="2"
            class="user-card"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useElementVisibility } from '@vueuse/core'
import TitleCard from '../dashboard/TitleCard.vue'
import PartsCard from '../dashboard/PartsCard.vue'
import EventCardWithLanding from '../dashboard/EventCardWithLanding.vue'
import EventCard from '../dashboard/EventCard.vue'
export default {
  components: { TitleCard, PartsCard, EventCardWithLanding, EventCard },
  setup(){
    const titleCard = ref();
    const isTitleCard = useElementVisibility(titleCard);
    const parts = ref();
    const isParts = useElementVisibility(parts);
    return{
        titleCard,
        isTitleCard,
        parts,
        isParts
    }
  }
}
</script>

<style scoped>
.card-content-wrap{
    display:flex;
    flex-direction:column;
    justify-content:flex-end;
    align-items: flex-end;
}
.card-content-wrap .title{
    font-weight: 700;
    font-size: 24px;
    line-height: 28px;
    letter-spacing: 0.15px;
    margin-bottom:9px;

}
.card-content-wrap .sub-title{
    font-weight: 500;
    font-size: 20px;
    line-height: 23px;
    letter-spacing: 0.15px;
}
.event-section{
    display:flex;
    justify-content:flex-end;
}
.circle-deco{
    background:#9155EB33;
    width:345px;
    height:345px;
    border-radius: 100%;
    position:absolute;
    top:30px;
    left:-50px;
}
.event-wrap{
    position:relative;
    width: 550px;
    height:612px;
    margin-left:100px;
}
.unit-card{
    position:absolute;
    /* transform:skew(30deg,20deg); */
    transform:skewY(30deg);
    width:314px;
    height:472px;
    left:180px;
}
.user-card{
    position:absolute;
    transform:skewY(-30deg);
    width:224px;
    height:336px;
    top:180px;
}
.mini-dash{
    width:100%;
}

.c2{
    width:100%;
    display:flex;
    justify-content: center;
    align-items: flex-start;
    gap:24px;
}
.f2{
    flex:1;
    display:flex;
    justify-content: center;
    align-items: center;
    gap:24px;
}
.wrap{
    padding-bottom:99px;
}
h1{
    font-weight: 700;
    font-size: 32px;
    line-height: 150%;
    /* identical to box height, or 48px */
    /* Primary */
    width:100%;
    color: #9155EB;
    display:flex;
    margin:87px 0px 0px 0px;
}
.c1{
    width:100%;
    display:flex;
    justify-content: center;
    gap:24px;
    margin-bottom:52px
}
.f1{
    flex:1;
    display:flex;
    flex-direction:column;
    justify-content: flex-end;
    align-items: flex-end;
}
.f1 .title{
    font-weight: 700;
    font-size: 24px;
    line-height: 28px;
    letter-spacing: 0.15px;
    margin-bottom: 9px;
}
.f1 .sub-title{
    font-weight: 500;
    font-size: 20px;
    line-height: 23px;
    letter-spacing: 0.15px;
    margin-bottom:14px;
}
.f1 .go-dash{
    cursor:pointer;
    width: 141px;
    height: 32px;
    display:flex;
    align-items: center;
    justify-content: center;
    background: #9155EB;
    border-radius: 8px;
    color:white;
    font-weight: 500;
    font-size: 14px;
    line-height: 16px;
    letter-spacing: 1.25px;
}
</style>