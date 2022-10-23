<template>
  <div class="page">
    <div>
      <div class="search-div">
        <form
          class="add-unit" 
          @submit.prevent="addGaurdroom()"
        >
          <input
            v-model="newGaurdroom"
            placeholder="위병소 이름을 입력하세요."
          >
          <button>추가</button>
        </form>
        <SearchInput @search="search" />
      </div>
      <table>
        <thead>
          <tr>
            <th>
              위병소 이름
            </th>
            <th>변경</th>
            <th>삭제</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="room in gaurdrooms.slice((page-1)*8,page*8 > gaurdrooms.length ? gaurdrooms.length:page*8)"
            :key="room.house_id"
          >
            <td>{{ room.house }}</td>
            <td>
              <div class="tcenter">
                <a @click="openEdit(room.house,room.house_id)">변경</a>
              </div>
            </td>
            <td>
              <div class="tcenter">
                <a @click="deleteGaurdroom(room.house_id)">삭제</a>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <PaginationBar
      :total="parseInt((gaurdrooms.length+7)/8)"
      @page="pagination"
    />
    <EditTitleCard
      v-if="isEdit"
      title="위병소"
      :data="editText"
      @close="closeEdit"
      @submit="submitEdit"
    />
  </div>
</template>
  
<script>
  import SearchInput from '../common/SearchInput.vue';
  import EditTitleCard from './EditTitleCard.vue';
  import PaginationBar from '../common/PaginationBar.vue';
  export default {
      components: { SearchInput,EditTitleCard,PaginationBar },
      data(){
        return{
          gaurdrooms:[],
          newGaurdroom:'',
          editID:0,
          editText:'',
          isEdit:false,
          page:1,
        }
      },
      mounted(){
        this.getGaurdrooms();
      },
      methods:{
          pagination(page){
            this.page = page;
          },
          async search(text){
            try{
              this.page =1;
              this.gaurdrooms = (await this.$axios.get(`/house/?house=${text}`)).data;
            }catch(err){
              console.log(err);
            }
          },
          async getGaurdrooms(){
            try{
              this.gaurdrooms = (await this.$axios.get('/house/')).data;
            }catch(err){
              console.log(err);
            }
          },
          async addGaurdroom(){
            try{
              await this.$axios.post('/house/',{
                house:this.newGaurdroom
              })
              this.newGaurdroom = '';
              this.getGaurdrooms();
            }catch(err){
              console.log(err);
            }
          },
          async deleteGaurdroom(gaurdroom_id){
            try{
              await this.$axios.delete(`/house/${gaurdroom_id}`);
              this.getGaurdrooms();
            }catch(err){
              console.log(err);
            }
          },
          closeEdit(){
            this.isEdit = false;
          },
          openEdit(text,room_id){
            this.editID = room_id;
            this.editText = text;
            this.isEdit = true;
          },
          async submitEdit(text){
            if(text == '' || this.editText == text){
              this.closeEdit();
              return;
            }
            try{
              await this.$axios.put(`/house/${this.editID}`,{
                house:text
              });
              this.getGaurdrooms();
            }catch(err){ 
              console.log(err);
            }
            this.closeEdit();
          }
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