<template>
  <div class="wrap df-col">
    <div class="row df">
      <TotalScoreCard
        class="f1"
      />
      <div class="f1 df-col">
        <div class="f1 df">
          <WeekCard class="f1" />
          <MonthCard class="f1" />
        </div>
        <div class="f1 df">
          <UnitCard class="f1" />
          <TodayCard class="f1" />
        </div>
      </div>
    </div>
    <div class="row df">
      <div class="f1 df">
        <HeatMapCard class="f1" />
        <RadarCard class="f1" />
      </div>
      <LineCard class="f1" />
    </div>
  </div>
</template>

<script>
import TotalScoreCard from '@/components/totaldash/TotalScoreCard.vue';
import WeekCard from '@/components/totaldash/WeekCard.vue';
import MonthCard from '@/components/totaldash/MonthCard.vue';
import UnitCard from '@/components/totaldash/UnitCard.vue';
import TodayCard from '@/components/totaldash/TodayCard.vue';
import HeatMapCard from '@/components/totaldash/HeatMapCard.vue';
import RadarCard from '@/components/totaldash/RadarCard.vue';
import LineCard from '@/components/totaldash/LineCard.vue';
export default {
    components: { TotalScoreCard, WeekCard, MonthCard, UnitCard, TodayCard, HeatMapCard, RadarCard, LineCard }
}
</script>

<style scoped>
.row{
    height:402px;
}
.f1{
    flex:1;
}
.df{
    display:flex;
    gap:24px;
}
.df-col{
    display:flex;
    flex-direction: column;
    gap:26px;
}
.wrap{
    margin-bottom: 42px;
}
</style>