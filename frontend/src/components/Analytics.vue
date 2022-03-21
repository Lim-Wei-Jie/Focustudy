<template>
  <div>
    <div class="d-flex justify-content-between mx-5">
      <h1>Productivity</h1>
      <select class="p-2 bg-light rounded border-0" v-model="timeRange" @change="updateGraph">
          <option value="week">This Week</option>
          <option value="month">This Month</option>
          <option value="year">This Year</option>
          <option value="all">All Time</option>
      </select>
    </div>
    <div class="m-5">Insert Graph Here!</div>
  </div>
</template>

<script>
import {getTimesAll, getTimesYear, getTimesMonth, getTimesWeek} from "../endpoint/endpoint.js"
export default {
  name: "Analytics",
  data() {
      return {
          timeRange: "week"
      }
  },
  methods: {
      updateGraph() {
          if (this.timeRange == "all") {
              getTimesAll()
          } else if (this.timeRange == "year") {
              getTimesYear()
          } else if  (this.timeRange == "month") {
              getTimesMonth()
          } else {
              getTimesWeek()
          }
      }
  },
  created() {
      getTimesWeek()
  }
};
</script>

<style scoped>
    select {
        height: 40px;
        box-shadow: 2px 2px lightgray;
    }
</style>