const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  //코드 서버 설정
  devServer : {
    allowedHosts: 'all', 
      // disableHostCheck : true 
    }
  // css: {
  //   loaderOptions: {
  //     sass: {
  //       data: `
  //         @import "@/assets/styles/common.scss";
  //       `
  //     }
  //   }
  // }
})
