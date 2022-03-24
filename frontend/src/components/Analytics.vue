<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col mx-5">
        <div class="d-flex justify-content-between">
          <h1>Study Duration</h1>
          <select class="p-2 bg-light rounded border" v-model="timeRange">
            <option value="day">Last 7 Days</option>
            <option value="month">This Month</option>
            <option value="year">This Year</option>
            <option value="all">All Time</option>
          </select>
        </div>
        <div class="mt-4">
          <table class="table table-bordered">
            <thead class="bg-light">
              <tr>
                <th>{{timeHeader}}</th>
                <th>Total Study Duration (s)</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="record in timeList"
                :key="[record.range, record.total]"
              >
                <td>{{ record.range }}</td>
                <td>{{ record.total }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div class="col mx-5">
        <div class="d-flex justify-content-between">
          <h1>Productivity</h1>
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
export default {
  name: "Analytics",
  data() {
    return {
      timeRange: "day",
      timeList: [],
    };
  },
  computed: {
    timeHeader() {
      if (this.timeRange == 'day' || this.timeRange == 'month') {
        return 'Day'
      } else if (this.timeRange == "year") {
        return 'Month'
      } else {
        return 'Year'
      }
    }
  },
  created() {
    let emailObj = { email: this.$store.state.email };
    getTimesDay(emailObj)
      .then((success) => {
        this.timeList = success;
      })
      .catch((failure) => {
        this.timeList = failure;
      });
  },
  watch: {
    timeRange(newValue) {
      let emailObj = { email: this.$store.state.email };
      if (newValue == "all") {
        getTimesAll(emailObj)
          .then((success) => {
            this.timeList = success;
          })
          .catch((failure) => {
            this.timeList = failure;
          });
      } else if (newValue == "year") {
        getTimesYear(emailObj)
          .then((success) => {
            this.timeList = success;
          })
          .catch((failure) => {
            this.timeList = failure;
          });
      } else if (newValue == "month") {
        getTimesMonth(emailObj)
          .then((success) => {
            this.timeList = success;
          })
          .catch((failure) => {
            this.timeList = failure;
          });
      } else {
        getTimesDay(emailObj)
          .then((success) => {
            this.timeList = success;
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