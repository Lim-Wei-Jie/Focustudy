<template>
  <form @submit="onSubmit" class="add-form" autocomplete="off">
    <div class="form-control">
      <label style="padding: 5px">Task Name</label>
      <input type="text" v-model="task" name="task" placeholder="Add Task" maxlength="30" />
    </div>
    <input type="submit" value="Save Task" class="btn btn-block" />
  </form>
</template>

<script>

import {addTask} from "../endpoint/endpoint.js"

export default {
    name: "AddTask",
    data() {
        return {
            task: "",
        }
    },
    methods: {
        onSubmit(e) {
            e.preventDefault()

            if (!this.task) {
                alert("Please add a task.")
                return
            }

            addTask({
                "email": this.$store.state.email,
                "task_description": this.task
            })

            const newTask = {
                "task_description": this.task
            }

            this.$emit('add-task', newTask)

            this.task = ""
        }
  }
};
</script>

<style scoped>
    .add-form {
        margin-bottom: 40px;
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
