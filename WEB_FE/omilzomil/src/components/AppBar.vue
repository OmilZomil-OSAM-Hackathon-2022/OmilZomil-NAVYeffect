<template>
  <div class="app-bar">
    <div class="wrap">
        <div class="top">
            <div class="logo">
                <img width="30" src="@/assets/logo.svg"/>
                <h1>OMIL-ZOMIL</h1>
            </div>
            <div class="options">
                <div>
                    <input type="checkbox" id="toggle" hidden> 

                    <label for="toggle" class="toggleSwitch">
                        <span class="toggleButton"></span>
                    </label>
                </div>

                <button />
                <button />
                <input type="text"/>
            </div>
        </div>
        <div></div>
    </div>
  </div>
</template>

<script>
export default {
    name:"AppBar",
}
// src="@/assets/styles/common.css"
</script>

<style scoped >
@import '@/assets/styles/common.css';
.app-bar{
    /* width:100%; */
    background: #FFFFFF;
    box-shadow: 0px 4px 25px rgba(145, 85, 235, 0.03);
    height:48px;
    display:flex;
    flex-direction: column;
    align-items: center;
}
.top{
    display:flex;
    justify-content: space-between;
    align-items: center;
}
.top h1{
    width: 111px;
    height: 22px;

    font-family: 'Inter';
    font-style: normal;
    font-weight: 700;
    font-size: 18px;
    line-height: 22px;

    color: #9155EB;
}
.top .logo{
    display:flex;
    align-items: center;
}
.top .logo img{
    margin-right:5px;
}
.top .options{
    display:flex;
}

.toggleSwitch {
  width: 6rem;
  /* margin: 2rem; */
  height: 3rem;
  display: block;
  position: relative;
  border-radius: 2rem;
  background-color: #fff;
  /* box-shadow: 0 0 1rem 3px rgba(0 0 0 / 15%); */
  border: 1px solid #D9D8E8;
  cursor: pointer;
}

.toggleSwitch .toggleButton {
  width: 1.5rem;
  height: 1.5rem;
  position: absolute;
  top: 50%;
  left: 10%;
  transform: translateY(-50%);
  border-radius: 50%;
  background: rgba(145, 85, 235, 0.2);
  border:#9155EB solid 5px;
}

/* 체크박스가 체크되면 변경 이벤트 */
#toggle:checked ~ .toggleSwitch {
  background: #32313F;
}

#toggle:checked ~ .toggleSwitch .toggleButton {
  left: calc(100% - 2.8rem);
  background: #78798D;

  border: #fff solid 5px;
}

.toggleSwitch, .toggleButton {
  transition: all 0.2s ease-in;
}

</style>