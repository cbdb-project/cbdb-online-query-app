import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const moduleA = {
  state:{
    lang: 'zh-TW',
    user:{
      uid:"114514",
      name:"北京大學"
    }
  },
  mutations:{},
  actions:{},
  getters:{}
}

const moduleB = {
  state:{},
  mutations:{},
  actions:{},
  getters:{}
}

export default new Vuex.Store({
  modules:{
    a: moduleA,
    b: moduleB
  }
})