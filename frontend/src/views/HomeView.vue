<template>
  <div>
    <div class="m-5">
        <router-link to="/analytics" class="bg-dark p-2 text-light rounded text-decoration-none">Analytics</router-link>
    </div>
    <Timer></Timer>
  </div>
</template>

<script>
// @ is an alias to /src
import Timer from "@/components/Timer.vue";

export default {
  name: "Homeview",
  components: {
    Timer
  }
}
</script>