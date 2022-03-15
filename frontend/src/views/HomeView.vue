<template>
  <div class="home">
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
