<template>
  <div class="row-center">
    <div class="wrap">
      <div class="row row-1">
        <div class="card card-1">
          test
        </div>
        <div class="row card-1">
          <div class="card">
            test
          </div>
          <div class="card">
            test
          </div>
          <div class="card">
            test
          </div>
        </div>
      </div>
      <div class="row row-2">
        <div class="list-up">
          <ListUp gap="46" />
        </div>
        <div class="card" />
      </div>
    </div>
  </div>
</template>

<script>
import ListUp from '@/components/ListUp.vue';
export default {
    components: { ListUp }
}
</script>

<style scoped>

.row{
    display:flex;
    gap:24px;
    /* margin-top:40px; */
}
.row-1{
    height:196px;
}
.row-2{
    margin-top:40px;
    height: 562px;
}
.card-1{
    width:50%;
}
.list-up{
  width:792px;
}
</style>