import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

const state = {
  //注意和i18n中的索引一致
  //参考：RFC 5646
  lang: 'zh-cmn-Hant',
  user:{
    uid:"114514",
    name:"北京大學"
  }
};

const mutations = {
  //ADD_NOTE添加一个note项
}

const actions = {
  /*
        actions处理函数接受一个 context 对象
        {
          state,     // 等同于 store.state, 若在模块中则为局部状态
          rootState, // 等同于 store.state, 只存在于模块中
          commit,    // 等同于 store.commit
          dispatch,  // 等同于 store.dispatch
          getters    // 等同于 store.getters
        }
    */
};

const getters = {
  /*
        Getters 接受 state 作为其第一个参数
        state => state.notes为箭头函数等价于：
        function (state){
            return state.notes
        }
    */
  

}

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
})
