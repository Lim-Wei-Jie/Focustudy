<template>
  <form @submit="onSubmit" class="add-form" autocomplete="off">
    <div class="form-control">
      <label style="padding: 5px">Task Name</label>
      <input type="text" v-model="text" name="text" placeholder="Add Task" maxlength="30" />
    </div>
    <input type="submit" value="Save Task" class="btn btn-block" />
  </form>
</template>

<script>
export default {
    name: "AddTask",
    data() {
        return {
            text: "",
        }
    },
    methods: {
        onSubmit(e) {
            e.preventDefault()

            if (!this.text) {
                alert("Please add a task.")
                return
            }
            const newTask = {
                id: Math.floor(Math.random() * 100000),
                text: this.text,
            }

            console.log(newTask)
            this.$emit('add-task', newTask)

            this.text = ""
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
