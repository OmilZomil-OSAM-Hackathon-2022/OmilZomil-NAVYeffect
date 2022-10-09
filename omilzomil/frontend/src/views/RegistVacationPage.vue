<template>
  <div class="wrap">
    <div class="search-card card">
      <div class="card-head">
        <a @click="$emit('backToPage')">
          <img
            src="@/assets/icons/left-arrow.svg"
            width="9"
            class="image-center"
          >
        </a>
        휴가신청
      </div>
      <div class="search-content">
        <div class="user-info">
          <div>{{ user.division }}</div>
          <div>{{ user.unit }}</div>
          <div>{{ user.uClass }}</div>
          <div>{{ user.uName }}</div>
          <div>{{ user.dogTag }}</div>
        </div>
        <div class="term">
          <div class="datepicker-wrap">
            시작일
            <Datepicker
              v-model="startDate"
              :format="format"
              input-class-name="datepicker-input"
              placeholder="시작일을 선택하세요."
              select-text="확인"
              :dark="getDarkMode"
            />
          </div>
          <div class="datepicker-wrap">
            복귀일
            <Datepicker
              v-model="endDate"
              :format="format"
              input-class-name="datepicker-input"
              placeholder="복귀일을 선택하세요."
              select-text="확인"
              :dark="getDarkMode"
            />
          </div>
          <a class="regist">신청</a>
        </div>
      </div>
    </div>
    <div class="list-card card">
      <div class="search">
        <SearchInput @on-click="search" />
      </div>
      <table>
        <thead>
          <tr> 
            <th>순번</th>
            <th>기간</th>
            <th>상태</th>
            <th>취소 관리</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(vacation,index) in vacationList"
            :key="index"
          >
            <td>{{ index+1 }}</td>
            <td>{{ vacation.term }}</td>
            <td>{{ vacation.state }}</td>
            <td><button>취소</button></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
  
<script>
import SearchInput from '../components/common/SearchInput.vue';
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import {ref} from 'vue';
  class Vacation{
      constructor(){
          this.term = "2022.09.29 ~ 2022.10.09";
          this.state = "완료";
      }
  }
  export default { 
      components:{ SearchInput, Datepicker },
    props:{
        user:{
            type:Object,
            default:null,
        }
    },
      emits:['backToPage'],
      setup(){
      const startDate = ref();
      const endDate = ref();
      const format = (date) => {
        return `${date.getFullYear()}/${date.getMonth()}/${date.getDate()}`;
      }
      return {
        startDate,
        endDate,
        format,
      }
    },
      data(){
          return{
              vacationList:[
                  new Vacation(),
                  new Vacation(),
                  new Vacation(),
                  new Vacation(),
                  new Vacation(),
                  new Vacation(),
                  new Vacation(),
                  new Vacation(),
              ],
          }
      },
      computed:{
      getDarkMode() {
        return this.$store.getters.getDarkMode;
      },
    },
      methods:{
          search(text){
              console.log(text);
          },
      }
  }
  </script>
  
  <style scoped>

  .image-center{
  display: block;
  margin-top: auto;
  margin-bottom: auto;
  /* width: 50%; */
  }
  .wrap{
      display:flex;
      flex-direction: column;
      margin-bottom:40px;
      flex-grow: 1;
      gap:25px;
  }

  .search-card{
    height:130px;
    flex-direction: column;
    justify-content: flex-start;
  }
  .search-content{
    box-sizing:border-box;
    width: 100%;
    height:100%;
    padding:0px 54px;
    display:flex;
    align-items: center;
    justify-content:space-between;
  }

  .datepicker-wrap{
    display:flex;
    align-items:center;
    gap:16px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 16px;
    letter-spacing: 0.25px;
    margin-right:24px;
  }
  .user-info{
    display:flex;
    align-items:center;
    gap:24px;
  }
  .term{
    display:flex;
    align-items:center;
  }

  .regist{
    box-sizing:border-box;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 7px 8px;
    gap: 10px;

    width: 39px;
    height: 28px;

    background: rgba(145, 85, 235, 0.2);
    border-radius: 4px;

    text-decoration: none;

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
  .list-card{
    height:653px;
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
      height:100%;
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
  table button{
      width: 44px;
      /* height: 20px; */
      padding:3px;
      background: #78798D;
      border-radius: 8px;
      border:none;
      color:white;
  }

  .card-head{
    box-sizing:border-box;
    width:100%;
    display:flex;
    /* justify-content: space-between; */
    gap:9px;
    align-items: center;
    padding:14px 21px;
    background: var(--color-state-card);
    border-radius: 20px 20px 0px 0px;
    /* Subtitle 1 - Bold */

    font-family: 'Roboto';
    font-style: normal;
    font-weight: 700;
    font-size: 16px;
    line-height: 19px;
    /* identical to box height */

    letter-spacing: 0.15px;
}
  </style>


<style>
/* datepicker style */
.datepicker-input{
    width: 224px;
    box-sizing: border-box;
    height:28px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 14px;
    /* identical to box height */
  
    letter-spacing: 0.4px;
  }
  
  .datepicker-input::placeholder{
    color: #ABACC0;
  }
  
  .dp__button, .dp__cancel, .dp__selection_preview{
    display:none;
  }
  .dp__action_buttons{
    width:100%;
    display:flex;
    justify-content: flex-end;
  }
  .dp__select{
    background: rgba(145, 85, 235, 0.2);
    color: #9155EB;
  
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 500;
    font-size: 12px;
    line-height: 14px;
    padding: 8px 16px;
  }
  .dp__theme_dark .dp__select{
    background: #9155EB;
    color: #ffffff;
  }
  /* .dp__range_start, .dp__range_end{
    background: #9155EB;
  } */
  /* .dp__overlay_cell_active{
    background: #9155EB;
  } */
  .dp__calendar_header_item{
    font-weight: normal;
  }
  .dp__theme_light {
      --dp-text-color: #888888;
      --dp-primary-color: #9155EB;
      --dp-success-color: #9155EB;
  }
  .dp__theme_dark {
      --dp-background-color: #312D4B;
      --dp-text-color: #fff;
      --dp-primary-color: #9155EB;
      --dp-border-color: #78798D;
      --dp-menu-border-color: #78798D;
      --dp-success-color: #00701a;
  }
  .dp__menu{
    margin-top: 5px;
  }
  </style>