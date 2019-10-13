<template lang="pug">
  div(id="Upload").flex.center.justify-center
    input(type="file" accept="image/*" @change="uploadImage($event)" id="file-input").pa3
</template>

<script>
import axios from 'axios';

export default {
  name: 'Upload',
  data() {
    return {
      image: "",
    }
  },
  methods: {
    uploadImage(event) {
      const URL = 'https://automl.googleapis.com/v1beta1/projects/905505838894/locations/us-central1/models/ICN618229000019378176:predict'
      //let token = "ya29.c.Kl6bB-gsJFXVNUer5OKkciPV0W2MrE450TfjweHHuawaew9UqsDCi_AlWzk4H3YQR-pQaWRNWzHBg7K9LyVFEgiiORED4nzz8uxVVb0PhQXrA2JOdhDiEJSHcKAMdwnf"
      let config = {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.$store.state.token}`
        }
      }
      if (event.target.files) {
        var reader = new FileReader()
        reader.onload = (e) => {
          var image = e.target.result
          image = this.image.split(",")[1]
          var data = {
            "payload": {
              "image": {
                "imageBytes": image
              }
            }
          }
          axios.post(URL,data,config)
            .then(res => {
              this.$store.state.payload = res.data.payload
              console.log('image upload response > ', res)
            })
            .catch(e => {console.log(e)})
        }
        reader.readAsDataURL(event.target.files[0])
      }
    }
  },
};
</script>

<style lang="scss">
#Upload {
}
</style>