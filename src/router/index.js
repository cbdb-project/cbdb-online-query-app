import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/home'
import entityQueryByPerson from '@/components/q-e-byPerson'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/index',
      name: 'Index',
      component: Home
    },
    { path: '/', 
      redirect: { name: 'Index' }
    },
    {
      path: '/help',
      name: 'Help',
     
    },
    {
      path: '/q-entity/by-person',
      name: 'Entity Query: By Person',
      component: entityQueryByPerson
    }
  ]
})
