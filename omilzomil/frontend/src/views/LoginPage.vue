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
            width="65px"
            src="@/assets/logo.svg"
          >
          <h1>OMIL-ZOMIL</h1>
        </div>
      </div>
    </div>
    <div class="right">
      <h2>로그인</h2>
      <div class="title">
        <img
          width="52px"
          src="@/assets/logo.svg"
        >
        <h1>OMIL-ZOMIL</h1>
      </div>
      <div class="right-wrap">
        <form @submit.prevent="buttonClick">
          <input
            v-model="username"
            class="user"
            placeholder="아이디"
          >
          <input
            v-model="password"
            class="password"
            type="password"
            placeholder="비밀번호"
            :style="{ 'margin-bottom': (loginFail? '0px':'60px')}"
          >
          <div
            v-show="loginFail"
            class="input-warning"
          >
            아이디(로그인 전용 아이디) 또는 비밀번호를 잘못 입력했습니다.<br>
            입력하신 내용을 다시 확인해주세요.
          </div>
          <button type="sumit">
            로그인
          </button>
        </form>
        <div style="display: flex; gap: 20px">
          <router-link to="/register">
            회원가입
          </router-link>
          <a>아이디 찾기</a>
          <a>비밀번호 찾기</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import qs from 'qs';
export default {
  data(){
    return{
      loginFail:false,
      username:'',
      password:'',
    }
  },
  methods:{
    buttonClick(){
      this.$axios.post('/login/access-token/',qs.stringify({
        username:this.username,
        password:this.password,
      })).then((response) => {
            if(response.data.success){
              this.$store.commit('login',{accessToken:response.data.access_token});
              this.$axios.post('/login/test-token/').then(async (response)=>{
                console.log(response.data);
                try{
                  if(response.data.success){
                    const ranks = (await this.$axios.get('/rank/')).data;
                    const unit = (await this.$axios.get(`/unit/${response.data.military_unit}`)).data.unit;
                    const affiliations = (await this.$axios.get('/affiliation/')).data;
                    response.data.unit_title = unit;
                    for(var key in ranks){
                      if(ranks[key].rank_id == response.data.rank)
                        response.data.rank_title = ranks[key].rank;
                    }
                    for(var key1 in affiliations){
                      if(affiliations[key1].affiliation_id == response.data.affiliation)
                        response.data.affiliation_title = affiliations[key1].affiliation;
                    }
                  }
                }catch(err){
                  console.log(err);
                  this.loginFail = true;
                }
                if(response.data.success){
                  this.$store.commit('setUser',response.data);
                  this.$router.push('/');
                }else{
                  alert("승인되지 않은 사용자입니다.");
                  // this.loginFail = true;
                }
              });
            }else{
              this.loginFail = true;
            }
          })
          .catch(() => {
            this.loginFail = true;
          });
    }
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
  /* margin-right: 10px; */
}
.wrap-title .title h1 {
  margin: 0px;
  font-size: 48px;
}

.right h2 {
  color: #585767;
  font-size: 34px;
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
  padding-left: 40px;

  font-size: 15px;
}
.right input::-webkit-input-placeholder {
  color: #abacc0;
  font-size: 15px;
}
.right .user {
  margin-bottom: 16px;
  background: url("@/assets/icons/account-outline.svg") no-repeat scroll 10px
    center;
}
.right .password {
  /* margin-bottom: 40px; */
  background: url("@/assets/icons/lock-outline.svg") no-repeat scroll 10px
    center;
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
.right .input-warning {
  font-size: 12px;
  color: #ff5467;
  text-align: left;
  height:60px;
  display:flex;
  align-items: center;
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