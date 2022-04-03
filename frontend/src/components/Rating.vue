<template>
  <div>
    <!-- Stars Input -->
    <div v-show="toggle">
      <div class="d-flex justify-content-center text-center">
        <div class="card" style="width: 68rem">
          <div class="card-body">
            <h5 class="card-title">How was your study session today?</h5>
            <div class="container">
              <div
                class="
                  starrating
                  risingstar
                  d-flex
                  justify-content-center
                  flex-row-reverse
                "
              >
                <input
                  type="radio"
                  id="star5"
                  name="rating"
                  value="5"
                  v-model="picked"
                  @click="toggle = !toggle"
                /><label for="star5" title="5 star">5</label>
                <input
                  type="radio"
                  id="star4"
                  name="rating"
                  value="4"
                  v-model="picked"
                  @click="toggle = !toggle"
                /><label for="star4" title="4 star">4</label>
                <input
                  type="radio"
                  id="star3"
                  name="rating"
                  value="3"
                  v-model="picked"
                  @click="toggle = !toggle"
                /><label for="star3" title="3 star">3</label>
                <input
                  type="radio"
                  id="star2"
                  name="rating"
                  value="2"
                  v-model="picked"
                  @click="toggle = !toggle"
                /><label for="star2" title="2 star">2</label>
                <input
                  type="radio"
                  id="star1"
                  name="rating"
                  value="1"
                  v-model="picked"
                  @click="toggle = !toggle"
                /><label for="star1" title="1 star">1</label>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Confirmation Message -->
    <div v-show="!toggle">
      <div class="d-flex justify-content-center">
        <div class="content text-center">
          <div class="ratings">
            <h2>You rated:</h2>
            <span class="product-rating">{{ picked }}</span
            ><span>/5</span>
            <div class="rating-text">
              <span>Thank you for using Focustudy</span>
            </div>
            <br />
            <button
              type="submit"
              class="btn btn-warning text-light"
              @click="postRating()"
            >
              Exit
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { recordSession } from "../endpoint/endpoint.js";
import { mapState, mapMutations } from "vuex"

export default {
  name: "Rating",
  data() {
    return {
      picked: null,
      toggle: true,
    };
  },

  computed: {

    ...mapState(["email", "timeData", "ratingData"]),
  },

  methods: {

    ...mapMutations(["updateRatingData"]),

    // Add new record to rating database
    postRating() {
      
      this.updateRatingData({
        email: this.email,
        currentDate: new Date().toISOString().slice(0, 10),
        rating: this.picked,
      })

      let sessionData = {
        timeData: this.timeData,
        ratingData: this.ratingData
      };

      // From endpoint.js
      recordSession(sessionData);
      // .then for the return data from endpoint.js to be store in vuex store for analytics - created analytics MS, post the return data to analytics db, get all data from db for analytics

      // Return to default view
      this.$emit("ratingComplete", false);
    },
  },
};
</script>

<style scoped>
@import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);
@import url(//fonts.googleapis.com/css?family=Open+Sans&display=swap);

h1[alt="Simple"] {
  color: white;
}

a[href],
a[href]:hover {
  color: grey;
  font-size: 0.5em;
  text-decoration: none;
}

body {
  background: #4a4a4c !important;
}

.starrating > input {
  display: none;
} /* Remove radio buttons */

.starrating > label:before {
  content: "\f005"; /* Star */
  margin: 2px;
  font-size: 8em;
  font-family: FontAwesome;
  display: inline-block;
}

.starrating > label {
  color: #222222; /* Start color when not clicked */
}

.starrating > input:checked ~ label {
  color: #ffca08;
} /* Set yellow color when star checked */

.starrating > input:hover ~ label {
  color: #ffca08;
} /* Set yellow color when star hover */

body {
  margin: 0;
  padding: 0;
  font-family: "Open Sans", serif;
  background: #eee;
}

.content {
  width: 420px;
  margin-top: 100px;
}

.ratings {
  background-color: #fff;
  padding: 54px;
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0px 10px 10px #e0e0e0;
}

.product-rating {
  font-size: 50px;
}

.stars i {
  font-size: 18px;
  color: #28a745;
}

.rating-text {
  margin-top: 10px;
}
</style>