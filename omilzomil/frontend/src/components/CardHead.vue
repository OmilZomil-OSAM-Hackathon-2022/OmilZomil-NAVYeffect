<template>
  <div class="card-head">
    {{ title }}
    <router-link
      v-if="target != null"
      :to="target"
    >
      <img src="@/assets/icons/right-arrow.svg">
      <!-- <IconBase
        :width="24"
        :height="24"
        viewBox="0 0 20 20"
      >
        <RightArrow />
      </IconBase> -->
    </router-link>
  </div>
</template>

<script>
// import IconBase from '@/components/IconBase.vue';
// import RightArrow from '@/assets/icons/right-arrow.vue';
export default {
    // components: { IconBase, RightArrow },
    props: {
        title: {
            type: String,
            default: null,
        },
        target: {
            type: String,
            default: null,
        }
    }
}
</script>

<style scoped>
.card-head{
    box-sizing:border-box;
    width:100%;
    display:flex;
    justify-content: space-between;
    align-items: center;
    padding:14px 21px;
    background: var(--color-state-card);
    border-radius: 20px 20px 0px 0px;
    /* Subtitle 1 - Bold */

    font-style: normal;
    font-weight: 700;
    font-size: 16px;
    line-height: 19px;
    /* identical to box height */

    letter-spacing: 0.15px;
}
a{
    /* color:#9155EB; */
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>