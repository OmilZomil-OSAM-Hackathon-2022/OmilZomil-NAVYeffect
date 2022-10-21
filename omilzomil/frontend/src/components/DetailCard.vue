<template>
  <transition 
    name="overlay"
    appear
  >
    <div
      class="overlay"
      @click.self="$emit('close',event)"
    >
      <div class="overlay-card card">
        <img
          src="@/assets/images/test.png"
        >
        <div class="detail">
          <div class="info">
            <div class="division">
              소속 : 대한민군 {{ item.affiliation_title }}
            </div>
            <div class="uClass">
              계급 : {{ item.rank_title }}
            </div>
            <div class="uName">
              이름 : {{ item.name }}
            </div>
          </div>
          <div class="time">
            시간 : {{ item.access_time.replace('T',' ') }}
          </div>
          <div style="display:flex;justify-content:space-between;width:100%;">
            <div class="dress-type">
              복장 : <DressType
                :dress-type="item.uniform"
                :title="item.uniform_title"
              />
            </div>
            <div
              v-if="isAdmin"
              class="match-user-wrap"
            >
              <select v-model="match">
                <option
                  selected
                  disabled
                  :value="null"
                >
                  부대를 선택해 주세요
                </option>
                <option
                  v-for="u in units"
                  :key="u.unit_id"
                  :value="u.unit_id"
                >
                  {{ u.unit }}
                </option>
              </select>
              <button @click="matchUnit()">
                확인
              </button>
            </div>
          </div>
          <div class="parts-grid">
            <div
              v-for="d in details" 
              :key="d.detail_id"
              class="parts"
            >
              <div class="parts-image">
                <div
                  v-if="isAdmin"
                  class="toggle-wrap"
                >
                  <input
                    :id="d.detail_id"
                    v-model="d.status"
                    type="checkbox"
                    hidden
                    @change="changeStatus(d)"
                  > 
                  <label
                    :for="d.detail_id"
                    :class="['toggleSwitch',d.status?'checked':'']"
                  >
                    <span class="toggleMessage" />
                    <span class="toggleButton" />
                  </label>
                </div>
                <div
                  v-if="!d.is_valid"
                  class="error-wrap"
                >
                  <img
                    src="@/assets/icons/alert-error.svg"
                    style="width:24px;height:24px;"
                  >
                  인식 오류
                </div>
              </div>
              <div class="parts-info">
                <div class="parts-name">
                  {{ d.apperance_title }}
                </div>
                <GoodBadTag :is-good="d.status" />
              </div>
            </div>
          </div>
        </div>
        <img
          class="close"
          src="@/assets/icons/close-thick.svg"
          @click="$emit('close')"
        >
      </div>
    </div>
  </transition>
</template>

<script>
import DressType from './DressType.vue';
import GoodBadTag from './GoodBadTag.vue';
export default {
    components: { DressType, GoodBadTag },
    props: {
        item: {
            type: Object,
            default: null,
        },
    },
    emits: ["close"],
    data(){
      return {
        toggle:false,
        units:[],
        details:[],
        appearances:[],
        match:null
      }
    },
    computed:{
      getUser () {
        return this.$store.getters.getUser;
      },
      isAdmin(){
        return this.getUser['role'] >= 2;
      }
    },
    async mounted(){
      try{
        this.appearances = (await this.$axios.get('/appearance/')).data;
        this.units = (await this.$axios.get(`/vacation/name/?access_time=${this.item.access_time}&affiliation=${this.item.affiliation}&rank=${this.item.rank}&name=${this.item.name}`)).data;
        this.details = (await this.$axios.get(`/rtm/detail/${this.item.inspection_id}`)).data;
        for(var i=0;i<this.details.length;i++){
          this.details[i].apperance_title = this.appearances.filter(a=>a.appearance_id == this.details[i].apperance_type)[0].appearance;
        }
      }catch(err){
        console.log(err);
      }
    },
    methods:{
      async matchUnit(){
        try{
          // await this.$axios.get(``);this.match
        }catch(err){
          console.log(err);
        }
      },
      async changeStatus(d){
        try{
          await this.$axios.put(`/rtm/detail/status/${d.detail_id}`,{
            status:d.status
          });
        }catch(err){
          console.log(err);
        }
      }
    },
}
</script>

<style scoped>

