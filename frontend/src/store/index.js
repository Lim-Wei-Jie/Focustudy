import { createStore } from "vuex";

export default createStore({
  state() {
    return {
      // Test email
      email: "",
      timeData: {},
      ratingData: {}
    }
  },
  getters: {},
  mutations: {
    updateEmail (state, email) {
      state.email = email
    },
    updateTimeData(state, timeData) {
      state.timeData = timeData
    },
    updateRatingData(state, ratingData) {
      state.ratingData = ratingData
    },
  },
  actions: {},
  modules: {},
});
