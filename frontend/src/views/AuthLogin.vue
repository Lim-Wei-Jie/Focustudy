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
          <div class="card">
            <div class="row g-0">
              <!-- left card img -->
              <div class="col-md-6 col-lg-6 d-none d-md-block">
                <img src="../assets/auth.png" alt="login form" class="img-fluid" style="border-radius: 1rem 0 0 1rem;"/>
              </div>
              <!-- right card sign in -->
              <div class="col-md-6 col-lg-6 d-flex align-items-center">
                <div class="card-body p-4 p-lg-5 text-black">
                  <!-- sign in -->
                  <button type="button" class="btn btn-outline-dark" @click="handleClickSignIn" :disabled="!Vue3GoogleOauth.isInit || Vue3GoogleOauth.isAuthorized">
                    <font-awesome-icon :icon="['fab', 'google']" /> Sign in with Google
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  
  <div>
    <h1>IsInit: {{ Vue3GoogleOauth.isInit }}</h1>
    <h1>IsAuthorized: {{ Vue3GoogleOauth.isAuthorized }}</h1>
    <h2 v-if="user">signed user: {{user}}</h2>
    <button type="button" class="btn btn-outline-dark" @click="handleClickGetAuthCode" :disabled="!Vue3GoogleOauth.isInit">get authCode</button>
    <button type="button" class="btn btn-outline-dark" @click="handleClickSignOut" :disabled="!Vue3GoogleOauth.isAuthorized">sign out</button>
    <!-- <button type="button" class="btn btn-outline-dark" @click="handleGoogleApi" :disabled="!Vue3GoogleOauth.isInit">get cal</button> -->
    <!-- <button @click="handleClickDisconnect" :disabled="!Vue3GoogleOauth.isAuthorized">disconnect</button> -->
  </div>
</template>

<script>
import { inject, toRefs } from "vue";
import { Icon } from "@iconify/vue";

export default {
  name: "AuthLogin",
  props: {
    msg: String,
  },
  components: {
    Icon,
  },

  data() {
    return {
      user: "",
      access_token: "",
    };
  },

  methods: {
    async handleClickSignIn() {
      try {
        const googleUser = await this.$gAuth.signIn();
        if (!googleUser) {
          return null;
        }
        console.log("googleUser", googleUser);
        this.user = googleUser.getBasicProfile().getEmail();
        console.log("getId", this.user);
        console.log("getBasicProfile", googleUser.getBasicProfile());
        this.access_token = googleUser.getAuthResponse().access_token
        console.log("getAuthResponse", this.access_token);
        console.log(
          "getAuthResponse",
          this.$gAuth.instance.currentUser.get().getAuthResponse()
        );
      } catch (error) {
        //on fail do something
        console.error(error);
        return null;
      }
    },

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
        this.user = "";
      } catch (error) {
        console.error(error);
      }
    },

    // try gaxios
    // async handleGoogleApi() {
    //   var serviceURL = "https://www.googleapis.com/calendar/v3/calendar?access_token=" + this.access_token
    //   try {
    //     const response = await fetch(serviceURL, { method: 'GET' });
    //     const result = await response.json();
    //     if (response.status === 200) {
    //       console.log(result);
    //     }
    //   } catch (error) {
    //     console.log(error);
    //   }
    // }

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

<style>
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
