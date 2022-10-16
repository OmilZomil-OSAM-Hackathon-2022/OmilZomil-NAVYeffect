const USER_INFO_KEY = "user_info"

export const getUserInfo = () => {
  const userString = window.localStorage.getItem(USER_INFO_KEY);
  if(userString !== null){
    return JSON.parse(userString);
  }
  return userString;
}

export const saveUser = user => {
  window.localStorage.setItem(USER_INFO_KEY, JSON.stringify(user))
}

export const destroyUser = () => {
  window.localStorage.removeItem(USER_INFO_KEY)
}

export default {
  getUserInfo,
  saveUser,
  destroyUser,
}