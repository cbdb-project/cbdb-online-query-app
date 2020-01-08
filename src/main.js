// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
//I18n 用于处理语言切换
import VueI18n from 'vue-i18n'
Vue.use(VueI18n)
//router 用于处理路由
import router from './router'
//store 用于处理全局变量
import store from './store'
import BootstrapVue from 'bootstrap-vue'
  Vue.use(BootstrapVue)
//引入 bootstrap-vue 的 css 文件
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

const i18n = new VueI18n(
  {
    locale:'zh-cmn-Hant',
    messages:{
      'zh-cmn-Hant':require('./assets/lang/zh-cmn-Hant'),
      'en':require('./assets/lang/en'),
    }
  }
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
