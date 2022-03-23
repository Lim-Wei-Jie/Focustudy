import { createStore } from "vuex";

export default createStore({
  state() {
    return {
      email: "a@gmail.com"
    }
  },
  getters: {},
  mutations: {
    updateEmail(state, { email }) {
      state.email = email
    }
  },
  actions: {},
  modules: {},
});
