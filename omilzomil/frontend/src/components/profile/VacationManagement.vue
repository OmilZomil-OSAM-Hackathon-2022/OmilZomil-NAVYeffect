<template>
  <div class="page">
    <table>
      <thead>
        <tr>
          <th>이름</th>
          <th>소속</th>
          <th>부대</th>
          <th>계급</th>
          <th>날짜</th>
          <th>승인</th>
          <th>거부</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="v in vacations"
          :key="v.vacation_id"
        >
          <td>{{ v.user.full_name }}</td>
          <td>{{ v.user.affiliation_title }}</td>
          <td>{{ v.user.unit_title }}</td>
          <td>{{ v.user.rank_title }}</td>
          <td>{{ v.start_date }} ~ {{ v.end_date }}</td>
          <td>
            <div class="tcenter">
              <a @click="confirm(v.vacation_id)">승인</a>
            </div>
          </td>
          <td>
            <div class="tcenter">
              <a @click="reject(v.vacation_id)">거부</a>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
    <pagination-bar
      :total="total"
      @page="pagination"
    />
  </div>
</template>

<script>
import PaginationBar from '../common/PaginationBar.vue';
export default {
  components: { PaginationBar },
  data(){
    return{
      vacations:[],
      users:[],
      units:[],
      affiliations:[],
      ranks:[],
      page:1,
      total:1,
    }
  },
  async mounted(){
    try{
      this.affiliations = (await this.$axios.get('/affiliation/')).data;
      this.ranks = (await this.$axios.get('/rank/')).data;
      this.units = (await this.$axios.get('/unit/')).data;
    }catch(err){
      console.log(err);
    }
    this.getVacations();
  },
  methods:{
    pagination(page){
      this.page = page;
      this.getVacations();
    },
    async getVacations(){
      try{
        const {data} = await this.$axios.get(`/vacation/unit/?page=${this.page}&size=9`);
        for(var i=0;i<data.items.length;i++){
          data.items[i].user = (await this.$axios.get(`/user/${data.items[i].user}`)).data;
          data.items[i].user.affiliation_title = this.affiliations.filter(af => af.affiliation_id == data.items[i].user.affiliation)[0].affiliation;
          data.items[i].user.unit_title = this.units.filter(u => u.unit_id == data.items[i].user.military_unit)[0].unit;
          data.items[i].user.rank_title = this.ranks.filter(r => r.rank_id == data.items[i].user.rank)[0].rank;
        }
        this.vacations = data.items;
        this.total = Math.max(parseInt((data.total+8)/9));
      }catch(err){ 
        console.log(err);
      }
    },
    async confirm(vacation_id){
      try{
        await this.$axios.put(`/vacation/approval/${vacation_id}`,{
          is_approved: true
        });
        this.getVacations();
      }catch(err){
        console.log(err);
      }
    },
    async reject(vacation_id){
      try{
        const {data}=await this.$axios.delete(`/vacation/${vacation_id}`);
        console.log(data);
        this.getVacations();
      }catch(err){
        console.log(err);
      }
    },
  }
}
</script>

<style scoped>
.page{
    padding:28px 61px;
    display:flex;
    flex-direction:column;
    justify-content:space-between;
    height:770px;
}

table{
  width:100%;
  border-collapse: collapse; 
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
  height:66px;
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