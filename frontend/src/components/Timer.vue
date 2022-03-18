<template>
  <div class="timer">
    <!-- STUDY -->

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
        v-model="inputHours"
        maxlength="2"
        placeholder="00"
        oninput="this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1');"
      />
      <span>&nbsp;:&nbsp;</span>

      <!-- Minutes -->
      <input
        type="text"
        v-model="inputMinutes"
        maxlength="2"
        placeholder="00"
        oninput="this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1');"
      />
      <span>&nbsp;:&nbsp;</span>

      <!-- Seconds -->
      <input
        type="text"
        v-model="inputSeconds"
        maxlength="2"
        placeholder="00"
        oninput="this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1');"
      />
    </span>

    <!-- Timer Started, prevent input -->
    <span class="time" v-else>
      {{ formattedTime }}
    </span>

    <!-- BUTTONS -->
    <!-- Default: Start Timer -->
    <div class="mt-3" v-if="!start">
      <button
        type="button"
        class="btn btn-warning btn-sm text-light"
        @click="startTimer"
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
        @click="endTimer"
      >
        End
      </button>
    </div>

    <!-- ERROR -->
    <p class="text-danger mt-3">{{ error }}</p>

    <!-- BREAK -->
  </div>
</template>

<script>
export default {
  name: "Timer",

  data() {
    return {
      inputHours: "",
      inputMinutes: "",
      inputSeconds: "",
      error: "",
      start: false,
      timerInterval: null,
      timeInSeconds: 0,
    };
  },

  computed: {
    // Ensure that timing convention is followed (HH:MM:SS)
    formattedTime() {
      let timeLeft = this.timeInSeconds;

      // Format hours
      let hours = Math.floor(timeLeft / 3600);
      if (hours < 10) {
        hours = `0` + hours;
      }

      // Format minutes
      timeLeft %= 3600;
      let minutes = Math.floor(timeLeft / 60);
      if (minutes < 10) {
        minutes = `0` + minutes;
      }

      // Format seconds
      let seconds = timeLeft % 60;
      if (seconds < 10) {
        seconds = `0` + seconds;
      }

      return hours + " : " + minutes + " : " + seconds;
    },
  },

  methods: {
    // Called when starting timer
    startTimer() {
      // Start timer status
      this.start = true;

      // Convert string input to number
      let hours = 0;
      let minutes = 0;
      let seconds = 0;

      if (this.inputHours != "") {
        hours = parseInt(this.inputHours);
      }

      if (this.inputMinutes != "") {
        minutes = parseInt(this.inputMinutes);
      }

      if (this.inputSeconds != "") {
        seconds = parseInt(this.inputSeconds);
      }

      // Convert input time to seconds
      let hrSec = hours * 60 * 60;
      let minSec = minutes * 60;
      this.timeInSeconds = hrSec + minSec + seconds;

      // Retain input from user after returning to default, with proper formatting
      let timeList = this.formattedTime.split(" : ");
      this.inputHours = timeList[0];
      this.inputMinutes = timeList[1];
      this.inputSeconds = timeList[2];

      // Start interval, decrease time by 1 per second
      this.timerInterval = setInterval(() => this.timeInSeconds--, 1000);
    },

    // Called when taking a break
    takeBreak() {
      // Stop interval
      clearInterval(this.timerInterval);
    },

    // Called when ending study session
    endTimer() {
      // Reset timer status
      this.start = false;

      // Stop interval
      clearInterval(this.timerInterval);
    },
  },

  watch: {
    // Return to default input timer once countdown reaches 0
    timeInSeconds(newValue) {
      if (newValue < 0) {
        // Reset timer status
        this.start = false;

        // Stop interval
        clearInterval(this.timerInterval);
      }
    },
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