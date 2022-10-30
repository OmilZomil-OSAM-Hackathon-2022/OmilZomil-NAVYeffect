<template>
  <div class="card">
    <CardHead title="월별 파츠별 불량 비율" />
    <div
      v-if="!isLoading"
      class="char-wrap"
    >
      <apexchart
        type="radar"
        :options="getOption"
        :series="series"
        height="250"
      />
    </div>
  </div>
</template>

<script>
import CardHead from '../CardHead.vue';
export default {
    components: { CardHead },
    props:{
      isInLanding:{
        type:Boolean,
        default:false,
      }
    },
    data(){
      return {
        isLoading:true,
        series: [],
      }
    },
    computed:{
        getOption(){
            return {
                chart: {
                    toolbar:{
                        show:false,
                    },
                    // height: 400,
                    type: 'radar',
                },
                colors:["#9155EB"],
                xaxis: {
                    categories: ['이름표', '계급장', '태극기', '모자', '두발']
                },
                stroke:{
                  show:false,
                },
                markers:{
                  size:0
                },
                yaxis:{
                  show:false,
                },
                dataLabels:{
                  enabled: true,
                  formatter: function (val) {
                      return val+'%'
                  },
                  style: {
                      colors:[this.$store.getters.getDarkMode ? "#D4B7FF":"#9155EB"]
                  },
                  background:{
                    enabled:false,
                    foreColor: '#9155EB',
                  }
                },
                fill:{
                  opacity: this.$store.getters.getDarkMode ? 0.75:0.25,
                }
            }
        }
    },
    async mounted(){
      if(this.isLoading){
        this.series = [{
            name: '파츠',
            data: [40,82,50,64,87],
          }]
      this.isLoading = false;
        return;
      }
      try{
        const {data} = await this.$axios.get('/stats/month/fail/detail/');
        // console.log(data);
        
        this.series = [{
            name: '파츠',
            data: [data.이름표,data.계급장,data.태극기,data.모자,data.두발],
          }]
        // console.log()
      }catch(err){
        console.log(err);
      }
      this.isLoading = false;
    }
}
</script>

<style scoped>

.card{
      flex-direction: column;
      justify-content: flex-start;
  }

.char-wrap{
  height:100%;
  display:flex;
  align-items: center;
}
</style>