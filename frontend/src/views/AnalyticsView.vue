<template>
  <div>
    <div class="m-5">
      <!-- Navigate to homepage -->
      <router-link
        to="/"
        class="bg-light p-2 text-dark rounded-3 text-decoration-none border"
        ><fa icon="clock"
      /></router-link>
    </div>
    <!-- Analytics component -->
    <Analytics />
    <!-- Activity Log component -->
    <ActivityLog />
  </div>
</template>

<script>
// @ is an alias to /src
import Analytics from "@/components/Analytics.vue";
import ActivityLog from "@/components/ActivityLog.vue"

export default {
  name: "AnalyticsView",
  components: {
    Analytics,
    ActivityLog,
  },
};
</script>

<style scoped>
</style>