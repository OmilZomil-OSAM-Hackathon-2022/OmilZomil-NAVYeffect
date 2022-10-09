<template>
  <div
    class="wrap"
  >
    <div class="card">
      <table>
        <thead>
          <tr> 
            <th>순위</th>
            <th>부대</th>
            <th>양호수</th>
            <th>위반수</th>
            <th>위반비율</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(user,index) in pageList[this.page-1]"
            :key="index"
          >
            <td class="rank">
              <img v-if="(this.page-1)*10+index===0" src="@/assets/icons/first.svg" />
              <img v-else-if="(this.page-1)*10+index===1" src="@/assets/icons/second.svg" />
              <img v-else-if="(this.page-1)*10+index===2" src="@/assets/icons/third.svg" />
              <div v-else>
                {{ (this.page-1)*10+index+1 }}
              </div> 
            </td>
            <td class="name">{{ user.name }}</td>
            <td class="number">{{ user.goodNumber }}명</td>
            <td class="number">{{ user.badNumber }}명</td>
            <td class="percent">{{ user.percent }}%</td>
          </tr>
        </tbody>
      </table>
      <foot>
        <tr>
          <tf class="choose">
              <div class="choosebox">
                <select v-model.number="this.page">
                  <option v-for="i in pageList.length" :key="i" value.number="i">{{i}}</option>
                </select>
              </div>
              <div class="max-page">
                /{{ pageList.length }}
              </div>
          </tf>
          <tf class="prev-next">
            <button class="prev" v-if="page!=1" @click="this.page-=1" />
            <img class="prev" v-else src="@/assets/icons/prev.svg" />
            <button class="next" v-if="page!=this.pageList.length" @click="this.page+=1" />
            <img class="next" v-else src="@/assets/icons/next.svg" />
          </tf>
        </tr>
      </foot>
    </div>
  </div>
</template>

<script>
class User{
    constructor(){
        this.name = "계룡대 본부대대";
        this.goodNumber = "269";
        this.badNumber = "269";
        this.percent = "1";
    }
}
class User2{
  constructor(){
        this.name = "계룡대 군경대대";
        this.goodNumber = "250";
        this.badNumber = "250";
        this.percent = "2";
    }
}
class User3{
  constructor(){
        this.name = "계룡대 수송대대";
        this.goodNumber = "230";
        this.badNumber = "230";
        this.percent = "3";
    }
}

export default {
    data(){
        return{
            page:1,
            pageList:[
              [
                new User(),
                new User(),
                new User(),
                new User(),
                new User(),
                new User(),
                new User(),
                new User(),
                new User(),
                new User(),
              ],
              [
                new User2(),
                new User2(),
                new User2(),
                new User2(),
                new User2(),
                new User2(),
                new User2(),
                new User2(),
                new User2(),
                new User2(),
              ],
              [
                new User3(),
                new User3(),
                new User3(),
                new User3(),
                new User3(),
                new User3(),
                new User3(),
                new User3(),
                new User3(),
              ]
            ]
        }
    },
    methods:{
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
    justify-content: space-between;
    box-sizing: border-box;
    padding: 28px 61px;
    /* align-items: flex-start; */
}
table{
    width:100%;
    border-collapse: collapse; 
    /* border-bottom: 1px solid #E1E2E9; */
    /* border-spacing: 0 16px; */
}
th{
  width: 50px;
  height: 50px;
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 16px;
  text-align: center;
  letter-spacing: 0.25px;
}
td{
  width: 50px;
  height: 50px;
  font-family: 'Roboto';
  font-style: normal;
  text-align: center;
  /* color: #78798D; */
}
.rank{
  font-weight: 700;
  font-size: 20px;
  line-height: 23px;
  letter-spacing: 0.5px;
}
.name{
  font-weight: 700;
  font-size: 16px;
  line-height: 19px;
  letter-spacing: 0.15px;
}
.number{
  font-weight: 400;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 0.25px;
}
.percent{
  font-weight: 700;
  font-size: 16px;
  line-height: 19px;
  letter-spacing: 0.15px;
}

table thead tr{
    border-bottom: 1px solid #E1E2E9;
    height:52px;
}
table tbody tr{
    height:58px;
}
foot{
  position:relative;
  box-sizing: border-box;
  width: 100%;
  height: 40px;
  border-top: 1px solid #E1E2E9;
}
.maxpage{
  width: 27px;
  height: 17px;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 17px;
  color: #616276;
}
.choose{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 0px;
  gap: 8px;

  position: absolute;
  width: 87px;
  height: 23px;
  right: 64px;
  top: 9px;
}
.choosebox{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0px 11px;
  gap: 10px;

  width: 52px;
  height: 23px;

  background: rgba(94, 99, 102, 0.08);
  border-radius: 8px;
}
.prev-next{
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  padding: 0px;
  gap: 8px;

  position: absolute;
  width: 40px;
  height: 16px;
  right: 0px;
  top: 13px;
}
.prev{
  background: url("@/assets/icons/prev.svg") no-repeat;
  width: 16px;
  height: 16px;
  border:none;
  cursor:pointer;
}
.next{
  background: url("@/assets/icons/next.svg") no-repeat;
  width: 16px;
  height: 16px;
  border:none;
  cursor:pointer;
}
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