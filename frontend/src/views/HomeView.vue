<template>
  <div>
    <div class="mx-4 mt-3 mb-5 d-flex justify-content-between">
      <h3>Focustudy</h3>
      <button class="btn btn-dark rounded-circle"><fa icon="right-from-bracket"/></button>
    </div>
    <!-- Default Page -->
    <div v-if="!sessionEnded" class="d-flex">
      <Timer @endSession="showRating"></Timer>
      <TaskList></TaskList>
    </div>
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