<template lang="pug">
  div(id="Home").flex.flex-column.items-center.justify-center.center
    WebCam.w-100
    Upload.w-100
    Display.w-100
</template>

<script lang="ts">
import { Vue, Component } from "vue-property-decorator";
import WebCam from "../components/WebCam.vue"
import Display from "../components/Display.vue"
import Upload from "../components/Upload.vue"

@Component({
  name: "Home",
  components: {
    WebCam,
    Upload,
    Display
  }
})

export default class Home extends Vue {}
</script>

<style scoped lang="scss">
#Home {
}
</style>
