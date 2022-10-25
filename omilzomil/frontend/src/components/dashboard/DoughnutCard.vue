<template>
  <div class="card">
    <CardHead title="파츠 별 불량비율" />
    <div class="total">
      총 :&nbsp;<number
        :from="0"
        :to="40"
        :duration="2"
      />건
    </div>
    <div class="content">
      <div class="back-circle" />
      <div class="front-circle" />
      <div class="chart">
        <apexchart
          style="margin-top:10px;"
          :width="310"
          type="donut"
          :options="options"
          :series="series"
        />
      </div>
      <div>
        <div class="point-flex">
          <div style="display:flex;align-items:center">
            <div
              style="background:#9155EB"
              class="point"
            />
            이름표(<number
              :from="0"
              :to="nameTag"
              :duration="2"
            />%)
          </div>
          <div style="display:flex;align-items:center">
            <div
              style="background:#BD91FF"
              class="point"
            />
            계급장(<number
              :from="0"
              :to="classTag"
              :duration="2"
            />%)
          </div>
        </div>
        <div class="point-flex">
          <div style="display:flex;align-items:center">
            <div
              style="background:#EDE2FF"
              class="point"
            />
            태극기(<number
              :from="0"
              :to="flag"
              :duration="2"
            />%)
          </div>
          <div style="display:flex;align-items:center">
            <div
              style="background:#F5EEFF"
              class="point"
            />
            두발(<number
              :from="0"
              :to="hat"
              :duration="2"
            />%)
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CardHead from '../CardHead.vue';

export default {
    components: { CardHead },
    data() {
        return {
            doughnutChart: null,
            nameTag:25,
            classTag:25,
            flag:25,
            hat:25,
            options:{
                  chart: {
                    type:'donut',
                    id: 'unit-donut-chart',
                    animations:{
                      speed:1000,
                    },
                    toolbar:{
                        show:false,
                    },
                  },
                  labels: ['이름표', '계급장', '태극기', '모자'],
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
                            size:'70%'
                        }
                    }
                 },
              },
        };
    },
    computed:{
      series(){
        return [this.nameTag,this.classTag,this.flag,this.hat];
      }
    },
    async mounted() {
      try{
        const {data} = await this.$axios.get("/stats/month/unit/fail/detail/");
        // const total = (data.이름표 + data.계급장 + data.태극기 + data.모자);
        // console.log(total);
        this.nameTag = data.이름표;
        this.classTag = data.계급장;
        this.flag = data.태극기;
        this.hat = data.두발;
      }catch(err){
        console.log(err);
      }
    },
}
</script>

<style scoped>

.card{
    flex-direction: column;
    justify-content: flex-start;
}
.content{
  box-sizing: border-box;
  width:100%;
  align-items: center;
  height: 70%;
  display:flex;
  flex-direction: column;
  justify-content: center;
  position:relative;
}
.total{
  box-sizing: border-box;
  width:100%;
  display: flex;
  justify-content: flex-end;
  padding:13px 18px;
  /* Caption */

  font-family: 'Roboto';
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 14px;
  /* identical to box height */
  letter-spacing: 0.4px;
}
.back-circle{
  position:absolute;
  width:250px;
  height:250px;
  background:var(--color-state-card);
  border-radius:100%;
  z-index:1;
  top:40px;
}
.front-circle{
  position:absolute;
  width:110px;
  height:110px;
  background:var(--color-card);
  border-radius:100%;
  z-index:1;
  top:110px;
}
.chart{
  z-index:100;
  width:220px;
  height:220px;
  margin:90px 0px;
  display:flex;
  justify-content:center;
  align-items: center;
}
.point{
  width:14px;
  height:14px;
  border-radius:100%;
  margin-right:12px;
}
.point-flex{
  display:flex;
  gap:58px;
  margin-bottom:16px;
}
</style>