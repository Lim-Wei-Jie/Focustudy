<template>
  <div class="container">
    <Header @show-task="showAdd" :showAddTask="showAddTask" />
    <AddTask v-if="showAddTask" @add-task="addTask" />
    <Tasks
      @toggle-reminder="toggleReminder"
      @delete-task="deleteTask"
      :tasks="tasks"
    />
    <button class="btn btn-dark btn-sm" @click="allTasks">Refresh</button>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Tasks from "@/components/Tasks.vue";
import AddTask from "@/components/AddTask.vue";
import { getTasks, deleteTask } from "../endpoint/endpoint.js";

export default {
  name: "TaskList",
  components: {
    Header,
    Tasks,
    AddTask,
  },
  data() {
    return {
      tasks: [],
      showAddTask: false,
      // render: true,
    };
  },
  methods: {
    deleteTask(id) {
      // console.log("task", id);
      if (confirm("Are you sure?")) {
        deleteTask({
          email: this.$store.state.email,
          task_id: id,
        });
        // this.force();
      }
    },
    toggleReminder(id) {
      // console.log("reminder", id);
      this.tasks = this.tasks.map((task) =>
        task.id === id ? { ...task, reminder: !task.reminder } : task
      );
    },
    addTask() {
      // this.tasks = [...this.tasks, task];
      console.log(this.tasks);
      this.showAddTask = false;
      // this.force();
    },
    showAdd() {
      this.showAddTask = !this.showAddTask;
    },
    allTasks() {
      getTasks({
        email: this.$store.state.email,
      })
        .then((retrievedTasks) => {
          this.tasks = [];
          for (var id of Object.keys(retrievedTasks.data)) {
            this.tasks.push({
              id: id,
              task_description: retrievedTasks.data[id]["task_description"],
            });
          }
          console.log(this.tasks);
        })
        .catch((error_message) => {
          console.log(error_message);
        });
    },
    // force() {
    //   this.render = false;

    //   this.$nextTick(() => {
    //     this.render = true;
    //   });
    // },
  },
  created() {
    this.allTasks();
  },
};
</script>

<style scoped>
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
</style>