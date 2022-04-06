<template>
  <!-- eslint-disable -->
  <div class="container">

    <div class="title text-center mb-2">
      Task List
      <i class="fa fa-refresh" aria-hidden="true" @click="allTasks"></i>
    </div>

    <!-- task list -->
    <ul class="my mx-0 p-0">
      <!-- each row -->
      <li v-for="task in tasks" :key="task.id" class="d-flex border rounded my-2 py-1 px-3">
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

    <!-- add task -->
    <div class="input-group">
      <input
        class="form-control form-control-sm shadow-none"
        type="text"
        name="newTask"
        v-model="newTask"
        @keyup.enter="onEnter"
        placeholder="Task Name"
        maxlength="30"
      />
      <div class="input-group-append">
        <button @click.prevent="addNewTask" type="button" class="btn btn-sm btn-outline-dark">Add</button>
      </div>
    </div>

  </div>
</template>

<script>
import { getTasks, deleteTask, addTask } from "../endpoint/endpoint.js";
import { mapState } from "vuex"

export default {
  data() {
    return {
      tasks: [],
      newTask: ''
    }
  },
  setup() {
    
  },

  computed: {
    ...mapState(["email"]),
  },

  created() {
    this.allTasks()
  },

  methods: {
    allTasks() {
      this.tasks = []
      getTasks({email: this.email})
      .then((taskData) => {
        for (var id of Object.keys(taskData.data)) {
          this.tasks.push({
            id: id,
            task_description: taskData.data[id]["task_description"],
          });
        }
      })
      .catch((err) => {
        console.log(err);
      })
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

    addNewTask() {
      if (!this.newTask) {
        alert("Please add a task.")
        return
      }

      addTask({
        email: this.email,
        task_description: this.newTask,
      })

      this.newTask = "";
    },

    onEnter() {
      this.addNewTask()
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
  font-size: 20px;
  color: #043631;
}

.done {
  text-decoration: line-through;
}
</style>