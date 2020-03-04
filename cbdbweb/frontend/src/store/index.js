import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const moduleA = {
  state:{
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
  state:{
    serverAddress:'127.0.0.1'
  },
  mutations:{},
  actions:{},
  getters:{}
}

export default new Vuex.Store({
  modules:{
    local: moduleA,
    global: moduleB
  }
})