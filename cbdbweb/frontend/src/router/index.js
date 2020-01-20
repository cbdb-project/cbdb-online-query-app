import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/views/home'
import entityQueryByPerson from '@/components/views/q-e-byPerson'
import entityQueryByEntry from '@/components/views/q-e-byEntry'
import entityQueryByOffice from '@/components/views/q-e-byOffice'
import relationQueryBySocialNetwork from '@/components/views/q-r-bySocialNetwork'
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
    },
    {
      path: '/q-entity/by-office',
      name: 'Entity Query: By Office',
      component: entityQueryByOffice
    },
    {
      path: '/q-entity/by-entry',
      name: 'Entity Query: By Entry',
      component: entityQueryByEntry
    },
    {
      path: '/q-relation/by-social-network',
      name: 'Entity Query: By Socialnetwork',
      component: relationQueryBySocialNetwork
    }
  ]
})
