<template>
  <div class="box">

    <div class="title">
        Task List&nbsp;
        <i @click="$emit('show-task')" class="lni lni-circle-plus"></i>
        <!-- <i class="fa-solid fa-plus"></i> -->
    </div>

  </div>
</template>

<script>

export default {
  name: "Header",
  props: ["showAddTask"],
  components: {

  },
};
</script>

<style scoped>
    .title {
        text-align: center;
        font-size: 20px;
        color: #043631;
    }
    header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
    .bottom-right {
        position: absolute;
        bottom: 0;
        right: 0;
    }
    .box {
        position: relative;
    }
</style>
