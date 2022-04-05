<template>
  <!-- eslint-disable -->
  <div class="container">
    <h3>Activity Log</h3>

  </div>
</template>

<script>
import { displaySessions } from "../endpoint/endpoint.js";
import { mapState } from "vuex"

export default {
  name: "ActivityLog",
  data() {
    return {

    }
  },

  computed: {
    ...mapState(["email"]),
  },

  created() {

    displaySessions({
      email: this.email
    })
  }

}
</script>

<style scoped>

</style>