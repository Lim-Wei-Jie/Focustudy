<template>
  <!-- eslint-disable -->

  <!-- Page -->
  <section class="vh-100 background">
    <div class="container py-3 h-100">
      <div class="row d-flex justify-content-center align-items-center" style="height: 85%">
        <div class="col col-xl-10">
          <!-- App Logo -->
          <div class="d-flex align-items-center mb-3 pb-1">
            <span class="h1 fw-bold">
              <Icon icon="arcticons:bookshelf" width="60" color="white" />
            </span>
            <h1 class="text-light">Focustudy</h1>
          </div>
          <!-- Card -->
          <SignInCard />
        </div>
      </div>
    </div>
  </section>
  
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
        sessionStorage.clear();
      } catch (error) {
        console.error(error);
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
