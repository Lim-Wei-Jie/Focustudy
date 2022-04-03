import { createStore } from "vuex";

export default createStore({
  state() {
    return {
      // Test email
      email: "a@gmail.com",
      timeData: {},
      ratingData: {}
    }
  },
  getters: {},
  mutations: {
    updateTimeData(state, timeData) {
      state.timeData = timeData
    },
    updateRatingData(state, ratingData) {
      state.ratingData = ratingData
    }
  },
  actions: {},
  modules: {},
});
