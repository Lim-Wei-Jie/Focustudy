import { createStore } from "vuex";

export default createStore({
  state() {
    return {
      time: 0,
      spotify: []
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
    },

    updateSpotify(state, {
      spotify
    }) {
      state.spotify = spotify
      console.log(state.spotify)
    }
  },
  actions: {},
  modules: {},
});
