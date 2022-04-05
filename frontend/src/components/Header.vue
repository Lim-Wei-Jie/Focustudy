<template>
  <div class="box">
    <div class="title">
      Task List&nbsp;
      <i @click="$emit('show-task')" class="lni lni-circle-plus"></i>&nbsp;
      <fa icon="arrow-rotate-right" @click="allTasks" />
    </div>
  </div>
</template>

<script>
import { getTasks } from "../endpoint/endpoint.js";

export default {
  name: "Header",
  props: ["showAddTask"],
  components: {},
  methods: {
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
  }
  
};
</script>

<style scoped>
.title {
  text-align: center;
  font-size: 20px;
  color: #043631;
}
.box {
  position: relative;
}
</style>
