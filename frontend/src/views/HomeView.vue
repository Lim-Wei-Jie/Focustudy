<template>
  <div>
    <div class="m-5">
      <!-- Navigate to analytics -->
      <router-link
        to="/analytics"
        class="bg-light p-2 text-dark rounded-3 text-decoration-none border"
        ><fa icon="chart-simple"
      /></router-link>
    </div>
    <div>
      <h1>IsInit: {{ Vue3GoogleOauth.isInit }}</h1>
      <h1>IsAuthorized: {{ Vue3GoogleOauth.isAuthorized }}</h1>
      <h2 v-if="email">signed user: {{ email }}</h2>
      <button type="button" class="btn btn-outline-dark" @click="handleClickGetAuthCode" :disabled="!Vue3GoogleOauth.isInit">get authCode</button>
      <button type="button" class="btn btn-outline-dark" @click="handleClickSignOut" :disabled="!Vue3GoogleOauth.isAuthorized">sign out</button>
    </div>
    <!-- Default Page -->
    <Timer v-if="!sessionEnded" @endSession="showRating"></Timer>

    <TaskList/>

    <!-- Rating Page -->
    <Rating v-if="sessionEnded" @ratingComplete='returnDefault'></Rating>

    <Spotify></Spotify>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapState, mapMutations } from "vuex"
import { inject, toRefs } from "vue";
import Timer from "@/components/Timer.vue";
import TaskList from "@/components/TaskList.vue";
import Rating from "@/components/Rating.vue"
import Spotify from '@/components/Spotify.vue';

export default {
  name: "HomeView",
  data() {
    return {
      sessionEnded: false
    }
  },
  computed: {
    ...mapState(["email"])
  },
  components: {
    Timer, Rating, TaskList, Spotify
  },
  methods: {
    ...mapMutations(["updateEmail"]),

    async handleClickSignOut() {
      try {
        await this.$gAuth.signOut();
        console.log("isAuthorized", this.Vue3GoogleOauth.isAuthorized);
        this.updateEmail("");
        sessionStorage.clear();
        this.$router.push({ name: 'auth', query: { redirect: '/auth' } });
      } catch (error) {
        console.error(error);
      }
    },

    showRating(event) {
      this.sessionEnded = event
    },
    returnDefault(event) {
      this.sessionEnded = event
    }
  },

  setup(props) {
    const { isSignIn } = toRefs(props);
    const Vue3GoogleOauth = inject("Vue3GoogleOauth");

    const handleClickLogin = () => {};
    return {
      Vue3GoogleOauth,
      handleClickLogin,
      isSignIn,
    };
  },
}
</script>