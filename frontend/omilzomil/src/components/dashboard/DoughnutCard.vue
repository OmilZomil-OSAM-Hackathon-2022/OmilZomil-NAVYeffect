<template>
  <div class="card">
    <CardHead title="파츠 별 불량비율" />
    <div>
      <div>총 : 40건</div>
      <Doughnut
        :chart-options="chartOptions"
        :width="220"
        :height="220"
        chart-id="doughnut-chart"
        :chart-data="chartData"
      />
    </div>
  </div>
</template>

<script>
import {Doughnut} from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
//   Plugin
} from 'chart.js'
import CardHead from '../CardHead.vue';
    

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale)

export default {
    components:{
        Doughnut,
        CardHead
    },
    data(){
        return {
            chartData: {
                labels: [ '이름표', '계급장', '태국기', '모자' ],
                datasets: [ 
                  { 
                    backgroundColor:['#9155EB','#BD91FF','#EDE2FF','#F5EEFF'],
                    data: [40, 20, 12,10] 
                  } 
                ]
            },
            chartOptions: {
              responsive: true,
              title:{
                display:true,
                text:'test'
              }
            }
        }
    }
}
</script>

<style scoped>
.card{
    flex-direction: column;
    justify-content: flex-start;
}
</style>