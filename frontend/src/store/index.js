import { createStore } from "vuex";

export default createStore({
  state() {
    return {
      time: 0,
    }
  },
  getters: {
    getTime: (state) => {
      return state.time
    }
  },
  mutations: {
    updateTime(state, {
      time
    }) {
      state.time = time
      console.log(state.time)
    }
  },
  actions: {},
  modules: {},
});
