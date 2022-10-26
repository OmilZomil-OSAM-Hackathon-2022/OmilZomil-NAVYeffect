<template>
  <div class="check-tag">
    <img
      v-if="isCheck"
      :class="{big:isBig}"
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
        },
        isBig:{
          type:Boolean,
          default:false,
        }
      }
    }
    </script>
    
    <style scoped>
    .big{
      width:24px;
    }
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