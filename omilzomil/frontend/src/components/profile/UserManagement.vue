<template>
  <div class="page">
    <div class="search-div">
      <SearchInput @search="search" />
    </div>
    <div class="filter-wrap">
      <select v-model="classFilter">
        <option
          :value="null"
          disabled
          selected
        >
          계급을 선택하세요.
        </option>
        <option
          :value="null"
        >
          전체
        </option>
        
        <option
          v-for="rank in ranks"
          :key="rank.rank_id"
          :value="rank.rank_id"
        >
          {{ rank.rank }}
        </option>
      </select>
      <select v-model="divisionFilter">
        <option
          :value="null"
          disabled
          selected
        >
          소속을 선택하세요.
        </option>
        <option
          :value="null"
        >
          전체
        </option>
        <option
          v-for="affiliation in affiliations"
          :key="affiliation.affiliation_id"
          :value="affiliation.affiliation_id"
        >
          {{ affiliation.affiliation }}
        </option>
      </select>
      <select v-model="unitFilter">
        <option
          :value="null"
          disabled
          selected
        >
          부대를 선택하세요.
        </option>
        <option
          :value="null"
        >
          전체
        </option>
        <option
          v-for="unit in units"
          :key="unit.unit_id"
          :value="unit.unit_id"
        >
          {{ unit.unit }}
        </option>
      </select>
      <select v-model="isActive">
        <option
          :value="null"
          disabled
          selected
        >
          승인 여부를 선택하세요.
        </option>
        <option
          :value="null"
        >
          전체
        </option>
        <option value="false">
          미승인
        </option>
        <option value="true">
          승인
        </option>
      </select>
      <button
        class="filterbtn"
        @click="filtering"
      >
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
        <tr
          v-for="user in users"
          :key="user.user_id"
        >
          <td>{{ user.full_name }}</td>
          <td>{{ user.affiliation_title }}</td>
          <td>{{ user.unit_title }}</td>
          <td>{{ user.rank_title }}</td>
          <td>{{ user.dog_number }}</td>
          <td>
            <select
              v-model="user.role"
              @change="changeRole(user.user_id,user.role)"
            >
              <!-- <option value="0">
                미승인 사용자
              </option> -->
              <option value="1">
                일반 사용자
              </option>
              <option value="2">
                관리자
              </option>
              <option
                v-if="getAdmin.role > 2"
                value="3"
              >
                루트 관리자
              </option>
            </select>
          </td>
          <td>
            <div style="display:flex; justify-content:center">
              <CheckTag
                :is-check="user.is_active"
                style="cursor:pointer"
                @click="activeUser(user.user_id,user.is_active)"
              />
            </div>
          </td>
        </tr>
      </tbody>
    </table>
    <pagination-bar :total="25" />
  </div>
</template>

<script>
import SearchInput from '../common/SearchInput.vue';
import CheckTag from '../CheckTag.vue';
import PaginationBar from '../common/PaginationBar.vue';
export default {
    components: { SearchInput, CheckTag, PaginationBar },
    data(){
      return{
        classFilter:null,
        divisionFilter:null,
        unitFilter:null,
        isActive:null,
        units:[],
        affiliations:[],
        ranks:[],
        users:[],
        roles:[],
      }
    },
    computed:{
      getAdmin(){
          return this.$store.getters.getUser;
      }
    },
    async mounted(){
      this.getUsers();
    },
    methods:{
        getInfo(){
          for(var i=0;i<this.users.length;i++){
            this.users[i].affiliation_title = this.affiliations.filter(af => af.affiliation_id == this.users[i].affiliation)[0].affiliation;
            this.users[i].unit_title = this.units.filter(u => u.unit_id == this.users[i].military_unit)[0].unit;
            this.users[i].rank_title = this.ranks.filter(r => r.rank_id == this.users[i].rank)[0].rank;
          }
        },
        async filtering(){
          try{
            let url = '/user/';
            let cnt = 0;
            if(this.classFilter){
              cnt++;
              if(cnt == 1) url += '?';
              else url += '&';
              url += `rank=${this.classFilter}`;
            }
            if(this.divisionFilter){
              cnt++;
              if(cnt == 1) url += '?';
              else url += '&';
              url += `affiliation=${this.divisionFilter}`;
            }
            if(this.unitFilter){
              cnt++;
              if(cnt == 1) url += '?';
              else url += '&';
              url += `military_unit=${this.unitFilter}`;
            }
            if(this.isActive != null){
              cnt++;
              if(cnt == 1) url += '?';
              else url += '&';
              url += `is_active=${this.isActive}`;
            }
            this.users = (await this.$axios.get(url)).data;
            this.getInfo();
          }catch(err){ 
            console.log(err);
          }
        },
        async search(text){
            try{
              this.users = (await this.$axios.get(`/user/?full_name=${text}`)).data;
              
              this.getInfo();
            }catch(err){
              console.log(err);
            }
        },
        async changeRole(user_id,role){
          // console.log(role);
          try{
            await this.$axios.put(`/user/role/${user_id}`,{
              role
            });
          }catch(err){
            console.log(err);
          }
        },
        async getUsers(){
          try{
            this.users = (await this.$axios.get('/user/')).data;
            
            this.affiliations = (await this.$axios.get('/affiliation/')).data;
            this.ranks = (await this.$axios.get('/rank/')).data;
            this.units = (await this.$axios.get('/unit/')).data;
            this.roles = (await this.$axios.get('role')).data;
            // console.log(this.users);
            this.getInfo();
            console.log(this.users);
          }catch(err){
            console.log(err);
          }
        },
        async activeUser(user_id,is_active){
          try{
            const {data} = await this.$axios.put(`/user/activity/${user_id}`,{
              is_active:!is_active
            });
            if(data.success){
              this.getUsers();
            }else{
              alert('오류!');
            }
          }catch(err){
            console.log(err);
          }
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
