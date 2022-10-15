<template>
  <div>
    <div>DarkMod : {{ getDarkMode }}</div>
    <h1>{{ res }}</h1>
    <button @click="getAPI">
      test
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      res: "",
    };
  },
  computed: {
    getDarkMode () {
      return this.$store.getters.getDarkMode;
    }
  },
  methods: {
    getAPI() {
      this.$axios
        .get("https://localhost:8888")
        .then((response) => {
          console.log(response);
          this.res = response;
        })
        .catch((error) => {
          console.log(error);
          this.res = error;
        });
    },
    
  },
};
</script>

<style>
</style>