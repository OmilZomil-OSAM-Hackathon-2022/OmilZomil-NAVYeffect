<template>
  <div class="card">
    <CardHead title="주간 불량 통계" />
    <div class="df">
      <div class="info">
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
      </div>
      <apexchart
        type="bar"
        :options="getOption"
        :series="series"
      />
    </div>
  </div>
</template>

<script>
import CardHead from '../CardHead.vue';
import PercentTag from '../common/PercentTag.vue';

export default {
    components: { CardHead, PercentTag },
    // props:{

    // }
    data(){
        return{
            series: [{
                name: '불량수',
                data: [30, 40, 45, 50, 49, 60, 70]
            }],
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
                    show: false
                },
                xaxis: {

                    show:false,
                    lines:{
                        show:false,
                    },
                    categories: ["월","화","수","목","금","토","일"],
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
}
</script>

<style scoped>
.card{
    flex-direction: column;
    justify-content: flex-start;
}
.df{
    display:flex;
    height:100%;
    width:100%;
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
/* identical to box height */

letter-spacing: 1.5px;

/* Dark5 */

color: #9C9DB2;
margin-bottom:2px;
margin-top:4px;
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