<template>
  <div class="wrap df-col">
    <div class="row df">
      <TotalScoreCard
        :total-count="30678"
        :percent="7"
        class="f1"
      />
      <div class="f1 df-col">
        <div class="f1 df">
          <WeekCard class="f1" />
          <MonthCard class="f1" />
          <!-- <div class="f1 card" /> -->
        </div>
        <div class="f1 df">
          <UnitCard class="f1" />
          <!-- <div class="f1 card" /> -->
          <div class="f1 card" />
        </div>
      </div>
    </div>
    <div class="row df">
      <div class="f1 df">
        <div class="card" />
        <div class="card" />
      </div>
      <div class="f1 card" />
    </div>
  </div>
</template>

<script>
import TotalScoreCard from '@/components/totaldash/TotalScoreCard.vue';
import WeekCard from '@/components/totaldash/WeekCard.vue';
import MonthCard from '@/components/totaldash/MonthCard.vue';
import UnitCard from '@/components/totaldash/UnitCard.vue';
export default {
    components: { TotalScoreCard, WeekCard, MonthCard, UnitCard }
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