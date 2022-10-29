<template>
  <div class="home">
    <div class="left">
      <div style="height:3vh; font-size:20px;">인식 준비완료 메세지가 뜨면 다음 사람이 들어와주세요</div>
      <div class="videoview">
        <div class="status" v-if="status==='done'">인식 완료</div>
        <div class="status" v-if="status==='ready'">인식 준비완료</div>
        <video ref="video" class="video" id="camera--view" autoplay></video>
        <canvas ref="canvas" class="video" style="display:none;"></canvas>
      </div>
      <!-- <button @click="capture">test</button>
      <img ref="test" style="object-fit:contain; width:160px;"> -->
      <div class="leftcontent" style="display:flex; flex-direction:column; height:10vh; gap:2vh;">
        <div class="leftcontent" style="display:flex; flex-direction:row; justify-content: space-between; height:4vh;">
          <button @click="connect">연결하기</button>
          <div style="display:flex; flex-direction:row; justify-content:center; align-items:center;">
            <div style="display:flex; height:4vh; align-items:center; line-height:20px;">연결 상태:</div>
            <div style="height:2vh; width:2vh; background-color:#1DCB9D; border-radius:10px;" v-if="this.connected===true"></div>
            <div style="height:2vh; width:2vh; background-color:crimson; border-radius:10px;" v-else></div>
          </div>
        </div>
        <div class="leftcontent" style="display:flex; flex-direction:row; justify-content: space-between; height:4vh;">
          <select v-model="name">
            <option selected="true" hidden value=null>위병소 선택</option>
            <option v-for="item in list" :key="item">{{item}}</option>
          </select>
          <button @click="start">시작</button>
          <button @click="capture">test</button>
        </div>
        <!-- <button @click="listtest">listtest</button> -->
        <!-- <button @click="test1">test1</button>
        <button @click="test2">test2</button>
        <button @click="test3">test3</button>
        <button @click="reset">reset</button> -->
      </div>
    </div>
    <div class="right" v-if="!(this.connected)">
      <div style="display:flex; background-color:#9C9DB2; width:270px; height:80px; font-size:20px; align-items:center; justify-content:center; border-radius:10px; color:#585767; font-weight: 600; ">
        연결상태를 확인해주세요
      </div>
    </div>
    <div class="right" v-else-if="this.data['imgview']">
      <img ref="back" class="back">
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
              전투복
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
        url : `wss://117.17.110.220:7778/v1/single`,
        img : null,
        setI : null,
        name : null,
        connected: false,
        status : null
      }
    },
  methods: {
    // listtest(){
    //   this.list=["1정문","2정문","3정문"]
    // },
    // test1(){
    //   this.data["imgview"]=true;
    //   this.$refs.back.src=this.img
    //   this.data["kind"]="blue";
    //   this.data["hair"]=true;
    //   this.data["nametag"]=false;
    //   this.data["level"]=true;
    // },
    // test2(){
    //   this.data["imgview"]=true;
    //   this.$refs.back.src=this.img
    //   this.data["kind"]="green";
    //   this.data["hair"]=true;
    //   this.data["nametag"]=true;
    //   this.data["level"]=false;
    //   this.data["flag"]=true;
    // },
    // test3(){
    //   this.data["imgview"]=true;
    //   this.$refs.back.src=this.img
    //   this.data["kind"]="black";
    //   this.data["hair"]=true;
    //   this.data["nametag"]=true;
    //   this.data["level"]=false;
    //   this.data["ma"]=true;
    //   this.data["neck"]=true;
    // },
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
      this.status=null;
    },
    connect() {
      console.log("start")
      this.socket = new WebSocket(this.url)
      this.socket.onopen = () => {
        console.log({ type: 'INFO', msg: 'CONNECTED' })
        this.connected=true;
      }
      this.socket.onerror = () => {
        console.log({ type: 'ERROR', msg: 'ERROR:'})
      }
      this.socket.onmessage = ({ data }) => {
        console.log({ type: 'RECV', msg: 'RECV:' + data }, new Date() )
        var msg = JSON.parse(data)
        switch(msg.type) {
          case "list":{
            this.list=msg.list;
          }
          case "result":{
            this.data["imgview"]=true;
            this.data["kind"]=msg.kind;
            this.data["hair"]=msg.hair;
            this.data["nametag"]=msg.nametag;
            this.data["level"]=msg.leveltag;
            this.data["ma"]=msg.muffler;
            this.data["neck"]=msg.neck;
            this.data["flag"]=msg.flag;
            this.$refs.back.src=msg.photo;
          }     
          case "status":{
            this.status=msg.status;
          }   
        }
      }
      this.socket.onclose = (msg) => {
        console.log({ type: 'ERROR', msg: 'Closed (Code: ' + msg.code + ', Message: ' + msg.reason + ')' })
        this.stop();
        this.reset();
      }
    },
    start(){
      if(!this.connected){
        alert("연결상태를 확인하세요")
      }
      else if(this.name==null){
        alert("위병소를 선택하세요")
      }
      else{
        this.setI=setInterval(this.capture,1000);
      }
    },
    stop(){
      clearInterval(this.setI);
      this.connected=false;
    },
    capture() {
      const video = this.$refs.video
      const canvas = this.$refs.canvas
      const ctx = canvas.getContext('2d')
      let canvas_width=video.videoWidth;
      let canvas_height=video.videoHeight;
      canvas.width=canvas_width;
      canvas.height=canvas_height;
      ctx.drawImage(video, 0, 0, canvas_width, canvas_height);
      this.img = canvas.toDataURL('image/webp')
      var msg = {
        name:this.name,
        photo:this.img
      }
      this.socket.send(JSON.stringify(msg))
      console.log("send : ", new Date())
    }
  },
  mounted() {
    navigator.mediaDevices.getUserMedia({
      video: {width:1920,height:1080}, audio: false
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
    position:relative;
  }
  .videoview{
    object-fit:contain;
    width:490px;
    height:35vh;
  }
  .status{
    background-color:gray;
    position:absolute;
    z-index:100;
    left:35%;
    right:35%;
    border-radius: 20px;
    font-size:20px;
  }
  .leftcontent{
    width:490px;
  }
  .video{
    transform: rotateY(180deg);
    width:490px;
    height:35vh;
    object-fit:contain;
  }
  .right{
    display:flex;
    flex-direction: row;
    align-content: center;
    align-items: center;
    justify-content: center;
    /* gap: 60px; */
    width:60%;
    height:100%;
  }
  .back{
    object-fit: contain;
    width:400px;
  }
  .result{
    display:flex;
    justify-content: center;
    align-items: center;
    width:240px;
  }
  .content{
    position:relative;
    width:240px;
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
  button{
    border:none; 
    border-radius: 10px; 
    background-color:#9C9DB2; 
    color:black; 
    font-weight: 600; 
  }
  button:hover{
    transform: scale(1.1); 
    cursor: pointer;
  }
  @media (max-width: 1200px) {
  .home{
    flex-direction: column;
  }
  .left{
    width:100%;
    height:50vh;
  }
  .videoview{
    width:300px;
  }
  .video{
    width:300px;
  }
  .leftcontent{
    width:300px;
  }
  .right{
    width:100%;
    height:50vh;
  }
  .back{
    width: 160px;
  }
}
</style>