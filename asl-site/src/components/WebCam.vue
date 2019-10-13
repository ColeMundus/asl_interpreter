<template lang="pug">
  div(id="WebCam").flex.flex-column.center.justify-center.items-center
    video(ref="video").webcam.pa3
    button(@click.prevent="capture").capture Capture
</template>

<script>
import axios from 'axios'

export default {
  name: "WebCam",
  data () {
    return {
      mediaStream: null
    }
  },
  methods: {
    capture() {
      const mediaStreamTrack = this.mediaStream.getVideoTracks()[0]
      const imageCapture = new window.ImageCapture(mediaStreamTrack)
      return imageCapture.takePhoto().then(blob => {
        var reader = new FileReader()
        reader.readAsDataURL(blob)
        reader.onloadend = () => {
          const URL = 'https://automl.googleapis.com/v1beta1/projects/905505838894/locations/us-central1/models/ICN618229000019378176:predict'
          //let token = "ya29.c.Kl6bB-gsJFXVNUer5OKkciPV0W2MrE450TfjweHHuawaew9UqsDCi_AlWzk4H3YQR-pQaWRNWzHBg7K9LyVFEgiiORED4nzz8uxVVb0PhQXrA2JOdhDiEJSHcKAMdwnf"
          let config = {
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${this.$store.state.token}`
            }
          }
          var base64data = reader.result
          base64data = base64data.split(",")[1]
          var data = {
            "payload": {
              "image": {
                "imageBytes": base64data
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
        //console.log(blob)
      })
    }
  },
  mounted () {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(mediaStream => {
        this.mediaStream = mediaStream
        this.$refs.video.srcObject = mediaStream
        this.$refs.video.play()
      })
      .catch(error => console.error('getUserMedia() error:', error))
  },
  destroyed () {
    const tracks = this.mediaStream.getTracks()
    tracks.map(track => track.stop())
  }
}
</script>

<style lang="scss">
#WebCam {
}
</style>
