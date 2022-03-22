<template>
  <!-- eslint-disable -->

  <div class="container">
    <Header @show-task="showTask" :showAddTask="showAddTask"/>
    <AddTask v-if="showAddTask" @add-task="addTask" />
    <Tasks
        @toggle-reminder="toggleReminder"
        @delete-task="deleteTask"
        :tasks="tasks"
    />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Tasks from "./components/Tasks.vue";
import AddTask from "./components/AddTask.vue";

export default {
  name: "App",
  components: {
    Header,
    Tasks,
    AddTask,
  },
  data() {
    return {
      tasks: [],
      showAddTask: false,
    };
  },
  methods: {
    deleteTask(id) {
      // console.log("task", id);
      // if (confirm("Are you sure?")) {
        this.tasks = this.tasks.filter((task) => task.id !== id);
      // }
    },
    toggleReminder(id) {
      // console.log("reminder", id);
      this.tasks = this.tasks.map((task) =>
        task.id === id ? { ...task, reminder: !task.reminder } : task
      );
    },
    addTask(task) {
      this.tasks = [...this.tasks, task];
      this.showAddTask = false
    },
    showTask() {
      this.showAddTask = !this.showAddTask;
    },
  },
  created() {
    this.tasks = [
      {
        id: 1,
        text: "esm change report",
      },
      {
        id: 2,
        text: "task list front-end",
      },
      {
        id: 3,
        text: "analytics wireframe",
      },
    ];
  },
};
</script>


<style>
#app {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: black;
}

/* nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
} */

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* body {
  font-family: 'Poppins', sans-serif;
} */

.container {
  max-width: 400px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  max-height: 500px;
  padding: 30px;
  border-radius: 20px;
  background: #F7F8F7;
  box-shadow: 0.5px 5px 10px 12px #E4E4E4;
}
.btn {
  display: inline-block;
  background: #043631;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  /* cursor: pointer; */
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}
.btn:focus {
  outline: none;
}
.btn:active {
  transform: scale(0.98);
}
.btn-block {
  display: block;
  width: 100%;
}
</style>
