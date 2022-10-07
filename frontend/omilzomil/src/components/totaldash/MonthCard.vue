<template>
  <div class="card">
    <CardHead title="월별 전군 불량 비율" />
    <div class="df">
      <div class="info">
        <div class="df-col">
          <number
            :from="0"
            :to="3424"
            :duration="1"
          />명
        </div>
        <div class="before">
          지난 주 대비
        </div>
        <PercentTag

          :percent="-3"
          :reverse="true"
        />
      </div>
      <apexchart
        class="donut"
        type="donut"
        :options="getOption"
        :series="series"
      />
      <div class="percentValue">
        <number
          :from="0"
          :to="35"
          :duration="1"
        />%
      </div>
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
    //   data(){
    //       return{
    //           series: [{
    //               name: '불량수',
    //               data: [70]
    //           }],
    //       }
    //   },
    data(){
          return{
            series: [44,56],
            dummy:[100],
          }
    },
          
      computed: {
        getOption(){
          const options = {
                  chart: {
                    type:'donut',
                      id: 'donut-chart',
                      toolbar:{
                          show:false,
                      },
                  },
                  colors:["#9155EB",this.$store.getters.getDarkMode ? "#2C2845":"#F3F3F3"],
                  plotOptions: {
                    pie: {
                        startAngle: -90,
                        endAngle: 90,
                        offsetY: 10,
                        donut:{
                            size:'65%'
                        }
                    }
                 },
                dataLabels:{
                    enabled:false,
                },
                legend:{
                    show:false,
                },
                theme: {
                    mode: 'light', 
                },
                stroke: {
                    show: false,    
                }

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
      
    width:282px;
      height:142px;
      overflow:hidden;
      position:relative;
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
  .donut{
    margin-top:20px;
    position:absolute;
    right:-10px;
    top:0px;
    width:230px;
  }
  .percentValue{
    position:absolute;
    bottom:25px;
    right:80px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 700;
    font-size: 20px;
    line-height: 23px;
    text-align: center;
    letter-spacing: 0.15px;

    color: #9155EB;
  }
  </style>