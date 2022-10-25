<template>
  <div class="row-center">
    <div class="wrap">
      <div class="column">
        <div class="row1">
          <div
            style="flex:1"
          >
            <TitleCard title="계룡대 본부대대" />
          </div>
          <div style="flex:1; display:flex;gap:24px">
            <div
              style="flex:1"
            >
              <PartsCard
                :parts-type="0"
              />
            </div>
            <div
              style="flex:1"
            >
              <PartsCard
                :parts-type="1"
              />
            </div>
            <div
              style="flex:1"
            >
              <PartsCard
                :parts-type="2"
              />
            </div>
          </div>
        </div>
        <div class="row2">
          <div style="width:792px;">
            <!-- test -->
            <ListUp
              gap="40"
              padding="41px 32px"
              min-height="0px"
              :is-in-dash="true"
            />
          </div>
          <div
            style="width:384px;"
          >
            <DoughnutCard />
          </div>
        </div>
        <div class="row3">
          <div style="width:384px;display:flex;flex-direction:column;gap:25px">
            <div style="flex:1">
              <EventCard
                :type="0"
                title="충청지역 부대 중 외적군기 1등!"
                content="이번 달 우리 부대는 몇 등 했을까?"
              />
            </div>
            <div style="flex:1">
              <EventCard
                :type="1"
                title="이번 달 계룡대 으뜸병사 나해군"
                content="우리 부대 으뜸병사는?"
              />
            </div>
          </div>
          <div
            style="width:792px;"
          >
            <LineCard />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ListUp from '@/components/ListUp.vue';
import TitleCard from '../components/dashboard/TitleCard.vue';
import PartsCard from '@/components/dashboard/PartsCard.vue';
import DoughnutCard from '@/components/dashboard/DoughnutCard.vue';
import LineCard from '@/components/dashboard/LineCard.vue';
import EventCard from '@/components/dashboard/EventCard.vue';
export default {
    components: { ListUp, TitleCard, PartsCard, DoughnutCard, LineCard,EventCard},
    mounted(){
      window.scrollTo(0, 0);
    }
}
</script>

<style scoped>
.column{
  display: flex;
  flex-direction: column;
  align-items: center;
  width:100%;
  margin-bottom: 100px;
  gap: 46px;
}
.row1, .row2, .row3{
  width:100%;
  display:flex;
  gap:24px;
}
.row1{
  height:196px;
}
.row2{
  height:562px;
}
.row3{
  height:417px;
}
</style>