<template>
  <!-- eslint-disable -->
  <div class="container">

    <div class="title">
      Task List <br>
      (trying new template that auto updates - weijie)
    </div>

    <!-- task list -->
    <ul class="my mx-0 p-0">
      <!-- each row -->
      <li v-for="task in tasks" :key="task.id" class="d-flex border rounded py-1 px-3">
        <!-- each task -->
        <div class="col-lg-11 col-10 m-0 p-0">
          <p :class="{ done: task.done }">{{task.task_description}}</p>
          
        </div>
        <!-- icons for done and delete task -->
        <div class="col-lg-1 col-2 d-flex m-0 p-0 justify-content-between align-items-center">
          <span @click="toggleDone(task)"><i class="far fa-check-circle text-success me-1"></i></span>
          <span @click="delCurrTask(task.id)"><i class="far fa-trash-alt text-danger"></i></span>
        </div>
      </li>
    </ul>

  </div>
</template>

<script>
import { ref } from 'vue';
import { getTasks, deleteTask } from "../endpoint/endpoint.js";
import { mapState } from "vuex"

export default {
  data() {
    return {
      tasks: ref([]),
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
    },

    delCurrTask(id) {
      if (confirm("Are you sure?")) {
        deleteTask({
          email: this.email,
          task_id: id
        });
      }
    },

    toggleDone(task) {
      task.done = !task.done
    },
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
  max-width: 400px;
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

.done {
  text-decoration: line-through;
}
</style>