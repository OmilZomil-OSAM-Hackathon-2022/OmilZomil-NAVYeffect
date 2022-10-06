<template>
    <div class="check-tag">
      <img
        v-if="isCheck"
        src="@/assets/icons/manager-check.svg"
      >
      <img
        v-else
        src="@/assets/icons/manager-nocheck.svg"
      >
    </div>
  </template>
  
  <script>
  export default {
    props:{
      isCheck:{
        type:Boolean,
        default:true,
      }
    }
  }
  </script>
  
  <style scoped>
  .check-tag{
    width: 26px;
    height:24px;
    background: var(--color-state-card);
    display:flex;
    align-items: center;
    justify-content: center;
    border-radius: 4px;
  }
  </style>