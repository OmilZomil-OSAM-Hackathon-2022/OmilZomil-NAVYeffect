import VueCookies from 'vue-cookies';

const ID_TOKEN_KEY = "id_token"

export const getToken = () => {
  // return window.localStorage.getItem(ID_TOKEN_KEY)
  return VueCookies.get(ID_TOKEN_KEY);
}

export const saveToken = token => {
  VueCookies.set(ID_TOKEN_KEY,token,'2h');
  // window.localStorage.setItem(ID_TOKEN_KEY, token)

}

export const destroyToken = () => {
  // window.localStorage.removeItem(ID_TOKEN_KEY)
  VueCookies.remove(ID_TOKEN_KEY);
}

export default {
  getToken,
  saveToken,
  destroyToken,
}