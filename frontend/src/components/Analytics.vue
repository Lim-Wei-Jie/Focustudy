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

          <div class="container">
            <h3 class="p-3 text-center">Rating table</h3>
            <table class="table table-striped table-bordered">
              <thead>
                <tr>
                  <th>Morning</th>
                  <th>Afternoon</th>
                  <th>Night</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>{{this.avgMorningRating.toFixed(2)}}/5</td>
                  <td>{{this.avgAfternoonRating.toFixed(2)}}/5</td>
                  <td>{{this.avgNightRating.toFixed(2)}}/5</td>
                </tr>
              </tbody>
            </table>
          </div>

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
  // getAllRatings
} from "../endpoint/endpoint.js";
import { mapState } from "vuex"

export default {
  name: "Analytics",
  data() {
    return {
      // Study Duration
      timeRange: "day",
      timeList: [],
      avgMorningRating: 0,
      avgAfternoonRating: 0,
      avgNightRating: 0
    };
  },

  computed: {
    // Change time chart x-axis value based on timeRange selection
    ...mapState(["email", "avgMorningGpa", "avgAfternoonGpa", "avgNightGpa"]),

    timeHeader() {
      if (this.timeRange == "day" || this.timeRange == "month") {
        return "Day";
      } else if (this.timeRange == "year") {
        return "Month";
      } else {
        return "Year";
      }
    },
    
  },

  created() {
    
    // Default chart: Last 7 days
    let emailObj = { email: this.$store.state.email }
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
    
    // getAllRatings()
    //   .then((res) => {
    //     // this.ratings = res
    //     this.processRating(res)
    //   })
    //   .catch((err) => {
    //     console.log(err);
    //   })
  },

  methods: {
    processRating(userData) {
      var avgMorningGpa = []
      var avgAfternoonGpa = []
      var avgNightGpa = []
      for (var key in userData) {
        if (userData[key]['morningGPA'] != 0) {
          avgMorningGpa.push(userData[key]['morningGPA'])
        }
        if (userData[key]['afternoonGPA'] != 0) {
          avgAfternoonGpa.push(userData[key]['afternoonGPA'])
        }
        if (userData[key]['nightGPA'] != 0) {
          avgNightGpa.push(userData[key]['nightGPA'])
        }
      }

      avgMorningGpa.length != 0 
      ? this.avgMorningRating = avgMorningGpa.reduce((acc, curr) => acc + curr, 0) / avgMorningGpa.length 
      : this.avgMorningRating = 0

      avgAfternoonGpa.length != 0
      ? this.avgAfternoonRating = avgAfternoonGpa.reduce((acc, curr) => acc + curr, 0) / avgAfternoonGpa.length
      : this.avgAfternoonRating = 0

      avgNightGpa.length != 0
      ? this.avgNightRating = avgNightGpa.reduce((acc, curr) => acc + curr, 0) / avgNightGpa.length
      : this.avgNightRating = 0
    }
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