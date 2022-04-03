<template>
  <div class="home">
    <Timer></Timer>
    <Spotify></Spotify>
  </div>
</template>

<script>
// @ is an alias to /src
import Timer from "@/components/Timer.vue";
import Spotify from '../components/Spotify.vue';

export default {
  name: "Homeview",
  components: {
    Timer,
    Spotify
  }
}
</script>