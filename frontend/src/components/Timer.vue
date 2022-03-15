<template>
  <div class="timer">
    <svg viewBox="0 0 100 100">
      <circle class="base" cx="50" cy="50" r="46.5" fill="none" stroke="orange" stroke-width="2"/>
    </svg>
    <span class="time">
        TIME!!!
    </span>
  </div>
</template>

<script>
export default {
  name: "Timer",
};
</script>

<style scoped>
    .timer {
        position: relative;
        margin: auto;
        width: 300px;
        height: 300px;
    }

    .time {
        position: absolute;
        width: 300px;
        height: 300px;
        top: 0;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>