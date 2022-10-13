<template>
  <div class="page">
    <div class="search-div">
      <SearchInput :on-click="search" />
    </div>
    <table>
      <thead>
        <tr>
          <th w>
            부대이름
          </th>
          <th>변경</th>
          <th>삭제</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>계룡대 본부대대</td>
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
    justify-content:flex-end;
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
</style>