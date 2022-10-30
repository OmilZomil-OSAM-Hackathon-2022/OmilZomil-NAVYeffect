<template>
  <div class="card">
    <CardHead title="월별 불량률" />
    <div
      v-if="!isLoading"
      class="char-wrap"
    >
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
import CardHead from "../CardHead.vue";

const days = ["일", "월", "화", "수", "목", "금", "토"];
export default {
  components: { CardHead },
  data() {
    return {
      isLoading: true,
      series: [],
    };
  },
  computed: {
    getOption() {
      return {
        plotOptions: {
          reverseNegativeShade: true,
        },
        chart: {
          type: "heatmap",
          toolbar: {
            show: false,
          },
        },
        dataLabels: {
          enabled: false,
        },
        tooltip:{
          theme:this.$store.getters.getDarkMode?'dark':'light',
        },
        // colors: ["#78798D"],
        colors: ["#9155EB"],
        xaxis: {
          position: "top",
          labels: {
            show: true,
            style: {
              colors: this.$store.getters.getDarkMode ? "#F4F5FA" : "#585767",
            },
          },
          axisBorder: {
            show: false,
          },
          axisTicks: {
            show: false,
          },
        },
        yaxis: {
          labels: {
            show: false,
          },
          axisBorder: {
            show: false,
          },
          axisTicks: {
            show: false,
          },
        },
        stroke: {
          width: 5,
          colors: [this.$store.getters.getDarkMode ? "#312D4B" : "#FFFFFF"],
        },
      };
    },
  },
  async mounted() {
    try {
      const { data } = await this.$axios.get("/stats/day/fail/hitmap/49");
      // console.log(data);
      var count = 0;
      var tmp = [];
      for (var key in data) {
        if (key == "success" || key == "message") continue;
        count++;
        tmp.push({
          x: days[new Date(key).getDay()],
          y: data[key],
        });
        if (count % 7 == 0) {
          this.series.push({
            name: Number(count / 7).toString(),
            data: [...tmp],
          });
          tmp = [];
        }
      }
      if (tmp.length != 0)
        this.series.push({
          name: Math.ceil(count / 7).toString(),
          data: [...tmp],
        });
    } catch (err) {
      console.log(err);
    }
    this.isLoading = false;
  },
  methods: {},
};
</script>

<style scoped>
.card {
  flex-direction: column;
  justify-content: flex-start;
}
.char-wrap {
  height: 100%;
  display: flex;
  align-items: center;
}
</style>
