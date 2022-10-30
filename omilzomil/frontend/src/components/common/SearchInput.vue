<template>
  <form
    class="search-wrap"
    @submit.prevent="$emit('search',text)"
  >
    <button>
      <img
        width="16"
        src="@/assets/icons/mdi_magnify.svg"
      >
    </button>
    <input
      v-model="text"
      placeholder="검색"
    >
  </form>
</template>

<script>
export default {
    emits:["search"],
    data(){
        return{
            text:'',
        }
    },
}
</script>

<style scoped>
.search-wrap{
    display:flex;
    gap:4px;
}


input{
  box-sizing: border-box;

  /* Auto layout */

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 7px 10px;

  width: 224px;
  height: 28px;

  background: var(--color-input);

  border: 1px solid var(--color-input-border);
  border-radius: 4px;
}
input::placeholder{
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  color: #9C9DB2;
}
button{
  width:28px;
  height:28px;
  background: rgba(145, 85, 235, 0.2);
  border-radius: 4px;
  border:none;
  display:flex;
  align-items:center;
  justify-content: center;
  cursor: pointer;
}
</style>