<template>
  <div class="card">
    <div class="title">
      <img
        src="@/assets/icons/left-arrow.svg"
        height="12"
        style="cursor:pointer"
        @click="$emit('close')"
      >
      {{ title }} 위병소 연결
    </div>
    <div class="search-div">
      <form
        class="add-unit"
        @submit.prevent="addHouse"
      >
        <input
          v-model="newHouse"
          placeholder="위병소 이름을 입력하세요."
          list="list"
        >
        <datalist
          v-if="newHouse.length >= 2"
          id="list"
        >
          <option
            v-for="h in allHouses"
            :key="h.house_id"
          >
            {{ h.house }}
          </option>
        </datalist>
        <button>추가</button>
      </form>
    </div>
    <table>
      <thead>
        <tr>
          <th>
            위병소
          </th>
          <th>연결</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="house in houses"
          :key="house.house_id"
        >
          <td>{{ house.house }}</td>
          <td>
            <div
              class="tcenter"
            >
              <a @click="delHouse(house.house_id)">해제</a>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
  
  <script>
  export default {
      props:{
        title:{
            type:String,
            default:'',
        },
        unitID:{
            type:Number,
            default:0,
        },
      },
      emits:["close"],
      data(){
        return{
          allHouses:[],
          houses:[],
          newHouse:'',
          searchHouse:[],
        }
      },
      async mounted(){
        this.getHouse();
        try{
            this.allHouses = (await this.$axios.get('/house/')).data;
            // console.log(this.allHouses);
        }catch(err){
            console.log(err);
        }
      },
      methods:{
          async getHouse(){
            try{
              const {data} = await this.$axios.get(`/unit/relation/${this.unitID.toString()}`);
              this.houses = data;
            }catch(err){ 
              console.log(err);
            }
          },
          async addHouse(){
            const h = this.allHouses.filter(h => h.house == this.newHouse);
            if(h.length > 0){
                await this.$axios.post(`/unit/relation/${this.unitID.toString()}`,{
                    house_id:h[0].house_id
                });
                this.getHouse();
                this.newHouse = '';
            }else{
                alert("위병소 이름을 확인해주세요!");
            }
          },
          async delHouse(house_id){
            try{
                await this.$axios.delete(`/unit/relation/${this.unitID.toString()}/${house_id}`);
                this.getHouse();
            }catch(err){
                console.log(err);
            }
          }
      }
  }
  </script>
  
  <style scoped>
  .card{    
    padding:28px 61px;
    position:absolute;
    top:0px;
    left:0px;
    box-sizing:border-box;
      /* padding:28px 61px; */
      display:flex;
      flex-direction:column;
      justify-content: flex-start;
      box-shadow: none;
      border-radius:0px 0px 0px 0px;
  }
  .title{
    display:flex;
    align-items:center;
    background:var(--color-state-card);
    width:100%;
    gap:18px;
    height:46px;
    border-radius: 20px;
    box-sizing: border-box;
    padding:0px 21px;
    margin-bottom: 30px;
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

  datalist{
    width:100%;
  }
  </style>
  