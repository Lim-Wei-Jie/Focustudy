<template>
  <div>
    <div v-for="task in tasks" :key="task.id">
      <Task
        @delete-task="$emit('delete-task', task.id)"
        :task="task"
      />
    </div>
  </div>
</template>

<script>
import Task from "./Task";

export default {
  name: "Tasks",
  props: [
    "tasks",
  ],
  components: {
    Task,
  },
  emits: ["delete-task"],
};
</script>