<template>
  <!-- eslint-disable -->
  <div class="container">
    <h3>Activity Log</h3>
    {{userData}}
  </div>
</template>

<script>
import { displaySessions } from "../endpoint/endpoint.js";
import { mapState } from "vuex"

export default {
  name: "ActivityLog",
  data() {
    return {
      userData: {}
    }
  },

  computed: {
    ...mapState(["email"]),
  },

  created() {

    displaySessions({email: this.email})
      .then((res) => {
        this.processSessions(res)
      })
      .catch((err) => {
        console.log(err);
      })
  },

  methods: {
    
    processSessions(userData) {
      this.userData = userData
    }
  }

}
</script>

<style scoped>

</style>