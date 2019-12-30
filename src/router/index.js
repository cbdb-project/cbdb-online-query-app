import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import entityQueryByPerson from '@/components/q-e-byPerson'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/index',
      name: 'Index',
      component: HelloWorld
    },
    { path: '/', 
      redirect: { name: 'Index' }
    },
    {
      path: '/help',
      name: 'Help',
      component: HelloWorld
    },
    {
      path: '/q-entity/by-person',
      name: 'Entity Query: By Person',
      component: entityQueryByPerson
    }
  ]
})
