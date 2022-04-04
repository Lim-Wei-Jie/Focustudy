<template>
  <div class="vh-100 bg-light">
    <div class="mx-4 pt-3 mb-5 d-flex justify-content-between">
      <div class="d-flex">
        <Icon icon="arcticons:bookshelf" width="40" color="black" />
        <h3>Focustudy</h3>
      </div>
      <button class="btn btn-dark rounded-circle" @click="handleClickSignOut" :disabled="!Vue3GoogleOauth.isAuthorized"><fa icon="right-from-bracket"/></button>
    </div>

    <!-- Default Page -->
    <div v-if="!sessionEnded" class="d-flex">
      <Spotify></Spotify>
      <Timer @endSession="showRating"></Timer>
      <TaskList></TaskList>
    </div>
    <!-- Rating Page -->
    <Rating v-if="sessionEnded" @ratingComplete='returnDefault'></Rating>

    <!-- Login Debug -->
    <div>
      <span>IsInit: {{ Vue3GoogleOauth.isInit }}</span>
      <br>
      <span>IsAuthorized: {{ Vue3GoogleOauth.isAuthorized }}</span>
      <br>
      <span v-if="email">signed user: {{ email }}</span>
      <br>
      <button type="button" class="btn btn-dark btn-sm" @click="handleClickGetAuthCode" :disabled="!Vue3GoogleOauth.isInit">Get authCode</button>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapState, mapMutations } from "vuex"
import { inject, toRefs } from "vue";
import { Icon } from "@iconify/vue";
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
    Icon, Timer, Rating, TaskList, Spotify
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

<style scoped>
</style>