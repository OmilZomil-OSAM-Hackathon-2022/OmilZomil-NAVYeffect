<template>
  <div class="page">
    <div class="search-div">
      <form
        class="add-unit"
        @submit.prevent="addUnit()"
      >
        <input
          v-model="newUnit"
          placeholder="부대 이름을 입력하세요."
        >
        <button>추가</button>
      </form>
      <SearchInput @search="search" />
    </div>
    <table>
      <thead>
        <tr>
          <th>
            부대이름
          </th>
          <th>위병소 관리</th>
          <th>변경</th>
          <th>삭제</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="unit in units.slice((page-1)*10,page*10 > units.length? units.length:page*10)"
          :key="unit.unit_id"
        >
          <td>{{ unit.unit }}</td>
          <td>
            <div
              class="tcenter"
            >
              <a @click="openConect(unit.unit,unit.unit_id)">관리</a>
            </div>
          </td>
          <td>
            <div
              class="tcenter"
            >
              <a
                @click="openEdit(unit.unit,unit.unit_id)"
              >변경</a>
            </div>
          </td>
          <td>
            <div
              class="tcenter"
            >
              <a
              
                @click="deleteUnit(unit.unit_id)"
              >삭제</a>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
    <PaginationBar
      :total="parseInt((units.length+9)/10)"
      @page="pagination"
    />
    <EditTitleCard
      v-if="isEdit"
      title="부대"
      :data="editText"
      @close="closeEdit"
      @submit="submitEdit"
    />
    <ConectCard
      v-if="isConect"
      :title="editText"
      :unit-i-d="editUnitID"
      @close="closeConect"
    />
  </div>
</template>

<script>
import SearchInput from '../common/SearchInput.vue';
import EditTitleCard from './EditTitleCard.vue';
import ConectCard from './ConectCard.vue';
import PaginationBar from '../common/PaginationBar.vue';
export default {
    components: { SearchInput, EditTitleCard, ConectCard, PaginationBar },
    data(){
      return{
        classFilter:'',
        divisionFilter:'',
        unitFilter:'',
        units:[],
        isEdit:false,
        editText:'',
        editUnitID:0,
        newUnit:'',
        isConect:false,
        page:1,
      }
    },
    mounted(){
      this.getUnits();
    },
    methods:{
      pagination(page){
        this.page = page;
      },
        async getUnits(){
          try{
            const {data} = await this.$axios.get('/unit/');
            this.units = data;
          }catch(err){ 
            console.log(err);
          }
        },
        closeEdit(){
          this.isEdit = false;
        },
        openEdit(text,id){
          this.editUnitID = id;
          this.editText = text;
          this.isEdit = true;
        },
        closeConect(){
          this.isConect = false;
        },
        openConect(text,id){
          this.editUnitID = id;
          this.editText = text;
          this.isConect = true;
        },

        async submitEdit(text){
          if(text == '' || this.editText == text){
            this.closeEdit();
            return;
          }
          try{
            await this.$axios.put(`/unit/${this.editUnitID}`,{
              unit:text
            });
            this.getUnits();
          }catch(err){ 
            console.log(err);
          }
          this.closeEdit();
        },
        async deleteUnit(unit_id){
          try{
            await this.$axios.delete(`/unit/${unit_id}`);
            this.getUnits();
          }catch(err){ 
            console.log(err);
          }
        },
        async addUnit(){
          try{
            await this.$axios.post('/unit/',{
              unit:this.newUnit
            });
            this.newUnit = '';
            this.getUnits();
          }catch(err){
            console.log(err);
          }
        },
        async search(text){
          try{
            const {data} = await this.$axios.get(`/unit/?unit=${text}`);
            this.units = data;
            this.page = 1;
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
