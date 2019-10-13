<template lang="pug">
  div
    .h3.w-100.flex.flex-row.router.items-center.justify-between
      .flex.justify-center.ml4
        h2 ASL Interpreter
      .justify-end
        router-link(to="/").mr4-ns.mh2 Home
        router-link(to="../GitHub").mr4-ns.mh2 GitHub
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
@Component({
  name: "NavBar"
})
export default class NavBar extends Vue {}
</script>

<style lang="scss" scoped>
#navbar {
}
</style>
