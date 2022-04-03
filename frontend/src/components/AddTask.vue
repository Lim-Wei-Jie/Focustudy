<template>
  <form class="mt-2" autocomplete="off">
    <div class="input-group">
      <input
        class="form-control form-control-sm shadow-none"
        type="text"
        v-model="task"
        name="task"
        placeholder="Task Name"
        maxlength="30"
      />
      <div class="input-group-append">
        <button @click="onSubmit" class="btn btn-sm btn-dark">Add</button>
      </div>
    </div>
  </form>
</template>

<script>
import { addTask } from "../endpoint/endpoint.js";

export default {
  name: "AddTask",
  data() {
    return {
      task: "",
    };
  },
  methods: {
    onSubmit(e) {
      e.preventDefault();

      if (!this.task) {
        alert("Please add a task.");
        return;
      }

      addTask({
        email: this.$store.state.email,
        task_description: this.task,
      });

      const newTask = {
        task_description: this.task,
      };

      this.$emit("add-task", newTask);

      this.task = "";
    },
  },
};
</script>

<style scoped>
.form-control:focus {
  outline: none;
}
</style>