<template lang="pug">
  div.flex.flex-row.justify-around.bg-white
    h1 Predicted Letter: {{ display }}
    h1 Accuracy: {{ accuracy }}
</template>

<script>
export default {
  name: 'Display',
  computed: {
    display () {
      if(this.$store.state.payload) return this.$store.state.payload[0].displayName
      return "None"
    },
    accuracy () {
      if(this.$store.state.payload) return this.$store.state.payload[0].classification.score
      return "None"
    }
  }
}
</script>