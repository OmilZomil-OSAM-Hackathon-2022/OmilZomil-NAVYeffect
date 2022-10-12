<template>
  <div class="page">
    <div class="search-wrap">
      <SearchInput :on-click="search" />
    </div>
  </div>
</template>

<script>
import SearchInput from '../common/SearchInput.vue';
export default {
    components: { SearchInput },
    methods:{
        search(text){
            text;
        }
    }
}
</script>

<style scoped>
.page{
    padding:28px 61px;
}
.search-wrap{
    width:100%;
    display:flex;
    justify-content:flex-end;
    margin-bottom:20px;
}
</style>