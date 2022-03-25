<template>
  <!-- eslint-disable -->

  <!-- Page -->
  <section class="vh-100 background">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center" style="height: 85%">
        <div class="col col-xl-10">
          <!-- App Logo -->
          <div class="d-flex align-items-center mb-3 pb-1">
            <span class="h1 fw-bold mb-0">
              <Icon icon="arcticons:bookshelf" width="80" color="white" />
            </span>
          </div>
          <!-- Card -->
          <SignInCard />
        </div>
      </div>
    </div>
  </section>

  <div>
    <h1>IsInit: {{ Vue3GoogleOauth.isInit }}</h1>
    <h1>IsAuthorized: {{ Vue3GoogleOauth.isAuthorized }}</h1>
    <h2 v-if="email">signed user: {{ email }}</h2>
    <button type="button" class="btn btn-outline-dark" @click="handleClickGetAuthCode" :disabled="!Vue3GoogleOauth.isInit">get authCode</button>
    <button type="button" class="btn btn-outline-dark" @click="handleClickSignOut" :disabled="!Vue3GoogleOauth.isAuthorized">sign out</button>
    <!-- <button @click="handleClickDisconnect" :disabled="!Vue3GoogleOauth.isAuthorized">disconnect</button> -->
  </div>
</template>

<script>
import { inject, toRefs } from "vue";
import { Icon } from "@iconify/vue";
import { mapState, mapMutations } from "vuex"
import SignInCard from "@/components/SignInCard.vue"

export default {
  name: "SignIn",
  props: {
    msg: String,
  },
  components: {
    Icon,
    SignInCard,
  },

  computed: {
    ...mapState(["email"])
  },

  methods: {

    async handleClickGetAuthCode() {
      try {
        const authCode = await this.$gAuth.getAuthCode();
        console.log("authCode", authCode);
      } catch (error) {
        //on fail do something
        console.error(error);
        return null;
      }
    },

    async handleClickSignOut() {
      try {
        await this.$gAuth.signOut();
        console.log("isAuthorized", this.Vue3GoogleOauth.isAuthorized);
        this.updateEmail("");
      } catch (error) {
        console.error(error);
      }
    },

    ...mapMutations(["updateEmail"])

    // handleClickDisconnect() {
    //   window.location.href = `https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout?continue=${window.location.href}`;
    // },
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
};
</script>

<style scoped>
button:disabled {
  background: #fff;
  color: #ddd;
  cursor: not-allowed;
}

.background {
  background-color: rgba(4, 54, 49, 0.7);
}

.card {
  border-radius: 1rem;
  background: linear-gradient(to right, white 50%, #e8e4e4 0%);
  border-width: 0px;
}
</style>
