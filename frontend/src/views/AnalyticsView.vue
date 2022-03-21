<template>
  <div>
    <div class="m-5">
        <router-link to="/" class="bg-dark p-2 text-light rounded text-decoration-none">Home</router-link>
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
    Analytics
  }
}
</script>

<style scoped>
</style>