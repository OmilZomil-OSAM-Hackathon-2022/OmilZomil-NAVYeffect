<template>
  <div class="home">
    <button id="camera--trigger" @click="capture">capture</button>
    <video ref="video" id="camera--view" autoplay width="300"></video>
    <canvas ref="canvas" style="display:none;" width="300" height="225"></canvas>
    <img ref="image" style="object-fit: contain;">
  </div>
</template>

<script>
export default {
  name: 'Capture',
  methods: {
    capture() {
      const video = this.$refs.video
      const canvas = this.$refs.canvas
      const image = this.$refs.image
      const ctx = canvas.getContext('2d')

      ctx.drawImage(video, 0, 0, video.clientWidth, video.clientHeight);
      image.src = canvas.toDataURL('image/webp');




      console.log("test 1")
      fetch('/v1/')
      .then((response) => response.json())
      .then((data) => console.log(data));

      // WebSocket 연결 생성
      var ws = new WebSocket("wss://218.150.159.22:14491/v1/ws");
      


      ws.addEventListener('open', function (event) {
          console.log('Hello Server!');
      });

      ws.send("connetions")

      console.log('end')
    }
  },
  mounted() {
    navigator.mediaDevices.getUserMedia({
      video: { facingMode: "user"}, audio: false
    }).then(stream => {
      this.$refs.video.srcObject = stream;
    })
    .catch(function(error){
      console.error(error);
    })
  }
}
</script>