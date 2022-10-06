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
      <div class="canvas-wrap">
        <canvas
          id="doughnutChart"
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
              :to="55"
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
              :to="21"
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
              :to="14"
              :duration="2"
            />%)
          </div>
          <div style="display:flex;align-items:center">
            <div
              style="background:#F5EEFF"
              class="point"
            />
            모자(<number
              :from="0"
              :to="10"
              :duration="2"
            />%)
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Chart } from 'chart.js'
import CardHead from '../CardHead.vue';
export default {
    components: { CardHead },
    data() {
        return {
            doughnutChart: null
        };
    },
    mounted() {
        this.start();
    },
    methods: {
        start() {
            const ctx = document.getElementById("doughnutChart").getContext("2d");
            this.doughnutChart = new Chart(ctx, {
                type: "doughnut",
                data: {
                    labels: ["이름표", "계급장", "태국기", "모자"],
                    datasets: [
                        {
                            backgroundColor: ["#9155EB", "#BD91FF", "#EDE2FF", "#F5EEFF"],
                            borderWidth:0,
                            data: [40, 20, 12, 10],
                        }
                    ]
                },
                options: {
                    animation: {
                        duration: 1500,
                    },
                    cutout:75,
                    responsive: true,
                    plugins: {
                        legend: {
                            display:false
                        },
                    },
                }
            });
        }
    }
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
  padding-bottom:50px;
  height: 100%;
  display:flex;
  flex-direction: column;
  align-content: center;
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
  top:75px;
}
.front-circle{
  position:absolute;
  width:110px;
  height:110px;
  background:var(--color-card);
  border-radius:100%;
  z-index:1;
  top:145px;
}
.canvas-wrap{
  z-index:100;
  width:220px;
  height:220px;
  margin:90px 0px;
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