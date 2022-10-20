<template>
  <div
    v-show="!showRegister"
    class="wrap"
  >
    <div class="card">
      <div class="search">
        <SearchInput @on-click="search" />
      </div>
      <table>
        <thead>
          <tr> 
            <th>이름</th>
            <th>소속</th>
            <th>부대</th>
            <th>계급</th>
            <th>군번</th>
            <th>휴가 관리</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(user,index) in userList"
            :key="index"
          >
            <td>{{ user.uName }}</td>
            <td>{{ user.division }}</td>
            <td>{{ user.unit }}</td>
            <td>{{ user.uClass }}</td>
            <td>{{ user.dogTag }}</td>
            <td>
              <a @click="showRegisterPage(user)">
                관리
              </a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <RegistVacationPage
      v-show="showRegister"
      :user="currentUser"
      @back-to-page="backToPage"
    />
  </div>
</template>

<script>
import SearchInput from '../components/common/SearchInput.vue';
import RegistVacationPage from './RegistVacationPage.vue';
class User{
    constructor(){
        this.uName = "김민섭";
        this.division = "해군";
        this.unit = "계룡대근무지원단";
        this.uClass = "일병";
        this.dogTag = "22-71005164";
    }
}
export default {
    components:{ SearchInput, RegistVacationPage },
    data(){
        return{
            userList:[
                new User(),
                new User(),
                new User(),
                new User(),
                new User(),
                new User(),
                new User(),
                new User(),
            ],
            currentUser:new User(),
            showRegister:false,
        }
    },
    methods:{
        search(text){
            console.log(text);
        },
        showRegisterPage(u){
            this.currentUser = u;
            this.showRegister = true;
        },
        backToPage(){
            this.showRegister =false;
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
    flex-grow:1;
    flex-direction: column;
    justify-content: flex-start;
    box-sizing: border-box;
    padding: 28px 61px;
    /* align-items: flex-start; */
}
.search{
    display:flex;
    width:100%;
    justify-content: flex-end;
    margin-bottom:8px;
}
.search button{
    width:28px;
    height:28px;
    background: rgba(145, 85, 235, 0.2);
    border-radius: 4px;
    border:none;
    margin-right: 4px;
}
table{
    width:100%;
    border-collapse: collapse; 
    border-bottom: 1px solid #E1E2E9;
  /* border-spacing: 0 5px; */
}

th, td{
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 16px;
    text-align: center;
    letter-spacing: 0.25px;
}
table thead tr{
    border-bottom: 1px solid #E1E2E9;
    height:52px;
}
table tbody tr{
    height:54px;
}
/* .table > :not(:first-child) {
    border-top: 2px solid "#E1E2E9";
} */
table a{
    padding: 2px 8px;
    gap: 10px;

    width: 44px;
    height: 20px;


    background: #78798D;
    border-radius: 8px;
    text-decoration:none;
    color:white;
}

</style>