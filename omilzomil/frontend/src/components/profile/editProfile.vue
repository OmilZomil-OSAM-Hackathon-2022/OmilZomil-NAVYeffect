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
        <div class="title">
          군번
        </div>
        <input
          v-model="dogTag.data"
          placeholder="군번"
          :class="{
            success: dogTag.check == 1,
            error: dogTag.check == 2,
          }"
          @change="checkName"
        >
      </div>
      <div class="input-wrap">
        <div class="title">
          소속
        </div>
        <select v-model="division.data">
          <option
            value=""
            disabled
            selected
          >
            소속을 선택하세요.
          </option>
          <option value="육군">
            육군
          </option>
          <option value="해군">
            해군
          </option>
          <option value="공군">
            공군
          </option>
          <option value="해병대">
            해병대
          </option>
          <option value="국방부직속">
            국방부직속
          </option>
        </select>
      </div>
      <div class="input-wrap">
        <div class="title">
          부대
        </div>
        <select v-model="armyUnit.data">
          <option
            value=""
            disabled
            selected
          >
            부대를 선택하세요.
          </option>

          <option value="계룡대 근무지원단">
            계룡대 근무지원단
          </option>
          <option value="1함대">
            1함대
          </option>
          <option value="2함대">
            2함대
          </option>
          <option value="3함대">
            3함대
          </option>
          <option value="작전사">
            작전사
          </option>
        </select>
      </div>
    </div>
    <div class="f1">
      <h2>&nbsp;</h2>
      <div class="input-wrap">
        <div class="title">
          계급
        </div>
        <select v-model="uClass.data">
          <option
            value=""
            disabled
            selected
          >
            계급을 선택하세요.
          </option>

          <option value="이병">
            이병
          </option>
          <option value="일병">
            일병
          </option>
          <option value="상병">
            상병
          </option>
          <option value="병장">
            병장
          </option>
        </select>
      </div>
      <div class="input-wrap">
        <div class="title">
          비밀번호
        </div>
        <input
          v-model="password.data"
          placeholder="비밀번호"
          :class="{
            success: password.check == 1,
            error: password.check == 2,
          }"
          type="password"
          @change="checkName"
        >
      </div>
      <div class="input-wrap">
        <div class="title">
          비밀번호 확인
        </div>
        <input
          v-model="passwordConfirm.data"
          placeholder="비밀번호"
          :class="{
            success: passwordConfirm.check == 1,
            error: passwordConfirm.check == 2,
          }"
          type="password"
          @change="checkName"
        >
      </div>
      <div class="wrap-button">
        <button>저장</button>
      </div>
    </div>
  </div>
</template>

<script>
class inputData {
  constructor() {
    this.data = "";
    this.check = 1;
  }
}
export default {
    data(){
        return{
            name: new inputData(),
            dogTag: new inputData(),
            division: new inputData(),
            armyUnit: new inputData(),
            uClass: new inputData(),
            uid: new inputData(),
            password: new inputData(),
            passwordConfirm: new inputData(),
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
    justify-content: flex-start;
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
</style>