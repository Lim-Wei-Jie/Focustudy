<template>
  <!-- eslint-disable -->
  <div class="card">
    <div class="row g-0">
      <!-- left card img -->
      <div class="col-md-6 col-lg-6 d-none d-md-block">
        <img src="../assets/auth.png" alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem;"/>
      </div>
      <!-- right card sign in -->
      <div class="col-md-6 col-lg-6 d-flex align-items-center">
        <div class="card-body p-4 p-lg-5 text-black">
          <h2>Welcome.</h2>
          <br>
          <h5>Time to get focused.</h5>
          <br>
          <!-- sign in -->
          <button type="button" class="btn btn-sm btn-outline-dark px-3" @click="handleClickSignIn" :disabled="!Vue3GoogleOauth.isInit || Vue3GoogleOauth.isAuthorized">
            <font-awesome-icon :icon="['fab', 'google']" /> Continue with Google
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { inject, toRefs } from "vue";
import { mapState, mapMutations } from "vuex"

export default {
  name: "SignInCard",
  props: {
    msg: String,
  },

  data() {
    return {
      access_token: "",
    };
  },

  computed: {
    ...mapState(["email"])
  },

  methods: {

    async handleClickSignIn() {
      try {
        const googleUser = await this.$gAuth.signIn();
        if (!googleUser) {
          return null;
        }
        console.log("googleUser", googleUser);
        this.updateEmail(googleUser.getBasicProfile().getEmail())
        console.log("getId", this.email);
        console.log("getBasicProfile", googleUser.getBasicProfile());
        this.access_token = googleUser.getAuthResponse().access_token
        console.log("access_token", this.access_token);
        console.log("getAuthResponse", googleUser.getAuthResponse());
        console.log(
          "getAuthResponse",
          this.$gAuth.instance.currentUser.get().getAuthResponse()
        );
        this.$router.push({ name: 'home', query: { redirect: '/' } });
      } catch (error) {
        //on fail do something
        console.error(error);
        return null;
      }
    },

    ...mapMutations(["updateEmail"])
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
.card {
  border-radius: 1rem;
  background: linear-gradient(to right, white 50%, #e8e4e4 0%);
  border-width: 0px;
}
</style>
