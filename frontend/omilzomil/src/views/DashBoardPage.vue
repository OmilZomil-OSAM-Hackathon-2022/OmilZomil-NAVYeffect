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
                title="두발 양호 인원"
                :count="126"
                :percent="12"
                :parts-type="0"
              />
            </div>
            <div
              style="flex:1"
            >
              <PartsCard
                title="복장 양호 인원"
                :count="96"
                :percent="-4"
                :parts-type="1"
              />
            </div>
            <div
              style="flex:1"
            >
              <PartsCard
                title="출입 인원"
                :count="53"
                :percent="0"
                :parts-type="2"
              />
            </div>
          </div>
        </div>
        <div class="row2">
          <div style="flex:7;">
            <!-- test -->
            <ListUp
              gap="46"
              padding="41px 32px"
              min-height="0px"
              :is-in-dash="true"
            />
          </div>
          <div
            style="flex:3"
          >
            <DoughnutCard />
          </div>
        </div>
        <div class="row3">
          <div style="display:flex;flex:2;">
            <div
              class="card"
              style="flex:1"
            />
            <div
              class="card"
              style="flex:1"
            />
          </div>
          <div
            style="flex:1"
            class="card"
          />
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
export default {
    components: { ListUp, TitleCard, PartsCard, DoughnutCard }
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
.row2 .row3{
  height:562px;
}
</style>