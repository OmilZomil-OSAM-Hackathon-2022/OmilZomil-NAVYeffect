<template>
  <div class="home">
    <div class="left">
      <video ref="video" class="video" id="camera--view" autoplay></video>
      <canvas ref="canvas" class="video" style="display:none;"></canvas>
      <div style="display:flex; flex-direction:row height:5vh;">
        <button @click="connect">connect</button>
        <button @click="listtest">listtest</button>
        <select v-model="name">
                  <option v-for="item in list" :key="item">{{item}}</option>
        </select>
        <button @click="start">start</button>
        <button @click="test1">test1</button>
        <button @click="test2">test2</button>
        <button @click="test3">test3</button>
        <button @click="reset">reset</button>
      </div>
    </div>
    <div class="right" v-if="this.data['imgview']">
      <img ref="back" class="back" src="@/assets/images/test.svg">
      <div class="result">
        <div class="content" v-if="data['kind']==='blue'">
          <div class="kind">
            <div class="res-left">
              복장 종류:
            </div>
            <div class="res-right" style="color: #4471FB;">
              <img class="kind-img" src="@/assets/icons/blue.svg" />
              해군 샘당
            </div>
          </div>
          <div class="hair">
            <div class="res-left">
              두발:
            </div>
            <div class="res-right">
              <img v-if="data['hair']" src="@/assets/icons/pass.svg" />
              <img v-else src="@/assets/icons/fail.svg" />
            </div>
          </div>
          <div class="level">
            <div class="res-left">
              계급장:
            </div>
            <div class="res-right">
              <img v-if="data['level']" src="@/assets/icons/pass.svg" />
              <img v-else src="@/assets/icons/fail.svg" />
            </div>
          </div>
          <div class="nametag">
            <div class="res-left">
              이름표:
            </div>
            <div class="res-right">
              <img v-if="data['nametag']" src="@/assets/icons/pass.svg" />
              <img v-else src="@/assets/icons/fail.svg" />
            </div>
          </div>
        </div>
        <div class="content" v-if="data['kind']==='green'">
          <div class="kind">
            <div class="res-left">
              복장 종류:
            </div>
            <div class="res-right" style="color: #1DCB9D;">
              <img class="kind-img" src="@/assets/icons/green.svg" />
              해군 전투복
            </div>
          </div>
          <div class="hair">
            <div class="res-left">
              두발:
            </div>
            <div class="res-right">
              <img v-if="data['hair']" src="@/assets/icons/pass.svg" />
              <img v-else src="@/assets/icons/fail.svg" />
            </div>
          </div>
          <div class="level">
            <div class="res-left">
              계급장:
            </div>
            <div class="res-right">
              <img v-if="data['level']" src="@/assets/icons/pass.svg" />
              <img v-else src="@/assets/icons/fail.svg" />
            </div>
          </div>
          <div class="nametag">
            <div class="res-left">
              이름표:
            </div>
            <div class="res-right">
              <img v-if="data['nametag']" src="@/assets/icons/pass.svg" />
              <img v-else src="@/assets/icons/fail.svg" />
            </div>
          </div>
          <div class="flag">
            <div class="res-left">
              태극기:
            </div>
            <div class="res-right">
              <img v-if="data['flag']" src="@/assets/icons/pass.svg" />
              <img v-else src="@/assets/icons/fail.svg" />
            </div>
          </div>
        </div>
        <div class="content" v-if="data['kind']==='black'">
          <div class="kind">
            <div class="res-left">
              복장 종류:
            </div>
            <div class="res-right" style="color: #585767;">
              <img class="kind-img" src="@/assets/icons/black.svg" />
              해군 동정복
            </div>
          </div>
          <div class="hair">
            <div class="res-left">
              두발:
            </div>
            <div class="res-right">
              <img v-if="data['hair']" src="@/assets/icons/pass.svg" />
              <img v-else src="@/assets/icons/fail.svg" />
            </div>
          </div>
          <div class="level">
            <div class="res-left">
              계급장:
            </div>
            <div class="res-right">
              <img v-if="data['level']" src="@/assets/icons/pass.svg" />
              <img v-else src="@/assets/icons/fail.svg" />
            </div>
          </div>
          <div class="nametag">
            <div class="res-left">
              이름표:
            </div>
            <div class="res-right">
              <img v-if="data['nametag']" src="@/assets/icons/pass.svg" />
              <img v-else src="@/assets/icons/fail.svg" />
            </div>
          </div>
          <div class="ma">
            <div class="res-left">
              마후라:
            </div>
            <div class="res-right">
              <img v-if="data['ma']" src="@/assets/icons/pass.svg" />
              <img v-else src="@/assets/icons/fail.svg" />
            </div>
          </div>
          <div class="neck">
            <div class="res-left">
              네카치프 & 링:
            </div>
            <div class="res-right">
              <img v-if="data['neck']" src="@/assets/icons/pass.svg" />
              <img v-else src="@/assets/icons/fail.svg" />
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="right">
      <img class="loading" src="@/assets/icons/loading.svg"  />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Capture',
  data() {
      return {
        data:{
          "imgview" : false,
          "kind" : null,
          "hair" : null,
          "nametag" : null,
          "level" : null,
          "ma" : null,
          "neck" : null,
          "flag" : null
        },
        list:[],
        socket : null,
        url : `wss://117.17.110.220:7778/v1/test`,
        img : null,
        setI : null,
        name : null,
      }
    },
  methods: {
    listtest(){
      this.list=["1정문","2정문","3정문"]
    },
    test1(){
      this.data["imgview"]=true;
      this.data["kind"]="blue";
      this.data["hair"]=true;
      this.data["nametag"]=false;
      this.data["level"]=true;
    },
    test2(){
      this.data["imgview"]=true;
      this.data["kind"]="green";
      this.data["hair"]=true;
      this.data["nametag"]=true;
      this.data["level"]=false;
      this.data["flag"]=true;
    },
    test3(){
      this.data["imgview"]=true;
      this.data["kind"]="black";
      this.data["hair"]=true;
      this.data["nametag"]=true;
      this.data["level"]=false;
      this.data["ma"]=true;
      this.data["neck"]=true;
    },
    reset(){
      this.data["imgview"]=false;
      this.data["kind"]=null;
      this.data["hair"]=null;
      this.data["nametag"]=null;
      this.data["level"]=null;
      this.data["flag"]=null;
      this.data["ma"]=null;
      this.data["neck"]=null;
      this.list=[];
      this.name=null;
    },
    connect() {
      console.log("start")
      this.socket = new WebSocket(this.url)
      this.socket.onopen = () => {
        console.log({ type: 'INFO', msg: 'CONNECTED' })
      }
      this.socket.onerror = () => {
        console.log({ type: 'ERROR', msg: 'ERROR:'})
      }
      this.socket.onmessage = ({ data }) => {
        console.log({ type: 'RECV', msg: 'RECV:' + data })
        var msg = JSON.parse(data)
        switch(msg.type) {
          case "list":{
            this.list=msg.list;
          }
          case "result":{
            this.$refs.back.src=msg.photo;
            this.data["kind"]=msg.kind;
            this.data["hair"]=msg.hair;
            this.data["nametag"]=msg.nametag;
            this.data["level"]=msg.leveltag;
            this.data["ma"]=msg.muffler;
            this.data["neck"]=msg.neck;
            this.data["flag"]=msg.flag;
            this.data["imgview"]=true;
          }        
        }
      }
      this.socket.onclose = (msg) => {
        console.log({ type: 'ERROR', msg: 'Closed (Code: ' + msg.code + ', Message: ' + msg.reason + ')' })
      }
    },
    start(){
      this.setI=setInterval(this.capture,1000);
    },
    capture() {
      const video = this.$refs.video
      const canvas = this.$refs.canvas
      const image = this.$refs.image
      const ctx = canvas.getContext('2d')
      ctx.drawImage(video, 0, 0, video.clientWidth, video.clientHeight);
      this.img = canvas.toDataURL('image/webp')
      var msg = {
        name:this.name,
        photo:this.img
      }
      this.socket.send(JSON.stringify(msg))
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

<style scoped>
  @keyframes load {
    0% {transform:rotate(0deg);}
    100% {transform: rotate(360deg);}
  }
  .home{
    display:flex;
    flex-direction: row;
    justify-content: center;
    width:100%;
    height:90vh;
  }
  .left{
    display:flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width:40%;
    height:100%;
  }
  .video{
    /* transform: rotateY(180deg); */
    width:490px;
    height:45vh;
  }
  .right{
    display:flex;
    flex-direction: row;
    align-content: center;
    justify-content: center;
    /* gap: 60px; */
    width:60%;
    height:100%;
  }
  .back{
    width:160px;
  }
  .result{
    display:flex;
    justify-content: center;
    align-items: center;
    width:240px;
  }
  .content{
    position:relative;
    width:220px;
    height:220px;
    display: flex;
    flex-direction: column;
    /* gap:16px; */
    justify-content: space-between;
  }
  .kind{
    display: flex;
    justify-content: space-between;
    align-content: center;
    height: 39.96px;
  }
  .hair{
    display: flex;
    justify-content: space-between;
    align-content: center;
    height: 39.96px;
  }
  .level{
    display: flex;
    justify-content: space-between;
    align-content: center;
    height: 39.96px;
  }
  .nametag{
    display: flex;
    justify-content: space-between;
    align-content: center;
    height: 39.96px;
  }
  .flag{
    display: flex;
    justify-content: space-between;
    align-content: center;
    height: 39.96px;
  }
  .ma{
    display: flex;
    justify-content: space-between;
    align-content: center;
    height: 39.96px;
  }
  .neck{
    display: flex;
    justify-content: space-between;
    align-content: center;
    height: 39.96px;
  }
  .res-left{
    display: flex;
    flex-direction: row;
    align-items: center;
    height:28px;
  }
  .res-right{
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 6px;
    height: 28px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 600;
    font-size: 24px;
    line-height: 28px;
    letter-spacing: 0.373762px;
  }
  .kind-img{
    width: 24px;
    height: 24px;
  }
  .loading{
    width:50px;
    animation: load 0.7s linear infinite;
  }
  @media (max-width: 1200px) {
  .home{
    flex-direction: column;
  }
  .left{
    width:100%;
    height:50vh;
  }
  .right{
    width:100%;
    height:50vh;
  }
}
</style>