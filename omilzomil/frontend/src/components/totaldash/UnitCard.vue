<template>
  <div class="card">
    <CardHead title="소속별 위반 비율" />
    <!-- <div class="chart-wrap"> -->
    <div style="display:flex;width:100%;">
      <apexchart
        style="margin-top:10px;"
        :width="170"
        type="donut"
        :options="options"
        :series="series"
      />
      <div class="legend">
        <div class="item">
          <div style="display:flex;align-items:center;">
            <div
              class="label"
              style="background: #9155EB;"
            />
            <div class="text">
              육군
            </div>
          </div>
          <div>
            <number
              :from="0"
              :to="40"
              :duration="1"
            />%
          </div>
        </div>
        <div class="item">
          <div style="display:flex;align-items:center;">
            <div
              class="label"
              style="background: #B98EFA;"
            />
            <div class="text">
              해군
            </div>
          </div>
          <div>
            <number
              :from="0"
              :to="30"
              :duration="1"
            />%
          </div>
        </div>
        <div class="item">
          <div style="display:flex;align-items:center;">
            <div
              class="label"
              style="background: #D4B7FF;"
            />
            <div class="text">
              공군
            </div>
          </div>
          <div>
            <number
              :from="0"
              :to="20"
              :duration="1"
            />%
          </div>
        </div>
        <div class="item">
          <div style="display:flex;align-items:center;">
            <div
              class="label"
              style="background: #ECDFFF;"
            />
            <div class="text">
              해병대
            </div>
          </div>
          <div>
            <number
              :from="0"
              :to="10"
              :duration="1"
            />%
          </div>
        </div>
      </div>
    </div>
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
  .legend{
    display:flex;
    flex-direction:column;
    width:100%;
    gap:15px;
    justify-content: center;
  }
  .legend .item{
    display:flex;
    align-items: center;
    justify-content: space-between;
    width:100%;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 10px;
    line-height: 12px;
    box-sizing:border-box;
    padding-right: 30px;
    /* identical to box height */

    letter-spacing: 0.15px;
  }
  .legend .item .label{
    width: 8px;
    height: 8px;
    border-radius: 2px;
    margin-right:8px;
  }
  </style>