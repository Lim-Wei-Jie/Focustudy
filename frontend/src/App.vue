<template>
  <star-rating />
</template>

<script>
import StarRating from 'vue-star-rating'

export default {
  name: "App",
  components: {
    StarRating,
  },
  beforeCreate: function () {
    document.body.className = "home";
  }
};
</script>

