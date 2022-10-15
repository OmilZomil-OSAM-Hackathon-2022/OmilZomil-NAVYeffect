<template>
  <div class="page">
    <div class="search-div">
      <div class="add-unit">
        <input placeholder="부대 이름을 입력하세요.">
        <button>추가</button>
      </div>
      <SearchInput :on-click="search" />
    </div>
    <table>
      <thead>
        <tr>
          <th w>
            부대이름
          </th>
          <th>위병소 관리</th>
          <th>변경</th>
          <th>삭제</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>계룡대 본부대대</td>
          <td>
            <div class="tcenter">
              <a>관리</a>
            </div>
          </td>
          <td>
            <div class="tcenter">
              <a>변경</a>
            </div>
          </td>
          <td>
            <div class="tcenter">
              <a>삭제</a>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import SearchInput from '../common/SearchInput.vue';
export default {
    components: { SearchInput },
    data(){
      return{
        classFilter:'',
        divisionFilter:'',
        unitFilter:''
      }
    },
    methods:{
        search(text){
            text;
        }
    }
}
</script>

<style scoped>
.page{
    padding:28px 61px;
    display:flex;
    flex-direction:column;
}
.search-div{
    width:100%;
    display:flex;
    justify-content:space-between;
    margin-bottom:20px;
    height:wrap;
}

table{
  width:100%;
  border-collapse: collapse; 
  border-bottom: 1px solid #E1E2E9;
}

table thead tr{
    border-bottom: 1px solid #E1E2E9;
    height:52px;
}
th{
  font-weight: 400;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 0.25px;
}
td select{
  width: 128px;
  height: 36px;
}
tbody td{
  font-weight: 400;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 0.25px;
  height:70px;
}

a{
  width: 44px;
  height: 20px;
  left: 975px;
  top: 0px;

  /* Dark4 */

  background: #78798D;
  border-radius: 8px;
  color:white;
  display:flex;
  align-items:center;
  justify-content: center;

  font-weight: 500;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 1.25px;
}

.tcenter{
  display:flex;
  justify-content: center;
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
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  color: #9C9DB2;
}

.add-unit{
  display:flex;
  gap:4px;
}

.add-unit button{
  /* width:28px; */
  height:28px;
  background: rgba(145, 85, 235, 0.2);
  border-radius: 4px;
  border:none;
  display:flex;
  align-items:center;
  justify-content: center;
  cursor: pointer;
  color:#9155EB;
  font-weight: 500;
  font-size: 12px;
  line-height: 14px;
  /* identical to box height */

  letter-spacing: 0.4px;
}
</style>