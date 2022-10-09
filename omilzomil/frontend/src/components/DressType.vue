<template>
  <div
    class="dress-type"
    :style="{color:getColor}"
  >
    <IconBase
      :width="16"
      :height="16"
      :viewBox="'0 0 16 16'"
    >
      <TshirtIcon />
    </IconBase>
    {{ dressType }}
  </div>
</template>

<script>
import TshirtIcon from "../assets/icons/tshirt-icon.vue";
import IconBase from "./IconBase.vue";
export default {
    components: { TshirtIcon, IconBase },
    props:{
        dressType:{
            type:String,
            default:null
        }
    },
    computed:{
        getColor(){
            // console.log(this.dressType)
            if(['해군 전투복','육군 전투복','공군 전투복'].includes(this.dressType)) return '#1DCB9D';
            else if(this.dressType == '해군 샘당') return '#4471FB';
            else if(this.dressType == '해군 동정복') return '#585767;';
            else if(this.dressType == '해군 하정복') return '#ABACC0';
            return '';
        }
    }
}
</script>

<style scoped>
.dress-type{
  display: flex;
  align-items: center;
  padding: 4px;
  background: var(--color-state-card);
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 0.25px;
}
</style>