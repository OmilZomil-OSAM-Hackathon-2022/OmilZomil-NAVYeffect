<template>
  <div class="card">
    <CardHead title="월별 불량률" />
    <div class="char-wrap">
      <apexchart
        type="heatmap"
        :options="getOption"
        :series="series"
        height="290"
      />
    </div>
  </div>
</template>

<script>
import CardHead from '../CardHead.vue';

const days = ["월","화","수","목","금","토","일"];
export default {
    components: { CardHead },
    data(){
      return {
        series: [{
            name: '1',
            data: this.generateData(7, {
              min: 5,
              max: 90
            })
          },
          {
            name: '2',
            data: this.generateData(7, {
              min: 5,
              max: 90
            })
          },
          {
            name: '3',
            data: this.generateData(7, {
              min: 5,
              max: 90
            })
          },
          {
            name: '4',
            data: this.generateData(7, {
              min: 5,
              max: 90
            })
          },
          {
            name: '5',
            data: this.generateData(7, {
              min: 5,
              max: 90
            })
          },
          {
            name: '6',
            data: this.generateData(7, {
              min: 5,
              max: 90
            })
          },
          {
            name: '7',
            data: this.generateData(7, {
              min: 5,
              max: 90
            })
          }],
      }
    },
  computed:{
    getOption(){
      
      return {
                plotOptions:{
                  reverseNegativeShade: true,
                },
                chart: {
                  type: 'heatmap',
                  toolbar:{
                            show:false,
                        },
                },
                dataLabels: {
                  enabled: false
                },
                // colors: ["#78798D"],
                colors: ["#9155EB"],
                xaxis:{
                  position:"top",
                  labels:{
                    show:true,
                    style:{
                      colors:this.$store.getters.getDarkMode ? "#F4F5FA":"#585767",
                    }
                  },
                  axisBorder:{
                    show:false,
                  },
                  axisTicks:{
                    show:false,
                  }
                },
                yaxis:{
                  labels:{
                    show:false,
                  },
                  axisBorder:{
                    show:false,
                  },
                  axisTicks:{
                    show:false,
                  }
                },
                stroke: {
                  width: 5,
                  colors: [this.$store.getters.getDarkMode ? "#312D4B":"#FFFFFF"],
                }
              }
    }
  },
    methods: {
    generateData(count, yrange) {
      var i = 0;
      var series = [];
      while (i < count) {
        var x = days[i];
        // (i + 1).toString();
        var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
        series.push({
          x: x,
          y: y
        });
        i++;
      }
      return series;
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
}
</style>