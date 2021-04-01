import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const moduleA = {
  state: {
    user: {
      uid: "114514",
      name: "北京大學"
    }
  },
  mutations: {},
  actions: {},
  getters: {}
};

const moduleB = {
  state: {
    serverAddress: "127.0.0.1",
    apiAddress: "http://47.114.119.106:8000/api/"
    //⬆️update: 2020.10
    //apiAddress:'http://162.105.134.121/api/'
    //apiAddress:'http://140.247.116.238:8888/api/'
  },
  mutations: {},
  actions: {},
  getters: {}
};

export default new Vuex.Store({
  modules: {
    local: moduleA,
    global: moduleB
  }
});
