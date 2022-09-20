<template >
  <div style="display: flex; width: 100%; height: 100vh">
    <div class="left">
      <img class="back" src="@/assets/images/loginBackground.svg" />
      <img class="hand" src="@/assets/images/hand.svg" />
      <img class="front" src="@/assets/images/topBackground.svg" />
      <div class="wrap-title">
        <h2>오밀조밀<br />복장과 두발을 검사하다</h2>
        <div class="title">
          <img width="52px" src="@/assets/logo.svg" />
          <h1>OMIL-ZOMIL</h1>
        </div>
      </div>
    </div>
    <div class="right">
      <div class="flow-wrap">
        <h2>회원가입</h2>
        <div class="title">
          <img width="52px" src="@/assets/logo.svg" />
          <h1>OMIL-ZOMIL</h1>
        </div>
        <div class="right-wrap">
          <form>
            <div class="input-label">
              <h3>이름</h3>
              <div v-show="checkName == 2" class="input-warning">
                이름을 입력해주세요.
              </div>
            </div>
            <input
              placeholder="성명"
              v-bind:class="{ success: checkName == 1, error: checkName == 2 }"
            />

            <div class="input-label">
              <h3>군번</h3>
              <div v-show="checkDogTag == 2" class="input-warning">
                군번을 입력해주세요.
              </div>
            </div>
            <input
              placeholder="군번"
              v-bind:class="{
                success: checkDogTag == 1,
                error: checkDogTag == 2,
              }"
            />

            <div class="input-label">
              <h3>소속</h3>
              <div v-show="checkDivision == 2" class="input-warning">
                소속을 입력해주세요.
              </div>
            </div>
            <input
              placeholder="소속"
              v-bind:class="{
                success: checkDivision == 1,
                error: checkDivision == 2,
              }"
            />

            <div class="input-label">
              <h3>부대</h3>
              <div v-show="checkArmyUnit == 2" class="input-warning">
                부대를 입력해주세요.
              </div>
            </div>
            <input
              placeholder="부대"
              v-bind:class="{
                success: checkArmyUnit == 1,
                error: checkArmyUnit == 2,
              }"
            />

            <div class="input-label">
              <h3>계급</h3>
              <div v-show="checkClass" class="input-warning">
                계급을 입력해주세요.
              </div>
            </div>
            <input
              placeholder="계급"
              v-bind:class="{
                success: checkClass == 1,
                error: checkClass == 2,
              }"
            />

            <div class="input-label">
              <h3>아이디</h3>
              <div class="input-comment" v-show="checkID != 2">
                아이디를 6자 이상 입력해주세요.
              </div>
              <div class="input-warning" v-show="checkID == 2">
                아이디를 6자 이상 입력해주세요.
              </div>
            </div>
            <input placeholder="아이디" />

            <div class="input-label">
              <h3>비밀번호</h3>
              <div
                v-show="checkPassword != 2 && checkPasswordConfirm != 2"
                class="input-comment"
              >
                8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요.
              </div>
              <div
                v-show="checkPassword == 2 || checkPassword == 2"
                class="input-warning"
              >
                8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요.
              </div>
            </div>
            <input
              type="password"
              placeholder="비밀번호"
              style="margin-bottom: 12px"
              v-bind:class="{
                success: checkPassword == 1,
                error: checkPassword == 2,
              }"
            />
            <input
              type="password"
              placeholder="비밀번호 확인"
              v-bind:class="{
                success: checkPasswordConfirm == 1,
                error: checkPasswordConfirm == 2,
              }"
            />
            <button type="sumit">확인</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      checkName: 0,
      checkDogTag: 0,
      checkDivision: 0,
      checkArmyUnit: 0,
      checkClass: 0,
      checkID: 0,
      checkPassword: 0,
      checkPasswordConfirm: 0,
    };
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