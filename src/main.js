// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
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

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
