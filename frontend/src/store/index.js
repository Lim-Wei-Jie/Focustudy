import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";

export default createStore({
  plugins: [createPersistedState({
    storage: window.sessionStorage,
  })],
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
