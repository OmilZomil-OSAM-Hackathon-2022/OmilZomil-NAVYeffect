<template>
  <div style="display: flex; width: 100%; height: 100vh">
    <div class="left">
      <img
        class="back"
        src="@/assets/images/loginBackground.svg"
      >
      <img
        class="hand"
        src="@/assets/images/hand.svg"
      >
      <img
        class="front"
        src="@/assets/images/topBackground.svg"
      >
      <div class="wrap-title">
        <h2>오밀조밀<br>복장과 두발을 검사하다</h2>
        <div class="title">
          <img
            width="52px"
            src="@/assets/logo.svg"
          >
          <h1>OMIL-ZOMIL</h1>
        </div>
      </div>
    </div>
    <div class="right">
      <div class="flow-wrap">
        <h2>회원가입</h2>
        <div class="title">
          <img
            width="52px"
            src="@/assets/logo.svg"
          >
          <h1>OMIL-ZOMIL</h1>
        </div>
        <div class="right-wrap">
          <form @submit.prevent="submitForm">
            <div class="input-label">
              <h3>이름</h3>
              <div
                v-show="name.check == 2"
                class="input-warning"
              >
                이름을 입력해주세요.
              </div>
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

            <div class="input-label">
              <h3>군번</h3>
              <div
                v-show="dogTag.check == 2"
                class="input-warning"
              >
                군번을 입력해주세요.
              </div>
            </div>
            <input
              v-model="dogTag.data"
              placeholder="군번"
              :class="{
                success: dogTag.check == 1,
                error: dogTag.check == 2,
              }"
              @change="checkDogTag"
            >

            <div class="input-label">
              <h3>소속</h3>
              <div
                v-show="division.check == 2"
                class="input-warning"
              >
                소속을 선택하세요.
              </div>
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

            <div class="input-label">
              <h3>부대</h3>
              <div
                v-show="armyUnit.check == 2"
                class="input-warning"
              >
                부대를 선택하세요.
              </div>
            </div>

            <select v-model="armyUnit.data">
              <option
                value=""
                disabled
                selected
              >
                부대을 선택하세요.
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

            <div class="input-label">
              <h3>계급</h3>
              <div
                v-show="uClass.check"
                class="input-warning"
              >
                계급을 선택하세요.
              </div>
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

            <div class="input-label">
              <h3>아이디</h3>
              <div
                v-show="uid.check != 2"
                class="input-comment"
              >
                아이디를 6자 이상 입력해주세요.
              </div>
              <div
                v-show="uid.check == 2"
                class="input-warning"
              >
                아이디를 6자 이상 입력해주세요.
              </div>
            </div>
            <input
              v-model="uid.data"
              :class="{
                success: uid.check == 1,
                error: uid.check == 2,
              }"
              placeholder="아이디"
              @change="checkID"
            >

            <div class="input-label">
              <h3>비밀번호</h3>
              <div
                v-show="password.check != 2"
                class="input-comment"
              >
                8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요.
              </div>
              <div
                v-show="password.check == 2"
                class="input-warning"
              >
                8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요.
              </div>
            </div>
            <input
              v-model="password.data"
              type="password"
              placeholder="비밀번호"
              style="margin-bottom: 20px; background-image: none"
              :class="{
                success: password.check == 1,
                error: password.check == 2,
              }"
              @change="checkPassword"
            >
            <div class="input-label">
              <h3>비밀번호 확인</h3>
              <!-- <div v-show="passwordConfirm.check != 2" class="input-comment">
                8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요.
              </div> -->
              <div
                v-show="passwordConfirm.check == 2"
                class="input-warning"
              >
                비밀번호가 일치하지 않습니다.
              </div>
            </div>
            <input
              v-model="passwordConfirm.data"
              type="password"
              placeholder="비밀번호 확인"
              :class="{
                success: passwordConfirm.check == 1,
                error: passwordConfirm.check == 2,
              }"
              style="background-image: none"
              @change="checkPasswordCofirm"
            >
            <button type="submit">
              확인
            </button>
          </form>
          <h1 id="console">
            {{ text }}
          </h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";

class inputData {
  constructor() {
    this.data = "";
    this.check = 0;
  }
}

