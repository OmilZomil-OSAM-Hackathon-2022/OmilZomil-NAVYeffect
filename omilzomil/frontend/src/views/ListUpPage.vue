<!-- eslint-disable vue/attribute-hyphenation -->
<template>
  <div class="wrap">
    <div class="card filter">
      <form
        class="form1"
        @submit.prevent="filterList()"
      >
        <select v-model="appearanceFilter">
          <option
            :value="null"
            disabled
            selected
          >
            불량 요소를 선택하세요.
          </option>
          <option
            v-for="ap in appearances"
            :key="ap.appearance_id"
            :value="ap.appearance_id"
          >
            {{ ap.appearance }}
          </option>
        </select>
        <select v-model="rankFilter">
          <option
            :value="null"
            disabled
            selected
          >
            계급을 선택하세요.
          </option>
          <option
            v-for="r in ranks"
            :key="r.rank_id"
            :value="r.rank_id"
          >
            {{ r.rank }}
          </option>
        </select>
        <Datepicker
          v-model="date"
          :format="format"
          range
          inputClassName="datepicker-input"
          placeholder="기한을 선택하세요."
          selectText="확인"
          :dark="getDarkMode"
        />
        <button>필터 적용</button>
      </form>
      <form
        class="form2"
        @submit.prevent="filterList()"
      >
        <button><img src="@/assets/icons/mdi_magnify.svg"></button>
        <input
          v-model="search"
          placeholder="검색"
        >
      </form>
    </div>
    <ListUp :filter="filter" />
  </div>
</template>

<script>

import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import ListUp from '@/components/ListUp.vue';
import {ref} from 'vue';

export default {
    components: { Datepicker, ListUp},
    setup(){
      const date = ref(new Date());
      const format = (date) => {
        console.log(date[0]);
        const d1 = date[0];
        const d2 = date[1];
        return `${d1.getFullYear()}/${d1.getMonth()}/${d1.getDate()} ~ ${d2.getFullYear()}/${d2.getMonth()}/${d2.getDate()}`;
      }
      return {
        date,
        format,
      }
    },
    data(){
      return {
        ranks:[],
        appearances:[],
        appearanceFilter:null,
        rankFilter:null,
        filter:'',
        search:'',
      }
    },
    computed:{
      getDarkMode() {
        return this.$store.getters.getDarkMode;
      },
    },
    async mounted(){
      this.ranks = (await this.$axios.get('/rank/')).data;
      this.appearances = (await this.$axios.get('/appearance/')).data;
    }
}
</script>

<style scoped>
.wrap{
  margin-bottom:40px;
}
.filter{
  height:76px;
  margin-bottom: 40px;
  gap:20px;
}
.form1{
  display: flex;
  gap:20px;
}
.form2{
  display: flex;
  gap:8px;
}
select{
  box-sizing: border-box;
  padding: 6px 12px;
  /* gap: 2px; */

  width: 224px;
  height: 28px;

  background: var(--color-input);
  /* Dark8 */

  border: 1px solid var(--color-input-border);
  border-radius: 4px;

  font-family: 'Roboto';
  font-style: normal;
  font-weight: 400;
  font-size: 12px;
  line-height: 14px;
  /* identical to box height */

  letter-spacing: 0.4px;

  /* Dark6 */

  color: #ABACC0;
}
input{

  background: var(--color-input);
  /* Dark8 */

  border: 1px solid var(--color-input-border);
  box-sizing: border-box;
  padding: 7px 12px;
  /* gap: 2px; */

  width: 224px;
  height: 28px;

  border-radius: 4px;
}
input::placeholder{
  color:#ABACC0;
}
button{
  /* box-sizing: border-box; */
  padding: 0px 8px;
  height:28px;
  display: flex;
  align-items: center;
  background: rgba(145, 85, 235, 0.2);
  border-radius: 4px;
  border:none;
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
.pagenation{
  width:100%;
  display:flex;
  justify-content:flex-end;
}
</style>

<style>
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