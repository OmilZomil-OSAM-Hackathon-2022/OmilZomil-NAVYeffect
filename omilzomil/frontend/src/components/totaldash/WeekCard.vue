<template>
  <div class="card">
    <CardHead title="주간 불량 통계" />
    <!-- <div class="df"> -->
    <!-- <div class="info">
        <div class="df-col">
          <number
            :from="0"
            :to="203"
            :duration="1"
          />명
        </div>
        <div class="before">
          지난 주 대비
        </div>
        <PercentTag
          :percent="3"
          :reverse="true"
        />
      </div> -->
    <apexchart
      v-if="!isLoading"
      type="bar"
      :options="getOption"
      :series="[{
        name: '불량률',
        data: data
      }]"
      height="135px"
    />
  </div>
  <!-- </div> -->
</template>

<script>
import CardHead from '../CardHead.vue';
// import PercentTag from '../common/PercentTag.vue';

const days = ["일","월","화","수","목","금","토"];
export default {
    components: { CardHead },
    // props:{

    // }
    data(){
        return{
            data:[],
            isLoading:true,
            labels:[],
        }
    },
    computed: {
    //   getDarkMode () {
    //     return this.$store.getters.getDarkMode;
    //   },
      getOption(){
        const options = {
                chart: {
                    id: 'week-chart',
                    toolbar:{
                        show:false,
                    },
                },
                colors:["#9155EB"],
                dataLabels:{
                    enabled:false,
                },
                plotOptions:{
                    bar:{ 
                        columnWidth: '30%',
                        borderRadius:6,
                        colors: {
                            backgroundBarColors: [this.$store.getters.getDarkMode ? "#2C2845":"#F3F3F3",],
                            backgroundBarRadius: 6,
                        },
                    }
                },
                grid: {
                    show: false,
                },
                xaxis: {

                    show:false,
                    lines:{
                        show:false,
                    },
                    categories: this.labels,
                    axisBorder: {
                        show: false,
                    },
                    axisTicks:{
                        show:false,
                    },
                    labels:{
                        style:{
                            colors: this.$store.getters.getDarkMode ? "#F4F5FA":"#9C9DB2",
                        },
                    }
                },
                yaxis: {
                    show:false,
                },
            }
        return options;
      }
    },
    async mounted(){
        try{
            const {data} = await this.$axios.get('/stats/week/fail/');
            for(var key in data){
                if(key == 'success' || key == 'message' || key == 'count' || key == 'fail_rate' || key == 'increase_rate')continue;
                this.data.push(data[key]);
                this.labels.push(days[new Date(key).getDay()]);
            }
        }catch(err){
            console.log(err);
        }
        this.isLoading=false;
    },
}
</script>

<style scoped>

.card{
    flex-direction:column;
    justify-content:flex-start;
    height:189px;
}
.df{
    display:flex;
    height:100%;
    width:282px;

    /* box-sizing:border-box; */
}
.info{
    width:60px;
    padding-left:18px;   
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
white-space:nowrap;
/* identical to box height */

letter-spacing: 1.5px;

/* Dark5 */

color: #9C9DB2;
margin-bottom:2px;
margin-top:4px;
/* width:50px; */
}
.count{
    font-family: 'Roboto';
font-style: normal;
font-weight: 600;
font-size: 20px;
line-height: 23px;
letter-spacing: 0.25px;

}
</style>