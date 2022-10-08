<template>
  <div class="card">
    <CardHead title="오늘의 위반율" />
    <div class="content-wrap">
      <div class="info">
        <div>
          <number
            :from="0"
            :to="count"
            :duration="1"
          />명
        </div>
        <div class="before">
          어제 대비
        </div>
        <PercentTag
          :percent="percent"
          :reverse="true"
        />
      </div>
      <div class="circle-wrap">
        <div
          :style=" {background:(percent <= 0?'rgba(63, 198, 184, 0.2)':'rgba(255, 84, 103, 0.2)')}"
          class="circle1"
        />
        <div
          :style=" {background:(percent <= 0?'rgba(63, 198, 184, 0.2)':'rgba(255, 84, 103, 0.2)')}" 
          class="circle2"
        />
        <img
          :src="percent <= 0 ? require('@/assets/images/smile-face.svg'):require('@/assets/images/crying-face.svg')"
          class="circle3"
        >
      </div>
    </div>
  </div>
</template>

<script>
import CardHead from '../CardHead.vue';
import PercentTag from '../common/PercentTag.vue';
  
export default {
    components: { CardHead,PercentTag },
    data(){
        return {
            percent:-10,
            count:24,
        }
    }
}
</script>

<style scoped>
  .card{
      flex-direction: column;
      justify-content: flex-start;
  }
  .content-wrap{
    width:100%;
    height:100%;
    display:flex;
    align-items: center;
    justify-content: center;
    gap:37px;   
  }
  .info{
      width:60px;
      display:flex;
      flex-direction: column;
      justify-content: center;
      align-content: center;
  }
  .before{
font-family: 'Roboto';
  font-style: normal;
  font-weight: 500;
  font-size: 10px;
  line-height: 12px;
  /* identical to box height */
  
  letter-spacing: 1.5px;
  
  /* Dark5 */
  
  color: #9C9DB2;
  margin-bottom:2px;
  margin-top:4px;
  }


/* .wrapper {
  width: 250px;
  height: 250px;
} */

.circle-wrap{
    position:relative;
  /* width:150px;
  height:100px; */
  width: 80px;
  height: 80px;
}
.circle-wrap div {
  position: absolute;
  /* background: #ffffff; */
  border-radius: 50%;
  
}

.circle1 {
  width: 80px;
  height: 80px;
  top: 0px;
  left: 0px;
  filter: blur(2px);
  animation: scale1 2s;
}

.circle2 {
  width: 60px;
  height: 60px;
  top: 10px;
  left: 10px;
  filter: blur(2px);
  animation: scale2 2s;
}
.circle3 {
  position: absolute;
  top: 18px;
  left: 18px;
}


@keyframes scale1 {
  0%   { transform: scale(0) }
  100%  { transform: scale(1) }
}

@keyframes scale2 {
  0%, 40% { transform: scale(0) }
  100% {transform: scale(1) }
}

/* @keyframes scale3 {
  0%, 65% { transform: scale(0) }
  100% { transform: scale(1) }
} */
</style>