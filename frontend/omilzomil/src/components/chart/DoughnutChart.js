// import { Doughnut,mixins } from "vue-chartjs";
// const {reactiveProp} = mixins;
// export default {
//   extends: Doughnut,
//   mixins:[reactiveProp],
//   props: ["data", "options"],
//   mounted() {
//     this.renderChart(this.data, this.options);
//   }
// };
import { Doughnut } from "vue-chartjs";

export default {
  extends: Doughnut,
  props: ["data", "options"],
  mounted() {
    // this.chartData is created in the mixin.
    // If you want to pass options please create a local options object
    this.renderChart(this.data, this.options);
  }
};
