const USER_INFO_KEY = "user_info"

export const getUser = () => {
  return window.localStorage.getItem(USER_INFO_KEY)
}

export const saveUser = token => {
  window.localStorage.setItem(USER_INFO_KEY, token)
}

export const destroyUser = () => {
  window.localStorage.removeItem(USER_INFO_KEY)
}

export default {
  getUser,
  saveUser,
  destroyUser,
}