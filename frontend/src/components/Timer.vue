<template>
  <div class="timer">
    <!-- VISUAL -->
    <svg viewBox="0 0 100 100">
      <circle
        class="base"
        cx="50"
        cy="50"
        r="46.5"
        fill="none"
        stroke="orange"
        stroke-width="2"
      />
    </svg>

    <!-- ACTUAL NUMBERS -->
    <!-- Default: Input Time. Limit inputs to 2 numbers per text box -->
    <span class="time" v-if="!start">
      <!-- Hours -->
      <input type="text" :value="hours" maxlength="2" oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');" />
      <span>&nbsp;:&nbsp;</span>

      <!-- Minutes -->
      <input type="text" :value="minutes" maxlength="2" oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');" />
      <span>&nbsp;:&nbsp;</span>

      <!-- Seconds -->
      <input type="text" :value="seconds" maxlength="2" oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');" />
    </span>

    <!-- Timer Started, prevent input -->
    <span class="time" v-else>
      {{hours}} : {{minutes}} : {{seconds}}
    </span>

    <!-- BUTTONS -->
    <!-- Default: Start Timer -->
    <div v-if="!start">
      <button type="button" @click="startTimer">Start</button>
    </div>

    <!-- Timer Started, show take a break or end -->
    <div v-else>
      <button type="button" @click="takeBreak">Break</button>
      &nbsp;&nbsp;&nbsp;&nbsp;
      <button type="button" @click="startTimer">End</button>
    </div>

  </div>
</template>

<script>
var bootstrap = require("bootstrap");
export default {
  name: "Timer",
  data() {
    return {
      hours: "00",
      minutes: "00",
      seconds: "00",
      start: false
    };
  },
  computed: {

  },
  methods: {
    startTimer() {
      this.start = !this.start
    },
    takeBreak() {

    }
  }
};
</script>

<style scoped>
.timer {
  position: relative;
  margin: auto;
  width: 300px;
  height: 300px;
  text-align: center;
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

input[type="text"] {
  width: 22px;
  height: 20px;
  font-size: 20px;
  border: none;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

*:focus {
  outline: none;
}
</style>