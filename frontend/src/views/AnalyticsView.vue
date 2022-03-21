<template>
  <div>
    <div class="m-5">
      <router-link
        to="/"
        class="bg-light p-2 text-dark rounded-3 text-decoration-none border"
        ><fa icon="clock"
      /></router-link>
    </div>
    <Analytics></Analytics>
  </div>
</template>

<script>
// @ is an alias to /src
import Analytics from "@/components/Analytics.vue";

export default {
  name: "AnalyticsView",
  components: {
    Analytics,
  },
};
</script>

<style scoped>
</style>