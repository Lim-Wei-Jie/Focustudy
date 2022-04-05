<template>
  <div>
    <div class="m-5">
      <!-- Navigate to homepage -->
      <router-link
        to="/home"
        class="bg-light p-2 text-dark rounded-3 text-decoration-none border"
        ><fa icon="clock"
      /></router-link>
    </div>
    <!-- Activity Log component -->
    <ActivityLog />
  </div>
</template>

<script>
// @ is an alias to /src
import ActivityLog from "@/components/ActivityLog.vue"

export default {
  name: "ActivitiesView",
  components: {
    ActivityLog,
  },
};

</script>

<style scoped>
</style>