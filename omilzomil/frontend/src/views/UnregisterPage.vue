<template>
  <div class="wrap">
    <div class="card">
      <div class="unregist">
        회원 탈퇴
      </div>
      <img
        class="face"
        src="@/assets/images/crying-face.svg"
      >
      <div class="oz">
        OMIL-ZOMIL
      </div>
      <div class="msg1">
        탈퇴 전 확인하세요.
      </div>
      <div class="msg2">
        프로필, 이미지 등 저장된 모든 데이터들은 사라집니다.
      </div>
      <div class="pw1">
        <div class="pw1-box1">
          <div class="pw1-box1-msg1">
            비밀번호
          </div>
          <div class="pw1-box1-msg2">
            8~16자 영문 대 소문자, 숫자, 특수문자를 사용하세요.
          </div>
        </div>
        <div class="box2">
          <div class="inputbox">
            <input
              v-model="pw1"
              name="pw1input"
              :type="pw1show ? 'text' : 'password'"
              placeholder="비밀번호"
            >
            <button
              v-if="pw1show===true"
              class="eye-off"
              @click="pw1show=false"
            />
            <button
              v-else
              class="eye-on"
              @click="pw1show=true"
            />
          </div>
        </div>
      </div>
      <div class="pw2">
        <div class="pw2-box1">
          비밀번호 확인
        </div>
        <div class="box2">
          <div class="inputbox">
            <input
              v-model="pw2"
              name="pw2input"
              :type="pw2show ? 'text' : 'password'"
              placeholder="비밀번호"
            >
            <button
              v-if="pw2show===true"
              class="eye-off"
              @click="pw2show=false"
            />
            <button
              v-else
              class="eye-on"
              @click="pw2show=true"
            />
          </div>
        </div>
      </div>
      <button
        class="button"
        @click="unregist"
      >
        <div class="button-msg">
          탈퇴하기
        </div>
      </button>
    </div>
  </div>
</template>
  
<script>
  export default {
    data(){
      return{
        pw1:"",
        pw2:"",
        pw1show:false,
        pw2show:false,
      }
    },
    methods:{
      unregist(){
        //탈퇴~
      }
    }
  }
</script>
  
<style scoped>
  .wrap{
    display:flex;
    flex-direction: column;
    margin-bottom:40px;
    flex-grow: 1;
  }
  .card{
    height: 812px;
    flex-grow:1;
    flex-direction: column;
    justify-content: flex-start;
    box-sizing: border-box;
    /* padding: 28px 61px; */
  }
  .unregist{
    position:relative;
    /* top:21px; */
    width: 79px;
    height: 60px;
    font-weight: 700;
    font-size: 16px;
    line-height: 19px;
    letter-spacing: 0.15px;

    display:flex;
    align-items:center;
    justify-content:center;
    color: #9155EB;
    border-bottom: solid #9155EB 4px;
    box-sizing:border-box;
  }
  .face{
    position:relative;
    top: 85px;
    width:38px;
    height:38px;
  }
  .oz{
    position:relative;
    top: 89px;
    width: 119px;
    height: 23px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 900;
    font-size: 20px;
    line-height: 23px;
    letter-spacing: 0.15px;
    color: #9155EB;
  }
  .msg1{
    position:relative;
    top:99px;
    width: 165px;
    height: 23px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 700;
    font-size: 20px;
    line-height: 23px;
    letter-spacing: 0.15px;

  }
  /* .box{
    position:relative;
    top: 130px;
    width: 427px;
    height: 56px;
  } */
  .msg2{
    position:relative;
    display:flex;
    justify-content: center;
    align-items: center;
    top:111px;
    width: 394px;
    height: 56px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 16px;
    line-height: 19px;
    letter-spacing: 0.5px;
    color: #616276;
    background-color:var(--color-state-card);
    border-radius: 20px;
  }
  .pw1{
    position:relative;
    top: 179px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 0px;
    gap: 16px;
    width: 428px;
    height: 75px;
  }
  .pw1-box1{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: flex-end;
    padding: 0px;
    justify-content: space-between;
    width: 428px;
    height: 19px;
  }
  .pw1-box1-msg1{
    width: 60px;
    height: 19px;
    text-align: left;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 700;
    font-size: 16px;
    line-height: 19px;
    letter-spacing: 0.15px;
  }
  .pw1-box1-msg2{
    width: 277px;
    height: 14px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 14px;
    text-align: right;
    letter-spacing: 0.4px;
  }
  .box2{
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 12px;
    gap: 2px;
    width: 428px;
    height: 40px;
    background: #FFFFFF;
    border: 2px solid #D9D8E8;
    border-radius: 8px;

    background:var(--color-input)
  }
  .inputbox{
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 0px;
    justify-content: space-between;
    height: 16px;
  }
  input{
    width: 372px;
    height: 14px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 14px;
    letter-spacing: 0.4px;
    color: #ABACC0;
    outline: none;
    border: 0;
    background:var(--color-input)
  }
  .eye-on{
    width: 16px;
    height: 16px;
    background: url("@/assets/icons/eye-on.svg") no-repeat;
    border:none;
    cursor:pointer;
  }
  .eye-off{
    width: 16px;
    height: 16px;
    background: url("@/assets/icons/eye-off.svg") no-repeat;
    border:none;
    cursor:pointer;
  }
  .pw2{
    position:relative;
    top: 211px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 0px;
    gap: 16px;
    width: 428px;
    height: 75px;
  }
  .pw2-box1{
    width: 428px;
    height: 19px;
    text-align: left;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 700;
    font-size: 16px;
    line-height: 19px;
    letter-spacing: 0.15px;
  }
  .button{
    border:none;
    cursor:pointer;
    position:relative;
    top: 260px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 428px;
    height: 55px;
    background: #78798D;
    border-radius: 8px;
  }
  .button:hover {
    top:258px;
    height:59px;
    width:432px;
    background:#9155EB;
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
  }
  .button-msg{
    width: 75px;
    height: 23px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 600;
    font-size: 20px;
    line-height: 23px;
    letter-spacing: 0.15px;
    color: #FFFFFF;
  }
  @media (max-width: 1200px) {
    .msg2{
      width:270px;
      height:40px;
      font-size:11px;
    }
    .pw1{
      width:300px;
    }
    .pw1-box1{
      width:300px;
    }
    .pw1-box1-msg1{
      width:55px;
      font-size:14px;
    }
    .pw1-box1-msg2{
      width:230px;
      font-size:10px;
    }
    .pw2{
      width:300px;
    }
    .pw2-box1{
      width:300px;
      font-size:14px;
    }
    .box2{
      width:300px;
    }
    input{
      width:250px;
    }
    .button{
      width:150px;
    }
    .button:hover {
      height:59px;
      width:170px;
      box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
    }
  }
</style>