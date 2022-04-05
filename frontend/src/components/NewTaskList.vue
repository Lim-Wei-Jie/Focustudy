<template>
  <!-- eslint-disable -->
  <div class="container">

    <div class="title">
      Task List <br>
      (trying new template that auto updates - weijie)
    </div>

    <ul v-for="task in tasks" :key="task.id">
      {{task.task_description}}
    </ul>

  </div>
</template>

<script>
import { ref } from 'vue';
import { getTasks } from "../endpoint/endpoint.js";
import { mapState } from "vuex"

export default {
  data() {
    return {
      tasks: ref([])
    }
  },
  setup() {
    
  },

  computed: {
    ...mapState(["email"]),
  },

  created() {

    getTasks({email: this.email})
      .then((res) => {
        this.processTask(res)
      })
      .catch((err) => {
        console.log(err);
      })
  },

  methods: {
    processTask(taskData) {
      for (var id of Object.keys(taskData.data)) {
        this.tasks.push({
          id: id,
          task_description: taskData.data[id]["task_description"],
        });
      }
    }
  }
}
</script>

<style scoped>
#app {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: black;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.container {
  max-width: 300px;
  margin: auto;
  overflow: auto;
  min-height: 300px;
  max-height: 500px;
  padding: 20px;
  border-radius: 20px;
  background: #f7f8f7;
  box-shadow: 0.5px 5px 10px 12px #e4e4e4;
}

.title {
  text-align: center;
  font-size: 20px;
  color: #043631;
}

</style>