export default {
  data() {
    return {
      text: "",
      name: new inputData(),
      dogTag: new inputData(),
      division: new inputData(),
      armyUnit: new inputData(),
      uClass: new inputData(),
      uid: new inputData(),
      password: new inputData(),
      passwordConfirm: new inputData(),
    };
  },
  methods: {
    submitForm() {
      if (
        this.name.check == 1 &&
        this.dogTag.check == 1 &&
        this.uid.check == 1 &&
        this.division.data != "" &&
        this.armyUnit.data != "" &&
        this.uClass.data != "" &&
        this.password.check == 1 &&
        this.passwordConfirm.check == 1
      ) {
        this.$axios
          .post("/user/create/", {
            name: this.name.data,
            uid: this.uid.data,
            password: this.password.data,
            dog_num: this.dogTag.data,
            army: this.division.data,
            unit: this.armyUnit.data,
            rank: this.uClass.data,
          })
          .then((response) => {
            console.log(response);
            this.text = response;
          })
          .catch((error) => {
            console.log(error);
            this.text = error;
          });
        // .finally(function () {
        //   this.text = "adsffdsaadsf";
        // });
        this.text += "um";
      } else {
        this.text = "fail";
      }
    },
    checkName(event) {
      if (event.target.value != "") {
        this.name.check = 1;
      } else {
        this.name.check = 2;
      }
    },
    checkDogTag(event) {
      if (event.target.value != "") {
        this.dogTag.check = 1;
      } else {
        this.dogTag.check = 2;
      }
    },
    checkID(event) {
      if (event.target.value.length >= 6) {
        this.uid.check = 1;
      } else {
        this.uid.check = 2;
      }
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
  },
};
</script>

<style scoped>
@keyframes up {
  from {
    transform: rotate(10deg);
    /* transform: translateY(100px); */
    /* opacity: 0; */
  }
  to {
    transform: rotate(-10deg);
    /* transform: translateY(0); */
    /* opacity: 1; */
  }
}
.left {
  background: linear-gradient(180deg, #f4f5fa 0%, rgba(244, 245, 250, 0) 100%);
  width: 50%;
  position: relative;
  overflow: hidden;
}
.right {
  width: 50%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: #fff;
  /* overflow: scroll; */
}
.left .back {
  position: absolute;
  bottom: -110px;
  right: -200px;
}

.left .hand {
  position: absolute;
  bottom: -15px;
  right: 80px;
  animation: up 3s infinite alternate;
  z-index: 1;
}

.left .front {
  position: absolute;
  bottom: 0px;
  right: 30px;
  z-index: 2;
}

.wrap-title {
  position: absolute;
  top: 20%;
  left: 15%;
}
.wrap-title h2 {
  text-align: left;
  color: #9c9db2;
  margin-bottom: 16px;
  font-size: 34px;
}
.wrap-title .title {
  display: flex;
  color: #9155eb;
  align-items: center;
}
.wrap-title .title img {
  margin-right: 10px;
}
.wrap-title .title h1 {
  margin: 0px;
  font-size: 48px;
}

.right h2 {
  color: #585767;
  font-size: 34px;
  margin-bottom: 44;
}
.right .title {
  display: none;
  flex-direction: column;
  align-items: center;
  margin-bottom: 30px;
}
.right .title h1 {
  margin: 0px;
  margin-top: 10px;
  font-size: 35px;
  color: #9155eb;
}
.right-wrap {
  width: 428px;
}
.right-wrap a {
  font-weight: bold;
  text-decoration: none;
  color: #616276;
}
.right-wrap a:hover {
  color: #9155eb;
}
.right input {
  box-sizing: border-box;

  /* Auto layout */
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 16px 12px;
  width: 100%;
  height: 56px;

  background: #ffffff;
  /* Dark8 */
  border: 2px solid #d9d8e8;
  border-radius: 8px;
  /* padding-left: 40px; */
  margin-bottom: 40px;

  font-size: 20px;
  background: url("@/assets/icons/check.svg") no-repeat scroll 10px center;
  background-position: right 12px center;
}

.right select {
  box-sizing: border-box;

  padding: 16px 12px;
  width: 100%;
  height: 56px;

  background: #ffffff;
  /* Dark8 */
  border: 2px solid #d9d8e8;
  border-radius: 8px;
  margin-bottom: 40px;
  font-size: 20px;
  color: black;
}
.right select option {
  /* background: lightcoral; */
  /* color: #fff; */
  width: 100%;
  padding: 16px 12px;
  /* font-size: 16px; */
}

.right select option:hover {
  background-color: #9155eb;
  color: white;
}
.right input::-webkit-input-placeholder {
  color: #abacc0;
  font-size: 20px;
}
.right .input-label {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-bottom: 12px;
}
.right .input-label h3 {
  margin: 0px;
  font-size: 20px;
}
.right .input-warning {
  font-size: 12px;
  color: #ff5467;
}
.right .input-comment {
  font-size: 12px;
  color: #616276;
}
.right .success {
  border: 2px solid #3fc6b8;
  background: url("@/assets/icons/check-success.svg") no-repeat scroll 10px
    center;
  background-position: right 12px center;
}
.right .error {
  border: 2px solid #ff5467;
  background: url("@/assets/icons/error.svg") no-repeat scroll 10px center;
  background-position: right 12px center;
}
.right button {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 16px 0px;

  width: 100%;
  height: 55px;

  /* Primary */
  background: #9155eb;
  box-shadow: 0px 0px 10px rgba(145, 85, 235, 0.5);
  border-radius: 8px;
  border: none;
  margin-bottom: 16px;

  color: white;
  font-size: 20px;
  font-weight: bold;
}
.right .flow-wrap {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow: scroll;
  padding: 50px 0px 100px 0px;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}
.right .flow-wrap::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Opera*/
}
@media (max-width: 1200px) {
  .left {
    display: none;
  }
  .right {
    width: 100%;
  }
  .right h2 {
    display: none;
  }
  .right .title {
    display: flex;
  }
  .right-wrap {
    width: 85%;
  }
}
</style>