.overlay{
  position: fixed;
  /* display:none; */
  display:flex;
  justify-content: center;
  align-items: center;
  width:100%;
  height:100%;
  top:0;
  left:0;
  right:0;
  bottom:0;
  background-color:rgba(0,0,0,0.5);
  z-index:1000000;
}
.overlay-card{
  position: relative;
  box-sizing: border-box;
  width:1080px;
  height:600px;
  padding:40px;
  display:flex;
  gap:40px;


  font-family: 'Roboto';
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 19px;
    /* identical to box height */

  letter-spacing: 0.15px;
}
.overlay-card img{
  width:380px;
  height:100%;
}
.overlay-card .detail{
  width:580px;
  height:100%;
  display:flex;
  flex-direction: column;
  align-items: flex-start;
  gap:24px;
}
.overlay-card .detail .info{
  display:flex;
  gap:30px;
}
.overlay-card .close{
  position:absolute;
  right:20px;
  top:20px;
  width:16px;
  height:16px;
}

.dress-type{
    display:flex;
    align-items: center;
    gap:4px;
}

.parts-grid{
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap:40px;
}
.parts{
    display:flex;
    flex-direction: column;
    justify-content: center;
    gap:10px;
}
.parts-image{
  position:relative;
    background: #D9D9D9;
    border-radius: 10px;
    width:160px;
    height:120px;
    overflow:hidden;
}
.parts .parts-info{
    display:flex;
    width:100%;
    justify-content: space-between;
}

.match-user-wrap{
  display:flex;
  gap:10px;
  margin-right:18px;
}


.match-user-wrap select{
  box-sizing: border-box;

  padding: 0px 12px;
  width: 281px;
  height: 31px;

  background: #ffffff;
  /* Dark8 */
  border: 2px solid #d9d8e8;
  border-radius: 8px;
  font-weight: 400;
  font-size: 12px;
  line-height: 14px;
  /* identical to box height */

  letter-spacing: 0.4px;
  -webkit-appearance: none;

  background: url("@/assets/icons/mdi_chevron-down.svg") no-repeat scroll 10px center;
  background-position: right 5px center;
  /* background-size:13px; */
  color:var(--color)
}
.match-user-wrap button{
  height:31px;
  background:#9155EB33;
  color:#9155EB;
  border:none;
  border-radius: 4px;
}

.error-wrap{
  position:absolute;
  left:0px;
  top:0px;
  width:100%;
  height:100%;
  background: rgba(128, 128, 128, 0.8);
  display:flex;
  flex-direction:column;
  justify-content:center;
  align-items:center;
  gap:8px;
  
  font-weight: 700;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 0.1px;

  color: #FFFFFF;

}

.toggleSwitch {
  width: 52px;
  height: 22.75px;
  display: block;
  position: relative;
  border-radius: 2rem;
  background-color: #fff;
  border: 0.8125px solid #D9D8E8;
  border-radius: 32.5px;
  cursor: pointer;
}

.toggleSwitch .toggleButton {
  
  position: absolute;
  top: 50%;
  /* left: .2rem; */
  transform: translateY(-50%);
  width: 16.25px;
  height: 16.25px;

  left:30px;
  /* top: calc(50% - 16.25px/2); */


  background: rgba(255, 84, 103, 0.2);
  /* Error */
  border: 1.625px solid #FF5467;
  border-radius: 50%;
}
.toggleSwitch .toggleMessage{
  /* display:none; */
  
}
.toggleSwitch .toggleMessage::after{
  font-weight: 600;
  font-size: 9.75px;
  line-height: 11px;
  letter-spacing: 0.203125px;

  left:8.12px;
  /* top:50%; */
  top: 5.69px;
  position:absolute;
  /* Success */
  color: #FF5467;
  content:'불량';
}

/* 체크박스가 체크되면 변경 이벤트 */

.checked .toggleButton {
  background: rgba(63, 198, 184, 0.2);
  /* Success */

  left: 3.25px;
  border: 1.625px solid #3FC6B8;
}
.checked .toggleMessage::after{
  left:27px;
  color: #3FC6B8;
  content:'양호';
}
.toggleSwitch, .toggleButton , .toggleMessage::after{
  transition: all 0.2s ease-in;
}

.toggle-wrap{
  z-index:10000;
  position:absolute;
  top:4px;
  right:5px;
}
</style>