<template lang="pug">
  div(id="App")
    NavBar
    router-view
</template>

<script lang="ts">
import NavBar from "@/components/NavBar.vue";
import { Component, Vue } from "vue-property-decorator";

@Component({
  name: "App",
  components: {
    NavBar
  }
})
export default class App extends Vue {}
</script>

<style scoped lang="scss">
#App {
  font-family: "Roboto", sans-serif;
}
</style>
