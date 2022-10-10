<template>
  <div class="wrap">
    <div class="card filter">
      <form class="form1">
        <select>
          <option value="" disabled selected>부ㄹ량 요를 선택하세요.</option>
        </select>
        <select>

          <option value="" disabled selected>계급을 선택하세요.</option>
        </select>
        <input type="date" placeholder="기한을 선택하세요."/>
        <button>필터 적용</button>
      </form>
      <form class="form2">
        <button><img src="@/assets/icons/mdi_magnify.svg"/></button>
        <input/>
      </form>
    </div>
    <ListUp></ListUp>
  </div>
</template>

<script>
import ListUp from '@/components/ListUp.vue';
export default {
    components: { ListUp }
}
</script>

<style scoped>
.filter{
  height:76px;
  margin-bottom: 40px;
  gap:20px;
}
.form1{
  display: flex;
  gap:20px;
}
.form2{
  display: flex;
  gap:8px;
}
select{
  box-sizing: border-box;
  padding: 6px 0px 6px 12px;
  /* gap: 2px; */

  width: 224px;
  height: 28px;

  background: #FFFFFF;
  /* Dark8 */

  border: 1px solid #D9D8E8;
  border-radius: 4px;
}
input{
  box-sizing: border-box;
  padding: 6px 0px 6px 12px;
  /* gap: 2px; */

  width: 224px;
  height: 28px;

  background: #FFFFFF;
  /* Dark8 */

  border: 1px solid #D9D8E8;
  border-radius: 4px;
}
button{
  /* box-sizing: border-box; */
  padding: 0px 8px;
  height:28px;
  display: flex;
  align-items: center;
  background: rgba(145, 85, 235, 0.2);
  border-radius: 4px;
  border:none;
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 500;
  font-size: 12px;
  line-height: 14px;
  /* identical to box height */

  letter-spacing: 0.4px;

  /* Primary */

  color: #9155EB;

}
</style>