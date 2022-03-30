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
    updateMorningGPA (state, morningGpa) {
      state.avgMorningGpa = morningGpa
    },
    updateAfternoonGPA (state, afternoonGpa) {
      state.avgMorningGpa = afternoonGpa
    },
    updateNightGPA (state, nightGpa) {
      state.avgMorningGpa = nightGpa
    }
  },
  actions: {},
  modules: {},
});
