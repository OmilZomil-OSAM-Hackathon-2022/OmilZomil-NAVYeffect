<template>
  <div class="card">
    <CardHead title="소속별 위반 비율" />
    <!-- <div class="chart-wrap"> -->
    <div
      v-if="!isLoading"
      style="display: flex; width: 100%"
    >
      <apexchart
        style="margin-top: 10px"
        :width="170"
        type="donut"
        :options="options"
        :series="[army, navy, air, marin]"
      />
      <div class="legend">
        <div class="item">
          <div style="display: flex; align-items: center">
            <div
              class="label"
              style="background: #9155eb"
            />
            <div class="text">
              육군
            </div>
          </div>
          <div>
            <number
              :from="0"
              :to="army"
              :duration="1"
            />%
          </div>
        </div>
        <div class="item">
          <div style="display: flex; align-items: center">
            <div
              class="label"
              style="background: #b98efa"
            />
            <div class="text">
              해군
            </div>
          </div>
          <div>
            <number
              :from="0"
              :to="navy"
              :duration="1"
            />%
          </div>
        </div>
        <div class="item">
          <div style="display: flex; align-items: center">
            <div
              class="label"
              style="background: #d4b7ff"
            />
            <div class="text">
              공군
            </div>
          </div>
          <div>
            <number
              :from="0"
              :to="air"
              :duration="1"
            />%
          </div>
        </div>
        <div class="item">
          <div style="display: flex; align-items: center">
            <div
              class="label"
              style="background: #ecdfff"
            />
            <div class="text">
              해병대
            </div>
          </div>
          <div>
            <number
              :from="0"
              :to="marin"
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
import CardHead from "../CardHead.vue";

export default {
  components: { CardHead },
  props: {
    isInLanding: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      isLoading: true,
      army: 0,
      navy: 0,
      air: 0,
      marin: 0,
      options: {
        chart: {
          type: "donut",
          id: "donut-chart",
          toolbar: {
            show: false,
          },
        },
        labels: ["육군", "해군", "공군", "해병대"],
        colors: ["#9155EB", "#B98EFA", "#D4B7FF", "#ECDFFF"],
        tooltip: {
          theme: this.$store.getters.getDarkMode ? "dark" : "light",
        },
        dataLabels: {
          enabled: false,
        },
        legend: {
          show: false,
        },

        stroke: {
          show: false,
        },
        plotOptions: {
          pie: {
            donut: {
              size: "60%",
            },
          },
        },
      },
    };
  },
  async mounted() {
    if (this.isInLanding) {
      this.army = 40;
      this.navy = 30;
      this.air = 20;
      this.marin = 10;
      this.isLoading = false;
      return;
    }
    try {
      const { data } = await this.$axios.get("/stats/month/fail/affiliation/");
      // console.log(data);
      this.army = data.육군;
      this.navy = data.해군;
      this.air = data.공군;
      this.marin = data.해병대;
    } catch (err) {
      console.log(err);
    }
    this.isLoading = false;
  },
};
</script>

<style scoped>
.card {
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  height: 188px;
}
.legend {
  display: flex;
  flex-direction: column;
  width: 100%;
  gap: 15px;
  justify-content: center;
}
.legend .item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  font-style: normal;
  font-weight: 400;
  font-size: 10px;
  line-height: 12px;
  box-sizing: border-box;
  padding-right: 30px;
  /* identical to box height */

  letter-spacing: 0.15px;
}
.legend .item .label {
  width: 8px;
  height: 8px;
  border-radius: 2px;
  margin-right: 8px;
}
</style>
