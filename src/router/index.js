import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/pages/home'
import entityQueryByPerson from '@/components/pages/q-e-byPerson'
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
