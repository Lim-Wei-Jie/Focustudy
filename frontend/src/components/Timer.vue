<template>
  <div class="timer">
    <!-- VISUAL -->
    <!-- Colour differentiation: Study - Orange, Break - Green -->
    <svg viewBox="0 0 100 100">
      <g class="pathContainer">
        <circle class="base" cx="50" cy="50" r="45" />
        <path
          class="path"
          :class="{'study': !startBreak, 'break': startBreak}"
          d="
            M 50, 50
            m -45, 0
            a 45,45 0 1,0 90,0
            a 45,45 0 1,0 -90,0
          "
          :stroke-dasharray="studyDasharray"
        ></path>
      </g>
    </svg>

    <!-- TIME -->
    <!-- Default: Input Time. Limit inputs to 2 numbers per text box -->
    <span class="time study" :class="{'study': !startBreak, 'break': startBreak}" v-if="!start">
      <!-- Hours -->
      <input
        :class="{'study': !startBreak, 'break': startBreak}"
        type="text"
        v-model="inputHours"
        maxlength="2"
        placeholder="00"
        oninput="this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1');"
      />
      <span>&nbsp;:&nbsp;</span>

      <!-- Minutes -->
      <input
        :class="{'study': !startBreak, 'break': startBreak}"
        type="text"
        v-model="inputMinutes"
        maxlength="2"
        placeholder="00"
        oninput="this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1');"
      />
      <span>&nbsp;:&nbsp;</span>

      <!-- Seconds -->
      <input
        :class="{'study': !startBreak, 'break': startBreak}"
        type="text"
        v-model="inputSeconds"
        maxlength="2"
        placeholder="00"
        oninput="this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1');"
      />
    </span>

    <!-- Timer Started, prevent input -->
    <span class="time study" :class="{'study': !startBreak, 'break': startBreak}" v-else>
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
        Study
      </button>
      &nbsp;&nbsp;&nbsp;&nbsp;
      <button type="button" class="btn btn-dark btn-sm" @click="startTimer(); takeBreak()">
        Break
      </button>
    </div>

    <!-- Timer Started, show take a break or end -->
    <div class="mt-3" v-else>
      <button
        type="button"
        class="btn btn-sm text-light"
        :class="{'btn-warning': !startBreak, 'btn-dark': startBreak}"
        @click="endTimer"
      >
        End
      </button>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex"

export default {
  name: "Timer",

  data() {
    return {
      // Statuses
      start: false,
      startBreak: false,

      // Time inputs
      inputHours: "",
      inputMinutes: "",
      inputSeconds: "",

      // Time data
      startDate: "",
      timerInterval: null,
      initialTimeInSeconds: 0,
      timeInSeconds: 0,
    };
  },

  computed: {

    ...mapState(["email"]),

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

    // Divide time left by total time
    timeFraction() {
      return this.timeInSeconds / this.initialTimeInSeconds;
    },

    // Update dashaway overtime
    studyDasharray() {
      let ratio = (this.timeFraction * 283).toFixed(0);
      return ratio + " 283";
    },
  },

  methods: {

    ...mapMutations(["updateTimeData"]),

    // Called when starting study session and break
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

      // Save initial time
      this.initialTimeInSeconds = this.timeInSeconds;

      // Retain input in proper formatting when returning to default
      let timeList = this.formattedTime.split(" : ")
      this.inputHours = timeList[0]
      this.inputMinutes = timeList[1]
      this.inputSeconds = timeList[2]

      // Start interval, decrease time by 1 per second
      this.timerInterval = setInterval(() => this.timeInSeconds--, 1000);

      // If studying, save date when timer was started
      this.startDate = new Date().toISOString().slice(0, 10)
    },

    // Called when starting a break
    takeBreak() {
      // Start break
      this.startBreak = true
    },

    // Called when ending study session
    endTimer() {
      // Add new record to Timer database if in study mode
      if (!this.startBreak) {
        let time = this.initialTimeInSeconds - this.timeInSeconds
        this.updateTimeData({
          "email": this.email,
          "startDate": this.startDate,
          "duration": time
        })

        // Go on to Rating
        this.$emit('endSession', true)
      }

      // Reset timer
      this.start = false;
      this.timeInSeconds = this.initialTimeInSeconds
      this.startBreak = false

      // Stop interval
      clearInterval(this.timerInterval);
    },
  },

  watch: {
    // Return to default input timer once countdown reaches 0
    timeInSeconds(newValue) {
      if (newValue < 0) {
        // Add new record to Timer database if in study mode
        if (!this.startBreak) {
          this.updateTimeData({
            "email": this.email,
            "startDate": this.startDate,
            "duration": this.initialTimeInSeconds
          })

          // Go on to Rating
          this.$emit('endSession', true)
        }

        // Reset timer status
        this.start = false;
        this.startBreak = false

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

.pathContainer {
  fill: none;
}

svg {
  /* Flips the svg and makes the animation to move left-to-right*/
  transform: scaleX(-1);
}

.base {
  stroke: lightgrey;
  stroke-width: 2;
}

.path {
  stroke-width: 2;
  stroke-linecap: round;

  /* Makes sure the animation starts at the top of the circle */
  transform: rotate(90deg);
  transform-origin: center;

  /* One second aligns with the speed of the countdown timer */
  transition: 1s linear all;
}

.study {
  stroke: orange;
  color: orange;
}

.break {
  stroke: darkgreen;
  color: darkgreen;
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
}

input[type="text"] {
  width: 47px;
  height: 40px;
  font-size: 40px;
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

button {
  width: 75px;
}
</style>