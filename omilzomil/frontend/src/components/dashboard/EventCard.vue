<template>
  <div class="card">
    <div class="img-wrap">
      <img :src="returnImage">
    </div>
    <div style="display:flex;flex-direction:column;justify-content:space-between;align-items: flex-end;">
      <div style="display:flex;flex-direction:column;align-items: flex-end;">
        <div class="title">
          {{ type == 0 ? "이번달 부대중 외적군기 1등은?": "이번 달 우리부대 으뜸병사?" }}
        </div>
        <div class="content">
          {{ type == 0 ? "우리 부대는 몇 등 했을까?": "외적군기를 지킨 멋쟁이 병사!" }}
        </div>
      </div>
      <a @click="openCard">
        <div>자세히 보기</div>
      </a>
    </div>
    <EventCard
      v-if="showEvent===1"
      :name="title"
      contents="전체 부대 중 외적 군기 1등을 축하합니다!"
      @close-card="closeCard"
    />
    <EventCard
      v-else-if="showEvent===2"
      :name="title"
      contents="이번 달 소속 부대의 으뜸 병사입니다!"
      :photo="photo"
      @close-card="closeCard"
    />
  </div>
</template>

<script>
import EventCard from '../EventCard.vue';

export default {
    components:{EventCard},
    props:{
        type:{
            type:Number,
            default:null
        }
    },
    data(){
      return {
        showEvent:0,
        title:'',
        photo:null
      }
    },
    computed:{
        returnImage(){
            // return null
            if(this.type == 0) return require("@/assets/icons/podium-gold.svg");
            else return require("@/assets/icons/trophy-outline.svg");
        }
    },
    async mounted(){
      const url = this.type == 0 ? '/stats/month/unit/best/unit':'/stats/month/unit/best/person'
      try{
        const {data} = await this.$axios.get(url);
        // console.log(data);
        if(this.type == 0) this.title = data.unit;
        else {
          this.photo = data.image_path;
          this.title = data.name;
        }
      }catch(err){
        console.log(err)
      }
    },
    methods:{
      closeCard(){
        this.showEvent =false;
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