<template>
  <div class="about">
    <h1>This is an about page</h1>
    <Timer></Timer>
  </div>
</template>

<script>
import Timer from "@/components/Timer.vue";

export default {
  name: "AboutView",
  components: {
    Timer
  }
}
</script>
