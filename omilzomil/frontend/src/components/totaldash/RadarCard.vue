<template>
  <div class="card">
    <CardHead title="월별 파츠별 불량 비율" />
    <div class="char-wrap">
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
    data(){
      return {
        series: [{
            name: 'Series 1',
            data: [40,82,50,64,87],
          }],
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