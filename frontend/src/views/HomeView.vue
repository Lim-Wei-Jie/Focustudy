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
    <!-- Timer component -->
    <Timer></Timer>
  </div>
</template>

<script>
// @ is an alias to /src
import Timer from "@/components/Timer.vue";

export default {
  name: "Homeview",
  components: {
    Timer,
  }
};
</script>