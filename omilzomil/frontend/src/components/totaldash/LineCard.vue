<template>
  <div class="card">
    <CardHead title="월별 불량률" />
    <div class="char-wrap">
      <apexchart
        type="line"
        :options="getOption"
        :series="series"

        height="300"
        width="520"
      />
    </div>
  </div>
</template>

<script>
import CardHead from '../CardHead.vue';

export default {
    components: { CardHead },
    data() {
        return {
            series: [{
              name: "월별 불량비율",
              data: [10, 41, 35, 51, 49, 62, 69, 91, 100,49, 62, 69]
            }]
        };
    },
    computed:{
      getOption(){
        return {
            chart: {
              // height: 350,
              type: 'line',
              zoom: {
                enabled: false
              },
              toolbar:{
                show:false
              }
            },
            colors:["#9155EB"],
            dataLabels: {
              enabled: false
            },
            stroke: {
              curve: 'straight',
              width:3,
            },
            // grid: {
            //   row: {
            //     colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
            //     opacity: 0.5
            //   },
            // },
            xaxis: {
              categories: ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
              axisBorder: {
                  // show: false,
                  // tickAmount:10,
              },
              axisTicks: {
                  show: false
              },
            },
            // grid:{
            //   show:true,
            //   // strokeDashArray: [5],
            //   xaxis: {
            //     lines: {
            //       show: true
            //     }
            //   },  
            // },

            // 마지막 데이터 꼭 넣어주기 => 그래프 마지막에 마크찍는 코드
            annotations:{
              points:[
                {
                  x:'12월',

                  y:69,
                  label: {
                    borderWidth:0,
                    style: {
                      color: '#9155EB',
                      // background: '#FF4560',
                      fontWeight:900,
                      fontSize:'15px',
                    },
                    text: '69%',
                  },
                  marker:{
                    fillColor: "#9155EB",
                    strokeColor: "#9155EB80",
                    size: 5,
                    strokeWidth:5,
                  }
                }
              ]
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
  .char-wrap{
  height:100%;
  display:flex;
  align-items: center;
  justify-content:center;
}
</style>