<template>
  <div class="wrap">
    <div class="chart-position">
      <div class="chart-wrap">
        <div class="lock" />
        <apexchart
          type="line"
          :options="options"
          :series="series"
          height="700"
          width="1200"
        />
      </div>
    </div>
    <div class="circle-dec" />
    <h1>전군통계</h1>
    <div style="display: flex; width: 100%; z-index: 100; position: absolute">
      <div class="f1">
        <div style="display: flex; gap: 24px">
          <radar-card
            :is-in-landing="true"
            style="height: 402px; width: 282px; margin-top: 78px"
          />
          <div style="margin-top: 20px">
            <week-card
              :is-in-landing="true"
              style="margin-bottom: 25px"
            />
            <unit-card :is-in-landing="true" />
          </div>
        </div>
      </div>
      <div
        class="f1"
        style="
          display: flex;
          flex-direction: column;
          justify-content: flex-end;
          align-items: flex-end;
        "
      >
        <month-card
          :is-in-landing="true"
          style="width: 282px; height: 188px;margin-bottom: 60px;"
        />
        <div class="title">
          📈다양한 통계 차트들
        </div>
        <div class="sub-title">
          전체 부대 데이터를 통해 불량 비율 비교 가능
        </div>
        <router-link to="/totalDashboard">
          전군통계 바로가기
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import MonthCard from "../totaldash/MonthCard.vue";
import RadarCard from "../totaldash/RadarCard.vue";
import UnitCard from "../totaldash/UnitCard.vue";
import WeekCard from "../totaldash/WeekCard.vue";
export default {
  components: { RadarCard, WeekCard, UnitCard, MonthCard },
  data() {
    return {
      series: [
        {
          name: "back",
          data: [0, 20, 40, 20, 0, 25, 10, 60, 40, 80],
        },
      ],
      options: {
        chart: {
          type: "line",
          animations: {
            easing: "line",
            speed: 1000,
          },
          toolbar: {
            show: false,
          },
        },
        tooltip: {
          enabled: false,
        },
        stroke: {
          width: 15,
        },
        fill: {
          type: "gradient",
          gradient: {
            // shade: 'dark',
            type: "vertical",
            // shadeIntensity: 0,
            gradientToColors: ["#C3A5F3"], // optional, if not defined - uses the shades of same color in series
            // inverseColors: true,
            opacityFrom: 1,
            opacityTo: 0.7,
            // stops: [0, 50, 100],
            // colorStops: []
          },
        },
        colors: ["#C3A5F3"],
        dataLabels: {
          enabled: false,
        },
        legend: {
          show: false,
        },
        grid: {
          show: false,
        },
        xaxis: {
          show: false,
          axisTicks: {
            show: false,
          },
          labels: {
            show: false,
          },
          axisBorder: {
            show: false,
          },
        },
        yaxis: {
          show: false,
        },
      },
    };
  },
};
</script>

<style scoped>
.title {
  font-weight: 700;
  font-size: 24px;
  line-height: 28px;
  letter-spacing: 0.15px;
}
.sub-title {
  font-weight: 500;
  font-size: 20px;
  line-height: 23px;
  letter-spacing: 0.15px;
  margin:9px 0px 9px 0px;
}
a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 141px;
  height: 32px;

  /* Primary */

  background: #9155eb;
  border-radius: 8px;
  font-weight: 500;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 1.25px;

  color: #ffffff;
}
.f1 {
  flex: 1;
}
h1 {
  font-weight: 700;
  font-size: 32px;
  line-height: 150%;
  /* identical to box height, or 48px */
  /* Primary */
  width: 100%;
  color: #9155eb;
  display: flex;
  margin: 87px 0px 0px 0px;
}
.wrap {
  position: relative;
  height: 735px;
}
.chart-position {
  position: absolute;
  top: 0px;
}
.chart-wrap {
  position: relative;
}
.lock {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0px;
  z-index: 100000000;
}
.circle-dec {
  position: absolute;
  width: 433px;
  height: 433px;
  left: 220px;
  top: 130px;

  background: rgba(145, 85, 235, 0.2);
  filter: blur(20.5px);
  border-radius: 100%;
}
</style>
