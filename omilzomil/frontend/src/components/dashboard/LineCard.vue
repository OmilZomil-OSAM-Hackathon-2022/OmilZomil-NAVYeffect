<template>
  <div class="card">
    <CardHead title="월간 두발 및 복장 양호빈도" />
    <div class="chart-wrap">
      <canvas
        id="lineChart"
        style="width: 100%;height:100%;"
      />
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
            const ctx = document.getElementById("lineChart").getContext("2d");
            var gradient = ctx.createLinearGradient(0, 0, 0, 220);
            gradient.addColorStop(0.3, 'rgba(145, 85, 235, 0.4)');
            gradient.addColorStop(1, 'rgba(145, 85, 235, 0)');
            this.doughnutChart = new Chart(ctx, {
                type: "line",
                data: {
                    labels: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'],
                    datasets: [
                        {
                            fill:true,
                            // borderWidth: 1,
                            backgroundColor: gradient,
                            borderColor:gradient,
                            borderWidth:0,
                            data: [0, 70, 50, 10,20, 40, 50, 20, 60, 70, 90, 75],
                            lineTension:0.4,
                            pointRadius:0,
                            // pointRadius: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
                            // pointBorderColor:"#9155EB",
                        }
                    ]
                },
                options: {
                    // elements: {
                    //     point:{
                    //         radius: 0
                    //     }
                    // },
                    animation: {
                        duration: 1500,
                    },
                    responsive: false,
                    plugins: {
                        bezierCurve: true,
                        legend: {
                            display:false
                        },
                    },
                    scales: {
                        x: {
                            display: true,
                            title: {
                            display: true
                            }
                        },
                        y: {
                            
                            min: 0,
                            nax: 100,
                            ticks:{
                                stepSize:25,
                            }
                        }
                    }
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
.chart-wrap{
    width:100%;
    height:100%;
    padding:50px;
    box-sizing:border-box;
}
</style>