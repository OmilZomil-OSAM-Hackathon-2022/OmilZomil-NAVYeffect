<template>
  <div
    class="dress-type"
    :style="{color:dressColors[dressType]}"
  >
    <IconBase
      :width="16"
      :height="16"
      :viewBox="'0 0 16 16'"
    >
      <TshirtIcon />
    </IconBase>
    {{ title }}
  </div>
</template>

<script>
import TshirtIcon from "../assets/icons/tshirt-icon.vue";
import IconBase from "./IconBase.vue";
export default {
    components: { TshirtIcon, IconBase },
    props:{
        dressType:{
          type:Number,
          default:0,
        },
        title:{
            type:String,
            default:null
        },
    },
    data(){
      return{
        dressColors:["","","#4471FB","#585767","#1DCB9D"],
      }
    },
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