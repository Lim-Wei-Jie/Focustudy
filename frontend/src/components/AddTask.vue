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
<<<<<<< Updated upstream
.form-control:focus {
  outline: none;
}
</style>
=======
    .add-form {
        margin-bottom: 40px;
        background: #F7F8F7;
    }
    .form-control {
        margin: 20px 0;
    }
    .form-control label {
        display: block;
    }
    .form-control input {
        width: 100%;
        height: 40px;
        margin: 5px;
        padding: 3px 7px;
        font-size: 17px;
    }
    .form-control-check {
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .form-control-check label {
        flex: 1;
    }
    .form-control-check input {
        flex: 2;
        height: 20px;
    }
</style>
>>>>>>> Stashed changes
