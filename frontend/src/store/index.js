import { createStore } from "vuex";

export default createStore({
  state() {
    return {
      // Test email
      email: "a@gmail.com",
      avgMorningGpa:0, //
      avgAfternoonGpa:0, //
      avgNightGpa:0 //
    }
  },
  getters: {},
  mutations: {
    updateMorningGPA (state, avgMorningGpa) {
      state.avgMorningGpa = avgMorningGpa
    },
    updateAfternoonGPA (state, avgAfternoonGpa) {
      state.avgAfternoonGpa = avgAfternoonGpa
    },
    updateNightGPA (state, avgNightGpa) {
      state.avgNightGpa = avgNightGpa
    }
  },
  actions: {},
  modules: {},
});
