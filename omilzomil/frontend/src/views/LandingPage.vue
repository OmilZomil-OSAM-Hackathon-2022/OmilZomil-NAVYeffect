<template>
  <div class="landing-page">
    <section class="intro">
      <div class="wrap">
        <div class="deco1" />
        <div class="deco2" />
        <div class="title-wrap">
          <h2>오밀조밀</h2>
          <h1>쉽게 복장, 두발 불량을 찾아냅니다.</h1>
        </div>
        <img
          width="708"
          class="dashboard-image"
          src="@/assets/images/dashboard.png"
        >
      </div>
    </section>
    <section class="problem">
      <div class="wrap">
        <div class="soldier-image-wrap">
          <div class="image-back" />
          <div
            class="massege-box"
            style="padding:19px 23px;top:20px;left:-145px;"
          >
            출입 인원이 많으면 시간이 지체돼요.
          </div>
          <div
            class="massege-box"
            style="padding:19px 35px;top:50px;left:250px;"
          >
            사람마다 불량 판단 기준이 달라요.
          </div>
          <div
            class="massege-box"
            style="padding:28px 19px;left: -230px;top:200px;z-index:11"
          >
            많은 복장, 두발 규정 모두 알고있기 힘들어요.
          </div>
          <div
            class="massege-box"
            style="padding:18px 30px;left: 255px;top:240px;z-index:11"
          >
            추후 확인할 수 있는 방안이 없어요.
          </div>
          <img
            class="soldier-image"
            src="@/assets/images/soldier.png"
          >
        </div>
        <div class="bar" />
        <h2>찾아내기 힘든 복장, 두발 불량</h2>
        <h1>
          오밀조밀은 "<div style="color:#A265FE">
            영상 처리 AI
          </div>"를 통해 쉽게 해결합니다.
        </h1>
      </div>
    </section>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.landing-page{
    width:100%;
}
.intro{
    width:100%;
    height:845px;
    background: #1E1C2E;
    overflow:hidden;
    display:flex;
    justify-content:center;
}

.intro .wrap{
    position:relative;
    height:100%;
}
.intro .deco1{
    position: absolute;
    width: 440px;
    height: 1536.74px;
    left: 164.42px;
    top: -374px;

    background: #221E36;
    transform: rotate(36.95deg);
}
.intro .deco2{
    position: absolute;
    width: 440px;
    height: 1560.91px;
    left: 478.42px;
    top: -351px;

    background: #2B2245;
    transform: rotate(36.95deg);
}
.intro .title-wrap{
    position:absolute;
    color:white;
    display:flex;
    flex-direction: column;
    align-items: flex-start;
    top:88px;
}

.intro .title-wrap h2{
    font-weight: 700;
    font-size: 32px;
    line-height: 150%;
    margin:0px;
}

.intro .title-wrap h1{
    font-weight: 700;
    font-size: 40px;
    line-height: 150%;
    margin:0px;
}

.intro .dashboard-image{
    position:absolute;
    bottom:0px;
    right:0px;
    z-index:100;
}

.problem{
    height:695px;
    background-image:url("@/assets/images/problem-background.png");
    background-repeat: no-repeat;
    background-position: center;
    display:flex;
    justify-content:center;
    background-size : cover;
}

.problem .wrap{
    display:flex;
    flex-direction:column;
    align-items: center;
    justify-content: center;
}

.problem .soldier-image-wrap{
    position:relative;
}
.problem .image-back{

    background: rgba(145, 85, 235, 0.1);
    filter: blur(17.5px);
    width:346px;
    height:346px;
    border-radius:100%;
}
.problem .soldier-image{
    position:absolute;
    z-index: 10;
    top:38px;
    left:39px;
}

.problem .bar{
    width: 227px;
    height: 14px;
    background: linear-gradient(180deg, #6F45AE 0%, rgba(30, 28, 46, 0) 100%);
    margin-top:22px;
}
.problem h1,.problem h2{
    margin:0px;

    display:flex;
    color:white;
}
.problem h2{
    margin-top:40px;
    margin-bottom:4px;
}

.massege-box{
  position:absolute;
  font-style: normal;
  font-weight: 500;
  font-size: 15px;
  line-height: 150%;
  /* identical to box height, or 22px */

  text-align: center;

  /* Dark1 */

  color: #32313F;
  background: #FFFFFF;
  box-shadow: 0px 0px 20px rgba(92, 92, 92, 0.4);
  border-radius: 20px;
  white-space: nowrap;
}
</style>