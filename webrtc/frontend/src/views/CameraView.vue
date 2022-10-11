<template>
  <div class="home">
    <button id="camera--trigger" @click="capture">capture</button>
    <video ref="video" id="camera--view" autoplay width="300"></video>
    <canvas ref="canvas" style="display:none;" width="300" height="225"></canvas>
    <img ref="image" style="object-fit: contain;">
    <img ref="back" style="object-fit: contain;">
    <button @click="connect">Connect</button>
    <button @click="disconnect">Disconnect</button>
    <button @click="send">Send</button>
  </div>
</template>

<script>
export default {
  name: 'Capture',
  data() {
      return {
        socket : null,
        url : `wss://117.17.110.220:7778/v1/ws2`,
        img : null,
        backimg: null,
        // setI : null,
        // kind: '해군 동정복',
        // one:["태극기",true],
        // two:["이름표",false],
        // three:["계급장",true],
        // four:["두발",true],
        // five:null,
        // resive:false,
        // capturing:false,
      }
    },
  methods: {
    send() {
      this.socket.send(this.img);
    },
    connect() {
      console.log("start")
      this.socket = new WebSocket(this.url)
      this.socket.onopen = () => {
        console.log({ type: 'INFO', msg: 'CONNECTED' })
      }
      this.socket.onerror = () => {
        console.log({ type: 'ERROR', msg: 'ERROR:' })
      }
      this.socket.onmessage = ({ data }) => {
        console.log({ type: 'RECV', msg: 'RECV:' + data })
        this.$refs.back.src=data;
      }
      this.socket.onclose = (msg) => {
        console.log({ type: 'ERROR', msg: 'Closed (Code: ' + msg.code + ', Message: ' + msg.reason + ')' })
      }
    },
    capture() {
      const video = this.$refs.video
      const canvas = this.$refs.canvas
      const image = this.$refs.image
      const ctx = canvas.getContext('2d')
      ctx.drawImage(video, 0, 0, video.clientWidth, video.clientHeight);
      this.img = canvas.toDataURL('image/webp');
      image.src = this.img;
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