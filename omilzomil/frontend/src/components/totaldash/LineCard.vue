<template>
  <div class="card">
    <CardHead title="월별 불량률" />
    <div
      v-if="!isLoading"
      class="char-wrap"
    >
      <apexchart
        type="line"
        :options="getOption"
        :series="[{
          name: '월별 불량비율',
          data: data
        }]"

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
            data:[],
            labels:[],
            isLoading:true,
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
            xaxis: {
              categories: this.labels,
              axisBorder: {
                  // show: false,
                  // tickAmount:10,
              },
              axisTicks: {
                  show: false
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
                      // background: '#FF4560',
                      fontWeight:900,
                      fontSize:'15px',
                    },
                    text: this.data[this.data.length-1].toString()+'%',
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
    async mounted(){
      try{
        const {data} = await this.$axios.get('/stats/year/fail/');
        const keys = Object.keys(data);
        for(var i=0;i<keys.length;i++){
          if(keys[i] == 'success' ||keys[i] == 'message') continue;
          this.labels.push(keys[i].split('-')[1]+'월');
          this.data.push(data[keys[i]]);
        }
      }catch(err){
        console.log(err);
      }
      this.isLoading = false;
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
  justify-content:center;
}
</style>