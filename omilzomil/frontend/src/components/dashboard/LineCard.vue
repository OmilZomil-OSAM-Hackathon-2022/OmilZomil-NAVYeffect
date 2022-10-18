<template>
  <div class="card">
    <CardHead title="월간 두발 및 복장 양호빈도" />
    <div class="chart-wrap">
      <apexchart
        v-if="isEnd"
        type="area"
        :options="getOption"

        :series="getSeries"
        height="320"
        width="680"
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
            data:[],
            labels:[],
            isEnd:false,
        };
    },
    computed:{
        getSeries(){
            return [{
              name: "월별 두발 및 복장 양호빈도",
              data: this.data
            }]
        },
      getOption(){
        return {
            chart: {
              // height: 350,
              type: 'area',
              zoom: {
                enabled: false
              },
              toolbar:{
                show:false
              }
            },
            colors:["#9155EB"],
            fill: {
                colors:["#9155EB"],
                type: "gradient",
                gradient: {
                    opacityFrom: 0.6,
                    opacityTo: 0,
                }
            },
            dataLabels: {
              enabled: false
            },
            stroke: {
              curve: 'smooth',
              width:0,
            },
            xaxis: {
              categories: [...this.labels],
              axisTicks: {
                  show: false
              },
            },
            grid:{
              show:true,
              // strokeDashArray: [5],
              xaxis: {
                lines: {
                  show: true
                }
              },
              yaxis: {
                lines: {
                  show: true
                }
              },  
            },
            // 마지막 데이터 꼭 넣어주기 => 그래프 마지막에 마크찍는 코드
            annotations:{
              points:[
                {
                  x:this.labels[this.labels.length-1],
                  y:this.data[this.data.length-1],
                  label: {
                    borderWidth:0,
                    style: {
                      color: '#9155EB',
                      background: '#9155EB00',
                      fontWeight:900,
                      fontSize:'15px',
                    },
                    text: this.data[this.data.length-1]+'명',
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
    },
    async mounted() {
        try{
            const {data} = await this.$axios.get('/stats/month/unit/pass/');
            var keys = Object.keys(data);
            for(var i=0;i<keys.length;i++){
                if(keys[i] == 'success' || keys[i] == 'message') continue;
                this.data.push(data[keys[i]]);
                this.labels.push(Number(keys[i].split('-')[1]).toString()+'월');
            }
        }catch(err){
            console.log(err);
        }
        this.isEnd = true;
    }
}
</script>

<style scoped>

.card{
    flex-direction: column;
    justify-content: flex-start;
}
.chart-wrap{
    width:100%;
    height:100%;
    /* padding:50px;
    box-sizing:border-box; */
    display:flex;
    justify-content: center;
    align-items:center;
}
</style>
