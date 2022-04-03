<template>
  <div class="box">
    <div class="title">
      Task List&nbsp;
      <i @click="$emit('show-task')" class="lni lni-circle-plus"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  props: ["showAddTask"],
  components: {},
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
