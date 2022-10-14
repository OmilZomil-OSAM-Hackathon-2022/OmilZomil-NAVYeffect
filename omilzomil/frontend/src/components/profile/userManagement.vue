<template>
  <div class="page">
    <div class="search-div">
      <SearchInput :on-click="search" />
    </div>
    <div class="filter-wrap">
      <select v-model="classFilter">
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
      <select v-model="divisionFilter">
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
      <select v-model="unitFilter">
        <option
          value=""
          disabled
          selected
        >
          부대를 선택하세요.
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
      <select v-model="unitFilter">
        <option
          value=""
          disabled
          selected
        >
          승인 여부를 선택하세요.
        </option>

        <option value="계룡대 근무지원단">
          미승인
        </option>
        <option value="1함대">
          승인
        </option>
      </select>
      <button class="filterbtn">
        필터 적용
      </button>
    </div>
    <table>
      <thead>
        <tr>
          <th>이름</th>
          <th>소속</th>
          <th>부대</th>
          <th>계급</th>
          <th>군번</th>
          <th>권한 관리</th>
          <th>가입 승인</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>김민섭</td>
          <td>해군</td>
          <td>계룡대 근무지원단</td>
          <td>일병</td>
          <td>22-71005164</td>
          <td>
            <select>
              <option>미승인 사용자</option>
              <option>일반 사용자</option>
              <option>관리자</option>
              <option>루트 관리자</option>
            </select>
          </td>
          <td>
            <div style="display:flex; justify-content:center">
              <CheckTag :is-check="true" />
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import SearchInput from '../common/SearchInput.vue';
import CheckTag from '../CheckTag.vue';
export default {
    components: { SearchInput, CheckTag },
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

.filter-wrap{
  display:flex;
  justify-content:flex-end;
  gap:29px;
  margin-bottom:20px;
}

select {
  box-sizing: border-box;

  padding: 6px 12px;
  width: 224px;
  height: 28px;

  background: #ffffff;
  /* Dark8 */
  border: 1px solid #d9d8e8;
  border-radius: 4px;
  font-weight: 400;
  font-size: 12px;
  line-height: 14px;
  /* identical to box height */

  letter-spacing: 0.4px;
  -webkit-appearance: none;

  background: url("@/assets/icons/mdi_chevron-down.svg") no-repeat scroll 10px center;
  background-position: right 6px center;
  background-size:15px;
  color:var(--color)
}

.filterbtn{
  color:#9155EB;
  font-weight: 500;
  font-size: 12px;
  line-height: 14px;
  /* identical to box height */

  letter-spacing: 0.4px; 
  width: 65px;
  height: 28px;
  background: rgba(145, 85, 235, 0.2);
  border-radius: 4px;

  display:flex;
  justify-content: center;
  align-items: center;
  border:none;
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

</style>