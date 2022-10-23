<template>
  <div class="pagenation-section">
    <div class="pagination">
      <div class="select-wrap">
        <select v-model="page">
          <option
            v-for="i in numbers"
            :key="i"
            :value="i"
          >
            {{ i }}
          </option>
        </select>
        /{{ total }}
      </div>
      <img
        src="@/assets/icons/left-arrow.svg"
        width="6"
        style="margin-right:18px"
        @click="(page > 1) ?page = page - 1:page"
      >
      <img
        src="@/assets/icons/right-arrow.svg"
        width="6"
        @click="(page < total) ?page = page + 1:page"
      >
    </div>
  </div>
</template>

<script>
export default {
    props:{
        total:{
            type:Number,
            default:1
        }
    },
    emits:['page'],
    data(){
        return{
            page:1,
        }
    },  
    computed:{
        numbers(){
            return Array.from(Array(this.total),(_,index)=>index+1);
        }
    },
    watch:{
        page(){
            this.$emit("page",this.page);
        }
    },

}
</script>

<style scoped>
img{
    cursor:pointer;
}
select{
    padding: 0px 11px;
    height:23px;
    font-weight: 400;
    font-size: 14px;
    line-height: 15px;
    /* background: rgba(94, 99, 102);
    border-radius: 8px;
    border:none; */
}
.select-wrap{
    display:flex;
    align-items:center;
    gap:8px;
    font-weight: 400;
    font-size: 14px;
    line-height: 17px;
    margin-right:24px;
}
.pagination{
    display:flex;
    align-items:center;
}
.pagenation-section{
    width:100%;
    display:flex;
    justify-content: flex-end;
    padding:9px 0px;
}
</style>