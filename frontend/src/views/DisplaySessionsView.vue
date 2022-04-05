<template>
  <!-- Header -->
  <div class="vh-100 bg-light">

    <!-- Logo -->
    <div class="mx-4 pt-3 mb-5 d-flex justify-content-between">
      <div class="d-flex">
        <Icon icon="arcticons:bookshelf" width="40" color="black" />
        <h3>Focustudy</h3>
      </div>

        <!-- To HomeView -->
        <router-link
          to="/home"
          class="
            text-light
            bg-warning
            px-3
            pt-2
            me-3
            rounded
            text-decoration-none
          "
          title="Return Home"
          ><fa icon="home"
        /></router-link>

        <!-- Sessions component -->
        <Sessions />

    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { Icon } from "@iconify/vue";
import Sessions from "@/components/Sessions.vue"

export default {
  name: "DisplaySessionsView",
  data() {
    return {};
  },
  components: {
    Icon,
    Sessions
  },
};
</script>

<style scoped>
</style>