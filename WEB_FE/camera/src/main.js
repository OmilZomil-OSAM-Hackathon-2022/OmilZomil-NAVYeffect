import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
// import io from "socket.io-client"

// const socket = io("http://131.186.17.227:7717/docs#/");

// const SocketPlugin = {
//     install(vue) {
//         vue.mixin({});
//     }
// }

createApp(App).use(store).use(router).mount("#app");
