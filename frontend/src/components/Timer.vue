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
      <input
        type="text"
        v-model="hours"
        maxlength="2"
        oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"
      />
      <span>&nbsp;:&nbsp;</span>

      <!-- Minutes -->
      <input
        type="text"
        v-model="minutes"
        maxlength="2"
        oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"
      />
      <span>&nbsp;:&nbsp;</span>

      <!-- Seconds -->
      <input
        type="text"
        v-model="seconds"
        maxlength="2"
        oninput="this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');"
      />
    </span>

    <!-- Timer Started, prevent input -->
    <span class="time" v-else>
      {{formattedTime}}
    </span>

    <!-- BUTTONS -->
    <!-- Default: Start Timer -->
    <div class="mt-3" v-if="!start">
      <button
        type="button"
        class="btn btn-warning btn-sm text-light"
        @click="toggleTimer"
      >
        Start
      </button>
    </div>

    <!-- Timer Started, show take a break or end -->
    <div class="mt-3" v-else>
      <button type="button" class="btn btn-dark btn-sm" @click="takeBreak">
        Break
      </button>
      &nbsp;&nbsp;&nbsp;&nbsp;
      <button
        type="button"
        class="btn btn-warning btn-sm text-light"
        @click="toggleTimer"
      >
        End
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Timer",
  data() {
    return {
      hours: "00",
      minutes: "00",
      seconds: "00",
      start: false,
    };
  },
  computed: {
    // Ensure that timing convention is followed 
    formattedTime() {
      let seconds = parseInt(this.seconds)
      let minutes = parseInt(this.minutes)
      let hours = parseInt(this.hours)

      // Format seconds
      if (seconds > 59) {
        minutes += 1
        seconds -= 60
      }
      if (seconds < 10) {
        seconds = `0` + seconds
      }

      // Format minutes
      if (minutes > 59) {
        hours += 1
        minutes -= 60
      }
      if (minutes < 10) {
        minutes = `0` + minutes
      }

      if (hours < 10) {
        hours = `0` + hours
      }

      return hours + " : " + minutes + " : " + seconds
    }
  },
  methods: {
    // Called when starting and ending timer
    toggleTimer() {
      this.start = !this.start;
    },
    // Called when taking a break
    takeBreak() {},
  },
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
  font-size: 40px;
  color: orange;
}

input[type="text"] {
  width: 47px;
  height: 40px;
  font-size: 40px;
  border: none;
  color: orange;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

*:focus {
  outline: none;
}

button {
  width: 75px;
}
</style>