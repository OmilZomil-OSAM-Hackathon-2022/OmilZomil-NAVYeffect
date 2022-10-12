<template>
  <div
    class="percent"
    :style="{color:getPercentColor}"
  >
    <img
      v-if="percent == 0"
      src="@/assets/icons/equal.svg"
    >
    
    <IconBase
      v-if="percent != 0"
      :width="14"
      :height="14"
      viewBox="-2 -2 14 14"
    >
      <UpIcon v-if="percent > 0 && reverse || percent < 0 && !reverse" />
      <DownIcon v-else />
    </IconBase>
    <number
      :from="0"
      :to="getPercent"
      :duration="1"
    />%
  </div>
</template>

<script>
import IconBase from '../IconBase.vue';
import UpIcon from '@/assets/icons/up-icon.vue';
import DownIcon from '@/assets/icons/down-icon.vue';
export default {
    components: { IconBase, UpIcon, DownIcon },
    props: {
        percent: {
            type: Number,
            default: 0
        },
        reverse: {
            type: Boolean,
            default: false
        }
    },
    computed: {
        getPercent() {
            return this.percent > 0 ? this.percent : -this.percent;
        },
        getPercentColor(){
          if(this.percent == 0) return "#ABACC0";
            return this.percent > 0 && !this.reverse || this.percent < 0 && this.reverse ? '#3FC6B8' : '#FF5467';
        }
    }
}
</script>

<style>
.percent{
    display:flex;
    align-items: center;
    gap:4px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 14px;
    justify-content: center;
}
</style>