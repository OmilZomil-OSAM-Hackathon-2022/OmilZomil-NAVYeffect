<template>
  <div class="card">
    <div
      class="image-background"
      :style="{backgroundColor:getColor}"
    >
      <img :src="getSvg">
    </div>
    <div class="title-wrap">
      <div class="title-text">
        {{ title }}
      </div>
      <div class="before-month">
        지난 달 대비
      </div>
    </div>
    <div class="number-wrap">
      <div class="count">
        {{ count }}
      </div>
      <div
        class="percent"
        :style="{color:getPercentColor}"
      >
        <img :src="getPercentSvg">
        {{ getPercent }}%
      </div>
    </div>
  </div>
</template>

<script>
    
export default {
    props:{
        title:{
            type:String,
            default:null,
        },
        count:{
            type:Number,
            default:0,
        },
        percent:{
            type:Number,
            default:0,
        },
        partsType:{
            type:Number,
            default:0,
        }
    },
    data(){
        return{
            number:0,
        }
    },
    computed:{
        getColor(){
            if(this.partsType == 0) return 'rgba(255, 215, 68, 0.2)';
            else if(this.partsType == 1) return 'rgba(255, 84, 103, 0.2)';
            else return 'rgba(63, 198, 184, 0.2)';
        },
        getSvg(){
            if(this.partsType == 0) return require('@/assets/icons/face-man-shimmer.svg');
            else if(this.partsType == 1) return require('@/assets/icons/tshirt-crew-red.svg');
            else return require('@/assets/icons/door.svg');
        },
        getPercent(){
            if(this.percent < 0) return -this.percent;
            return this.percent;
        },
        getPercentColor(){
            if(this.percent > 0) return '#3FC6B8';
            else if(this.percent < 0) return '#FF5467';
            else return '#ABACC0';
        },
        getPercentSvg(){
            if(this.percent > 0) return require('@/assets/icons/up.svg');
            else if(this.percent < 0) return require('@/assets/icons/down.svg');
            else return require('@/assets/icons/equal.svg');
        }
    },
    methods:{
    }
}
</script>

<style scoped>
.card{
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap:12px;
}
.image-background{
    width:56px;
    height:56px;
    border-radius: 8px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.number-wrap{
    display:flex;
    align-items: center;
    justify-content: center;
    gap:12px;
}
.title-wrap{
    display:flex;
    flex-direction: column;
    gap:4px;
    align-items: center;
}
.title-text{
    /* Body 1 */
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 19px;
    /* identical to box height */

    text-align: center;
    letter-spacing: 0.5px;
}
.before-month{
    color:#9C9DB2;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 500;
    font-size: 10px;
    line-height: 12px;
    /* identical to box height */
    letter-spacing: 1.5px;
}
.count{
    /* Headline 4 */

    font-family: 'Roboto';
    font-style: normal;
    font-weight: 600;
    font-size: 34px;
    line-height: 40px;
    /* identical to box height */

    letter-spacing: 0.25px;
}
.percent{
    display:flex;
    align-items: center;
    gap:4px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 14px;
}

</style>