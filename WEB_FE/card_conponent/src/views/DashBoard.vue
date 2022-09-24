<template>
  <div>
    <Card11 class="oneone"></Card11>
    <Card12 class="onetwo"></Card12>
    <Card13 class="onethree"></Card13>
    <Card14 class="onefour"></Card14>
    <Card21 class="twoone"></Card21>
    <Card22 class="twotwo"></Card22>
    <Card31 class="threeone"></Card31>
    <Card32 class="threetwo"></Card32>
    <Card41 class="fourone"></Card41>
  </div>
</template>

<script>
import Card11 from '@/components/Card1_1.vue'
import Card12 from '@/components/Card1_2.vue'
import Card13 from '@/components/Card1_3.vue'
import Card14 from '@/components/Card1_4.vue'
import Card21 from '@/components/Card2_1.vue'
import Card22 from '@/components/Card2_2.vue'
import Card31 from '@/components/Card3_1.vue'
import Card32 from '@/components/Card3_2.vue'
import Card41 from '@/components/Card4_1.vue'

export default {
  name: 'DashBoard',
  components: {
    Card11,
    Card12,
    Card13,
    Card14,
    Card21,
    Card22,
    Card31,
    Card32,
    Card41
  }
}
</script>

<style scoped>
  .oneone {
    left: calc(50% - 588px/2 - 306px);
    top: 152px;
  }
  .onetwo {
    left: calc(50% - 180px/2 + 102px);
    top: 152px;
  }
  .onethree {
    left: calc(50% - 180px/2 + 306px);
    top: 152px;
  }
  .onefour {
    left: calc(50% - 180px/2 + 510px);
    top: 152px;
  }
  .twoone {
    left: calc(50% - 792px/2 - 204px);
    top: 394px;
  }
  .twotwo {
    left: calc(50% - 384px/2 + 408px);
    top: 394px;
  }
  .threeone {
    left: calc(50% - 384px/2 - 408px);
    top: 1002px;
  }
  .threetwo {
    left: calc(50% - 792px/2 + 204px);
    top: 1002px;
  }
  .fourone {
    left: calc(50% - 384px/2 - 408px);
    top: 1223px;
  }
</style>
