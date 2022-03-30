<template>
  <div class="container-fluid">
    <div class="row">

      <!-- STUDY DURATION -->
      <div class="col mx-5">

        <!-- Header -->
        <div class="d-flex justify-content-between">
          <!-- Title -->
          <h3>Study Duration</h3>
          <!-- Dropdown -->
          <select class="p-2 bg-light rounded border" v-model="timeRange">
            <option value="day">Last 7 Days</option>
            <option value="month">This Month</option>
            <option value="year">This Year</option>
            <option value="all">All Time</option>
          </select>
        </div>

        <!-- Chart -->
        <div class="mt-4">
          <column-chart :xtitle="timeHeader" ytitle="Hours" :data="timeList" :colors="['orange']" :precision="3"></column-chart>
        </div>

      </div>

      <!-- PRODUCTIVITY -->
      <div class="col mx-5">

        <!-- Header -->
        <div class="d-flex justify-content-between">
          <!-- Title -->
          <h3>Productivity</h3>
        </div>

      </div>

    </div>
  </div>
</template>

<script>
import {
  getTimesAll,
  getTimesYear,
  getTimesMonth,
  getTimesDay,
} from "../endpoint/endpoint.js";
import { mapState } from "vuex"

export default {
  name: "Analytics",
  data() {
    return {
      // Study Duration
      timeRange: "day",
      timeList: [],
    };
  },
  computed: {
    // Change time chart x-axis value based on timeRange selection
    timeHeader() {
      if (this.timeRange == "day" || this.timeRange == "month") {
        return "Day";
      } else if (this.timeRange == "year") {
        return "Month";
      } else {
        return "Year";
      }
    },
    ...mapState(["email", "avgMorningGpa", "avgAfternoonGpa", "avgNightGpa"])
  },
  created() {
    // Default chart: Last 7 days
    let emailObj = { email: this.$store.state.email };

    // Study Duration
    getTimesDay(emailObj)
      .then((success) => {
        this.timeList = []
        for (let row of success) {
          // Chartkick readable [x,y]
          this.timeList.push([row["range"], row["total"]])
        }
      })
      .catch((failure) => {
        this.timeList = failure;
      });
  },
  watch: {
    // Change time chart based on selection
    timeRange(newValue) {
      let emailObj = { email: this.$store.state.email };

      // All-time selected
      if (newValue == "all") {
        getTimesAll(emailObj)
          .then((success) => {
            this.timeList = []
            for (let row of success) {
              this.timeList.push([row["range"], row["total"]])
            }
          })
          .catch((failure) => {
            this.timeList = failure;
          });

      // This year selected
      } else if (newValue == "year") {
        getTimesYear(emailObj)
          .then((success) => {
            this.timeList = []
            for (let row of success) {
              this.timeList.push([row["range"], row["total"]])
            }
          })
          .catch((failure) => {
            this.timeList = failure;
          });

      // This month selected
      } else if (newValue == "month") {
        getTimesMonth(emailObj)
          .then((success) => {
            this.timeList = []
            for (let row of success) {
              this.timeList.push([row["range"], row["total"]])
            }
          })
          .catch((failure) => {
            this.timeList = failure;
          });

      // Last 7 days selected
      } else {
        getTimesDay(emailObj)
          .then((success) => {
            this.timeList = []
            for (let row of success) {
              this.timeList.push([row["range"], row["total"]])
            }
          })
          .catch((failure) => {
            this.timeList = failure;
          });
      }
    },
  },
};
</script>

<style scoped>
select {
  height: 40px;
  box-shadow: 2px 2px lightgray;
}
</style>