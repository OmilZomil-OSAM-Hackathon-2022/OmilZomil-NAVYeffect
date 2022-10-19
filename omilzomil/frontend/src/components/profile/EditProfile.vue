<template>
  <div class="page">
    <div class="f1">
      <h2>개인정보</h2>
      <div class="input-wrap">
        <div class="title">
          이름
        </div>
        <input
          v-model="name.data"
          placeholder="성명"
          :class="{
            success: name.check == 1,
            error: name.check == 2,
          }"
          @change="checkName"
        >
      </div>
      <div class="input-wrap">
        <div
          class="title"
          style="display:flex;justify-content:space-between;align-items: flex-end;"
        >
          군번 <div
            v-if="dogTag.check == 3"
            style="color:red;font-size:12px;"
          >
            이미 존재하는 군번입니다.
          </div>
        </div>
        <input
          v-model="dogTag.data"
          placeholder="군번"
          :class="{
            success: dogTag.check == 1,
            error: dogTag.check == 2 || dogTag.check == 3,
          }"
          @change="checkDogTag"
        >
      </div>
      <div class="input-wrap">
        <div class="title">
          소속
        </div>
        <select v-model="division.data">
          <option
            v-for="d in divisionList"
            :key="d.affiliation_id"
            :value="d.affiliation_id"
          >
            {{ d.affiliation }}
          </option>
        </select>
      </div>
      <div class="input-wrap">
        <div class="title">
          부대
        </div>
        <select v-model="armyUnit.data">
          <option
            v-for="u in unitList"
            :key="u.unit_id"
            :value="u.unit_id"
          >
            {{ u.unit }}
          </option>
        </select>
      </div>
      <div class="input-wrap">
        <div class="title">
          계급
        </div>
        <select v-model="uClass.data">
          <option
            v-for="c in classList"
            :key="c.rank_id"
            :value="c.rank_id"
          >
            {{ c.rank }}
          </option>
        </select>
      </div>
      <div class="wrap-button">
        <button @click="updateUser">
          수정
        </button>
      </div>
    </div>
    <div class="f1">
      <h2>&nbsp;</h2>
      <div class="input-wrap">
        <div class="title">
          기존 비밀번호
          <div
            v-show="beforePassword.check == 2"
            class="input-warning"
          >
            비밀번호가 틀렸습니다!
          </div>
        </div>
        <input
          v-model="beforePassword.data"
          placeholder="기존 비밀번호"
          :class="{
            success: beforePassword.check == 1,
            error: beforePassword.check == 2,
          }"
          type="password"
          @change="checkBeforePass"
        >
      </div>
      <div class="input-wrap">
        <div class="title">
          비밀번호
          <div
            :class="[{'input-comment':password.check != 2},{'input-warning':password.check == 2}]"
          >
            8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요.
          </div>
        </div>
        <input
          v-model="password.data"
          placeholder="비밀번호"
          :class="{
            success: password.check == 1,
            error: password.check == 2,
          }"
          type="password"
          @change="checkPassword"
        >
      </div>
      <div class="input-wrap">
        <div class="title">
          비밀번호 확인
          <div
            v-show="passwordConfirm.check == 2"
            class="input-warning"
          >
            비밀번호가 다릅니다!
          </div>
        </div>
        <input
          v-model="passwordConfirm.data"
          placeholder="비밀번호 확인"
          :class="{
            success: passwordConfirm.check == 1,
            error: passwordConfirm.check == 2,
          }"
          type="password"
          @change="checkPasswordCofirm"
        >
      </div>
      <div class="wrap-button">
        <button @click="changePass">
          수정
        </button>
      </div>
    </div>
  </div>
</template>

