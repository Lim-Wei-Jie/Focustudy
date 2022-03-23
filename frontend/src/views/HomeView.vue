<template>
  <div class="home">
    <Timer></Timer>
    <GCal></GCal>
    <Spotify></Spotify>
  </div>
</template>

<script>
// @ is an alias to /src
import Timer from "@/components/Timer.vue";
import Spotify from "@/components/Spotify.vue";
import GCal from "@/components/GCal.vue";

export default {
  name: "Homeview",
  components: {
    Timer,
    Spotify,
    GCal
  }
}
</script>
