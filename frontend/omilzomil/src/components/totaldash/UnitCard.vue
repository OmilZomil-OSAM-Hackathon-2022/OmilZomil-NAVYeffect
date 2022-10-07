<template>
  <div class="card">
    <CardHead title="소속별 위반 비율" />
    <!-- <div class="chart-wrap"> -->
    <apexchart
      style="margin-top:10px;"
      :width="170"
      type="donut"
      :options="options"
      :series="series"
    />
    <!-- </div> -->
  </div>
</template>
  
  <script>
  import CardHead from '../CardHead.vue';
  
  export default {
      components: { CardHead },
      // props:{
  
      // }
      data(){
          return{
              series: [40,30,20,10],
              options:{
                  chart: {
                    type:'donut',
                      id: 'donut-chart',
                      toolbar:{
                          show:false,
                      },
                  },
                  labels: ['육군', '해군', '공군', '해병대'],
                  colors:["#9155EB","#B98EFA","#D4B7FF","#ECDFFF"],
                  dataLabels:{
                      enabled:false,
                  },
                  legend:{
                      show:false,
                  },

                  stroke: {
                      show: false,    
                  },
                  plotOptions: {
                    pie: {
                        donut:{
                            size:'60%'
                        }
                    }
                 },
              },
          }
      },
  }
  </script>
  
  <style scoped>
  .card{
      flex-direction: column;
      justify-content: flex-start;
      align-items: flex-start;
      height:188px;
  }
  </style>