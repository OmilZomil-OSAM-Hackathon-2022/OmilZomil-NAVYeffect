module.exports = {
  root: true,
  parserOptions:{
    parser: '@babel/eslint-parser',
  },
  env:{
    node:true,
    browser: true,
  },
  extends: [
    // add more generic rulesets here, such as:
    'eslint:recommended',
    'plugin:vue/vue3-recommended',
    // 'plugin:vue/vue3-essential', // This option doesn't impose formatting rules
    // 'plugin:vue/vue3-strongly-recommended', // This option imposes formatting rules on your code to improve readability 
  ],
  rules: {
    // override/add rules settings here, such as:
    // 'vue/no-unused-vars': 'error'
    // "vetur.validation.style": false,
  }
}