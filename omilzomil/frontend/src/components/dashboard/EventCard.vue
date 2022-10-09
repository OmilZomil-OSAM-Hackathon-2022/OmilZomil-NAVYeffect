<template>
  <div class="card">
    <div class="img-wrap">
      <img :src="returnImage">
    </div>
    <div style="display:flex;flex-direction:column;justify-content:space-between;align-items: flex-end;">
      <div style="display:flex;flex-direction:column;align-items: flex-end;">
        <div class="title">
          {{ title }}
        </div>
        <div class="content">
          {{ content }}
        </div>
      </div>
      <a @click="openCard">
        <div>자세히 보기</div>
      </a>
    </div>
  </div>

  <EventCard
    v-if="showEvent===1"
    name="계룡대 본부대대"
    contents="충청지역 부대 중 외적 군기 1등을 축하합니다!"
    @close-card="closeCard"
  />
  <EventCard
    v-else-if="showEvent===2"
    name="김민순"
    contents="이번 달 소속 부대의 으뜸 병사입니다!"
    photo="1"
    @close-card="closeCard"
  />

</template>

<script>
import EventCard from '../EventCard.vue';

export default {
    components:{EventCard},
    props:{
        type:{
            type:Number,
            default:null
        },
        title:{
            type:String,
            default:null
        },
        content:{
            type:String,
            default:null
        },
    },
    data(){
      return {
        showEvent:0,
      }
    },
    computed:{
        returnImage(){
            // return null
            if(this.type == 0) return require("@/assets/icons/podium-gold.svg");
            else return require("@/assets/icons/trophy-outline.svg");
        }
    },
    methods:{
      closeCard(){
        console.log("Testsets");
        this.showEvent =0;
      },
      openCard(){
        if(this.type==0) return this.showEvent=1;
        else return this.showEvent=2;
      },
    }
}
</script>

<style scoped>
.card{
    padding:48px 32px;
    box-sizing: border-box;
    display:flex;
    justify-content: space-between;
    align-items: flex-start;
}
.title{
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 700;
    font-size: 16px;
    line-height: 19px;
    /* identical to box height */

    text-align: right;
    letter-spacing: 0.15px;


}
.content{
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 16px;
    text-align: right;
    letter-spacing: 0.25px;
    margin-bottom:26px;
}
a{
    text-decoration: none;
    color:#fff;
    /* BUTTON */
    padding:8px 12px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 500;
    font-size: 14px;
    line-height: 16px;
    letter-spacing: 1.25px;
    text-transform: uppercase;
    background:#9155EB;
    width:fit-content;
    border-radius: 8px;
    cursor: pointer;
}
.img-wrap{
    width:56px;
    height:56px;
    background: rgba(145, 85, 235, 0.2);
        
    border-radius: 8px;
    display:flex;
    justify-content: center;
    align-items: center;
}
</style>