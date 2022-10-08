<template>
  <div class="card">
    <table>
      <thead>
        <tr>
          <th>사진</th>
          <th>소속 / 계급 / 이름</th>
          <th>시간</th>
          <th>복장</th>
          <th>두발상태</th>
          <th>복장상태</th>
          <th>자세히보기</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>tser</td>
          <td>tser</td>
          <td>tser</td>
          <td>tser</td>
          <td>tser</td>
          <td>tser</td>
          <td>tser</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
    data(){
        return {

        }
    }
}
</script>

<style scoped>
.card{
    box-sizing: border-box;
    padding: 28px 61px;
    /* height:100%; */

    height: 500px;
    align-items: flex-start;
}
table{
    width:100%;
    border-collapse:separate; 
    /* border-collapse: collapse;  */
}

table th{
    font-family: 'Inter';
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 17px;
    color: #585767;
    margin-bottom: 8px;
	border-bottom: 1px solid #E1E2E9;
	/* padding-bottom: 0; */
    padding: 18px 0px;
}

/* table thead{
    height:52px;
    border-bottom:#E1E2E9 solid 1px;
    margin-bottom: 8px;
} */
</style>