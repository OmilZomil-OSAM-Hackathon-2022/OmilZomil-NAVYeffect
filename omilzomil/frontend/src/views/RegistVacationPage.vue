<template>
  <div class="wrap">
    <div class="search-card card">
      <CardHead title="휴가신청" />
      <div class="search-content">
        <div class="user-info">
          <div>{{ getUser.affiliation_title }}</div>
          <div>{{ getUser.unit_title }}</div>
          <div>{{ getUser.rank_title }}</div>
          <div>{{ getUser.full_name }}</div>
          <div>{{ getUser.dog_number }}</div>
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
          <a
            class="regist"
            @click="submit"
          >신청</a>
        </div>
      </div>
    </div>
    <div class="list-card card">
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
            <td>{{ `${vacation.start_date} ~ ${vacation.end_date}` }}</td>
            <td>{{ vacation.is_approved == null ? '미승인':(vacation.is_approved?'승인':'승인거부') }}</td>
            <td>
              <button @click="cancel(vacation.vacation_id)">
                취소
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <PaginationBar
        :total="total"
        @page="pagination"
      />
    </div>
  </div>
</template>
  
<script>
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

import {ref} from 'vue';
import CardHead from '@/components/CardHead.vue';
import PaginationBar from '@/components/common/PaginationBar.vue';

const format = (date) => {
  return `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`;
}
  export default { 
    components:{ Datepicker, CardHead, PaginationBar },
    setup(){
      const startDate = ref();
      const endDate = ref();
      
      return {
        startDate,
        endDate,
        format,
      }
    },
      data(){
          return{
              vacationList:[],
              page:1,
              total:1,
          }
      },
      computed:{
        getDarkMode() {
          return this.$store.getters.getDarkMode;
        },
        getUser () {
          return this.$store.getters.getUser;
        },
      },
      mounted(){
        this.getList();
      },
      methods:{
          search(text){
              console.log(text);
          },
          async submit(){
            try{
              const {data} = await this.$axios.post(`/vacation/user/${this.getUser.user_id}`,{
                start_date:format(this.startDate),
                end_date:format(this.endDate)
              }) ;
              if(data.success){
                this.getList();
                alert('신청이 완료되었습니다.');
              }else{
                alert('날짜를 확인해주세요.');
              }
            }catch(err){
              console.log(err);
            }
          },
          async getList(){
            try{
              const {data} = await this.$axios.get(`/vacation/user/${this.getUser.user_id}?page=${this.page}`);
              this.vacationList = data.items;
              this.total = parseInt((data.total+9)/10);
              // console.log(data);
            }catch(err){
              console.log(err);
            }
          },
          async cancel(vacation_id){
            try{
              const {data} = await this.$axios.delete(`/vacation/${vacation_id}`) ;
              if(data.success){
                this.getList();
                alert('취소가 완료되었습니다.');
              }else{
                alert('날짜를 확인해주세요.');
              }
            }catch(err){
              console.log(err);
            }
          }
      },
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
    height:183px;
    flex-direction: column;
    justify-content: flex-start;
  }
  .search-content{
    box-sizing:border-box;
    width: 100%;
    height:100%;
    padding:0px 54px;
    display:flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap:33px;
  }

  .datepicker-wrap{
    display:flex;
    align-items:center;
    gap:16px;
    
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
    justify-content:flex-start;
    width:100%;
    gap:24px;
  }
  .term{
    display:flex;
    align-items:center;
    justify-content: flex-end;
    width:100%;
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
      justify-content: space-between;
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
      /* height:100%; */
      border-collapse: collapse; 
    /* border-spacing: 0 5px; */
  }
  
  th, td{
      
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
      height:56px;
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

    
    font-style: normal;
    font-weight: 700;
    font-size: 16px;
    line-height: 19px;
    /* identical to box height */

    letter-spacing: 0.15px;
}
.gaurdroom{
  margin-right:26px;
  display:flex;
  align-items:center;
  gap:16px;
}

.gaurdroom .dropdown{
  border: 1px solid var(--color-input-border);
  border-radius: 4px;
  width:224px;
  box-sizing:border-box;
  display:flex;
  flex-direction:column;
  align-items: flex-start;
  justify-content: flex-start;
  position:relative;
}
.gaurdroom .dropdown input{
  border:none;
  font-weight: 400;
  font-size: 12px;
  line-height: 14px;
  width:100%;
  height:28px;

  padding:6px 10px;
  box-sizing:border-box;
  background:var(--color-input);
}
.gaurdroom .dropdown input:focus{
  outline:none;
}

.gaurdroom .dropdown .ditem{
  font-weight: 400;
  font-size: 12px;
  line-height: 14px;
  width:100%;
  height:28px;
  padding:6px 10px;
  box-sizing:border-box;
  background:var(--color-input);
  border-bottom:1px solid var(--color-input-border);
  display:flex;
  justify-content: flex-start;
}
.gaurdroom .active{
  border-bottom-left-radius:0px;
  border-bottom-right-radius:0px;
  border-bottom:none !important;
}
.gaurdroom .dropdown .ditem:hover{
  background:var(--color-state-card);
}
.dropdown-list{
  width:100%;
  position:absolute;
  top:28px;
  border: 1px solid var(--color-input-border);
  border-bottom-left-radius:4px;
  border-bottom-right-radius:4px;
  left:-1px;
  border-bottom:none;
}
  </style>


<style>
/* datepicker style */
.datepicker-input{
    width: 224px;
    box-sizing: border-box;
    height:28px;
    
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