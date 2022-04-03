<template>
  <div>
    <div class="m-5">
      <!-- Navigate to analytics -->
      <router-link
        to="/analytics"
        class="bg-light p-2 text-dark rounded-3 text-decoration-none border"
        ><fa icon="chart-simple"
      /></router-link>
    </div>
    <!-- Default Page -->
    <Timer v-if="!sessionEnded" @endSession="showRating"></Timer>

    <TaskList/>

    <!-- Rating Page -->
    <Rating v-if="sessionEnded" @ratingComplete='returnDefault'></Rating>
  </div>
</template>

<script>
// @ is an alias to /src
import Timer from "@/components/Timer.vue";
import TaskList from "@/components/TaskList.vue";
import Rating from "@/components/Rating.vue"

export default {
  name: "HomeView",
  data() {
    return {
      sessionEnded: false
    }
  },
  components: {
    Timer, Rating, TaskList
  },
  methods: {
    showRating(event) {
      this.sessionEnded = event
    },
    returnDefault(event) {
      this.sessionEnded = event
    }
  }
}
</script>