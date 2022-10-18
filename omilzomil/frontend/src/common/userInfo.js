import VueCookies from 'vue-cookies';

const USER_INFO_KEY = "user_info"

export const getUserInfo = () => {
  const userString = VueCookies.get(USER_INFO_KEY);
  // if(userString !== null){
    // console.log(userString);
    // return JSON.parse(userString);
  // }
  return userString;
  // const userString = window.localStorage.getItem(USER_INFO_KEY);
  // if(userString !== null){
  //   return JSON.parse(userString);
  // }
  // return userString;
}

export const saveUser = user => {
  VueCookies.set(USER_INFO_KEY, JSON.stringify(user),'2h');
  // window.localStorage.setItem(USER_INFO_KEY, JSON.stringify(user))
}

export const destroyUser = () => {
  // window.localStorage.removeItem(USER_INFO_KEY)
  VueCookies.remove(USER_INFO_KEY);
}

export default {
  getUserInfo,
  saveUser,
  destroyUser,
}