// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
//I18n 用于處理語言切換
import VueI18n from 'vue-i18n'
Vue.use(VueI18n)
//router 用于处理路由
import router from './router'
//store 用于處理全局變數
import store from './store'
import BootstrapVue from 'bootstrap-vue'
  Vue.use(BootstrapVue)
//引入 bootstrap-vue 的 css 檔
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
//引入 axios 和 vue-axios
import axios from 'axios'
import VueAxios from 'vue-axios'
 
Vue.use(VueAxios, axios)

Vue.config.productionTip = false
//初始化語言設定
let langConfig =  {
  locale:'zh-cmn-Hant',
  messages:{
    'zh-cmn-Hant':require('./assets/lang/zh-cmn-Hant'),
    'en':require('./assets/lang/en'),
  }
}
//檢查本地是否有語言設定
if(localStorage.lang){
  langConfig.locale = localStorage.lang;
} 
const i18n = new VueI18n(
  langConfig
)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  i18n,
  router,
  store,
  components: { App },
  template: '<App/>'
})
