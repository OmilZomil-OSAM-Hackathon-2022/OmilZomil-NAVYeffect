<template>
  <div
    class="overlay"
    @click.self="$emit('close')"
  >
    <div class="card">
      <div class="title">
        {{ title }} 이름 변경하기
        <img
          src="@/assets/icons/close-thick.svg"
          width="24"
          height="24"
          style="cursor:pointer"
          @click="$emit('close')"
        >
      </div>
      <div class="content">
        수정할 {{ title }} 이름을 입력해주세요.
      </div>
      <form
        class="data"
        @submit.prevent="$emit('submit',text)"
      >
        <div class="more">
          {{ title }} 이름
        </div>
        <input
          v-model="text"
          :placeholder="data"
        >
        <div class="btn-wrap">
          <button>
            저장
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
    props:{
        title:{
            type:String,
            default:''
        },
        data:{
            type:String,
            default:''
        }
    },
    emits:["submit","close"],
    data(){
      return{
        text:'',
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
.card{
    width:588px;
    height:306px;
    padding:17px;
    box-sizing:border-box;
    display: flex;
    flex-direction: column;
    align-items:center;
    justify-content: space-between;
}
.title{
    width:100%;
    display:flex;
    justify-content: space-between;
}
.content{
    width: 427px;
    height: 56px;

    background: var(--color-state-card);
    border-radius: 20px;
    font-weight: 400;
    font-size: 16px;
    line-height: 19px;

    letter-spacing: 0.5px;
    display:flex;
    justify-content:center;
    align-items:center;
}

.btn-wrap{
    width:100%;
    display:flex;
    justify-content: flex-end;
}

button{
    color:white;
    border:none;

    display:flex;
    justify-content: center;
    align-items:center;
    width: 52px;
    height: 32px;

    /* Primary */

    background: #9155EB;
    border-radius: 8px;
    font-weight: 500;
    font-size: 14px;
    line-height: 16px;
    letter-spacing: 1.25px;
}
input{
    box-sizing: border-box;

    /* Auto layout */

    padding: 16.5px 12px;

    width: 520px;
    height: 56px;

    background: var(--color-input);
    /* Dark8 */

    border: 2px solid var(--color-input-border);
    border-radius: 8px;
    margin-top:12px;
    margin-bottom:20px;
    font-weight: 500;
    font-size: 20px;
    line-height: 23px;
    letter-spacing: 0.15px;
}

.more{
  display:flex;
  width:100%;
  justify-content:flex-start;  
  font-weight: 400;
    font-size: 14px;
    line-height: 16px;
    letter-spacing: 0.25px;

    /* Dark4 */

    color: #78798D;
}
</style>