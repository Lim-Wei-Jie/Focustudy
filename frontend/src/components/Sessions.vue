<template>
  <!-- eslint-disable -->
  <div class="container">
    <h3>Here are your past sessions.</h3>
    <table class="table table-bordered table-hover mt-5">
      <thead class="bg-dark text-light">
        <tr>
          <th>Date</th>
          <th>Total Study Time (h)</th>
          <th>Average Rating / 5</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(record, index) in timeData">
          <td>{{record.date.slice(0,16)}}</td>
          <td>{{record.totalDuration}}</td>
          <td>{{ratingData[index].avgRating}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { displaySessions } from "../endpoint/endpoint.js";
import { mapState } from "vuex"

export default {
  name: "Sessions",
  data() {
    return {
      ratingData: {},
      timeData: {}
    }
  },

  computed: {
    ...mapState(["email"]),
  },

  created() {

    displaySessions({email: this.email})
      .then((res) => {
        this.processSessions(res)
      })
      .catch((err) => {
        console.log(err);
      })
  },

  methods: {
    
    processSessions(userData) {
      this.ratingData = userData.rating_data.data.ratings
      this.timeData = userData.time_data.data.times
    }
  }

}
</script>

<style scoped>
  table {
    margin: auto;
    width: 600px;
  }
</style>