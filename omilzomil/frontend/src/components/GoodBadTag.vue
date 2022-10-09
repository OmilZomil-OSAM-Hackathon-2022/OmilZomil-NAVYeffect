<template>
  <div
    class="good-bad-tag"
    :style="{color:isGood?'#3FC6B8':'#FF5467'}"
  >
    <img
      v-if="isGood"
      src="@/assets/icons/check-circle.svg"
    >
    <img
      v-else
      src="@/assets/icons/error-circle.svg"
    >
    {{ isGood ? "양호":"불량" }}
  </div>
</template>

<script>
export default {
  props:{
    isGood:{
      type:Boolean,
      default:true,
    }
  }
}
</script>

<style scoped>
.good-bad-tag{
  width: 55px;
  height:28px;
  background: var(--color-state-card);
  display:flex;
  align-items: center;
  justify-content: center;
  gap:5px;
  border-radius: 4px;
  font-family: 'Roboto';
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 16px;
  letter-spacing: 0.25px;
}
</style>