<script>
class inputData {
  constructor(check = 0) {
    this.data = "";
    this.check = check;
  }
}
export default {
    data(){
        return{
            name: new inputData(1),
            dogTag: new inputData(1),
            division: new inputData(1),
            armyUnit: new inputData(1),
            uClass: new inputData(1),
            uid: new inputData(1),
            beforePassword: new inputData(),
            password: new inputData(),
            passwordConfirm: new inputData(),
            unitList:[],
            divisionList:[],
            classList:[],
        }
    },
    computed:{
      initUser(){
        return this.$store.getters.getUser;
      }
    },
    async mounted(){
      this.name.data = this.initUser.full_name;
      this.dogTag.data = this.initUser.dog_number;
      this.division.data = this.initUser.affiliation;
      this.armyUnit.data = this.initUser.military_unit;
      this.uClass.data = this.initUser.rank;

      try{
        const unitList = await this.$axios.get('/unit/');
        const divisionList = await this.$axios.get('/affiliation/');
        const classList = await this.$axios.get('/rank/');

        this.unitList = unitList.data;
        this.divisionList = divisionList.data;
        this.classList = classList.data;
      }catch(err){
        console.log(err);
      }
    },
    methods:{
      updateUser(){
        // console.log("Asdfasd");
        this.$axios.put(`/user/information/${this.initUser.user_id}`,{
          full_name: this.name.data,
          dog_number: this.dogTag.data,
          affiliation: this.division.data,
          military_unit: this.armyUnit.data,
          rank: this.uClass.data
        }).then((res)=>{
          if(res.data.success){
            this.$axios.post('/login/test-token/').then((response)=>{
              console.log(response.data);
              if(response.data.success){
                this.$store.commit('setUser',response.data);
                alert("수정완료");
              }
            });
          }else{
            this.dogTag.check=3;
          }
        });
      },
      changePass(){
        if(this.passwordConfirm.data == this.password.data && this.password.check == 1){
          this.$axios.put(`/user/password/${this.initUser.user_id}`,{
            old_password:this.beforePassword.data,
            new_password:this.password.data
          }).then((res)=>{
            if(res.data.success){
              alert("변경 성공");
            }else{
              this.beforePassword.check = 2;
            }
          })
        }else{
          this.passwordConfirm.check = 2;
        }
      },
      checkName(){
        if(this.name.data == "") this.name.check = 2;
      },
      checkDogTag(){
        if(this.dogTag.data == "") this.dogTag.check = 2;
      },
      checkPassword(event) {
        let tmp = event.target.value;
        if (
          tmp &&
          /\d/.test(tmp) &&
          tmp.length <= 16 &&
          tmp.length >= 6 &&
          /[^A-Za-z0-9]/.test(tmp) &&
          /[A-Za-z]/.test(tmp)
        ) {
          this.password.check = 1;
          if (event.target.value == this.passwordConfirm.data) {
            this.passwordConfirm.check = 1;
          }else{
            this.passwordConfirm.check = 2;
          }
        } else {
          this.password.check = 2;
        }
      },
      checkPasswordCofirm(event) {
        if (
          event.target.value == this.password.data &&
          this.password.check == 1
        ) {
          this.passwordConfirm.check = 1;
        } else {
          this.passwordConfirm.check = 2;
        }
      },
      checkBeforePass(event){
        let tmp = event.target.value;
        if(tmp != "") this.beforePassword.check = 1;
        else this.beforePassword.check = 2;
      }
    }
}
</script>

<style scoped>

.f1{
    flex:1;
    padding-left:76px;
    width:100%;
    box-sizing: border-box;
    display:flex;
    flex-direction:column;
    align-items: flex-start;
}
.page h2{
    margin-bottom:32px;
    font-weight: 700;
    font-size: 16px;
    line-height: 19px;

    letter-spacing: 0.15px;
}

.input-wrap{
    width:428px;
    margin-bottom:32px;
}
.title{
    font-weight: 700;
    font-size: 16px;
    line-height: 19px;
    /* identical to box height */

    letter-spacing: 0.15px;
    /* float:left; */

    display:flex;
    justify-content: space-between;
    margin-bottom:16px;
}
select {
  box-sizing: border-box;

  padding: 0px 12px;
  width: 100%;
  height: 40px;

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
  background-position: right 12px center;
  /* background-size:13px; */
  color:var(--color)
}

input {
  box-sizing: border-box;

  /* Auto layout */
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 12px;
  width: 100%;
  height: 40px;

  background: #ffffff;
  /* Dark8 */
  border: 2px solid #d9d8e8;
  border-radius: 8px;
  /* padding-left: 40px; */
  /* margin-bottom: 40px; */

  font-weight: 400;
  font-size: 12px;
  line-height: 14px;
  /* identical to box height */

  letter-spacing: 0.4px;
  background: url("@/assets/icons/check.svg") no-repeat scroll 10px center;
  background-position: right 12px center;
  background-size:13px;
  color:var(--color);
}

input::placeholder{
  color:var(--color);
}

.wrap-button{
    width:100%;
    display:flex;
    justify-content:flex-end;
    box-sizing:border-box;
    padding-right:102px;
}
.wrap-button button{
    border:none;
    padding: 8px 12px;
    color:white;
    background: #9155EB;
border-radius: 8px;
}

.success {
  border: 2px solid #3fc6b8;
  background: url("@/assets/icons/check-success.svg") no-repeat scroll 10px
    center;
  background-position: right 12px center;
  background-size:13px;
}
.error {
  border: 2px solid #ff5467;
  background: url("@/assets/icons/error.svg") no-repeat scroll 10px center;
  background-position: right 12px center;
  background-size:13px;
}

.input-warning {
  font-size: 12px;
  color: #ff5467;
}
.input-comment {
  font-size: 12px;
  color: #616276;
}
</style>
