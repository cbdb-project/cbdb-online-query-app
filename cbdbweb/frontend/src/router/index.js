import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/views/home'
import entityQueryByPerson from '@/components/views/q-e-byPerson'
import entityQueryByEntry from '@/components/views/q-e-byEntry'
import entityQueryByOffice from '@/components/views/q-e-byOffice'
import relationQueryByKinship from '@/components/views/q-r-byKinship'
//import relationQueryByAssociation from '@/components/views/q-r-byAssociation'
import relationQueryBySocialNetwork from '@/components/views/q-r-bySocialNetwork'
//import relationQueryTwoPerson from '@/components/views/q-r-byTwoPerson'
import visualizationBySNA from '@/components/views/vis-bySNA'
//import visualizationByGIS from '@/components/views/vis-byGIS'
//import visualizationByGraphs from '@/components/views/vis-byGraphs'

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
      path: '/q-relation/kinship',
      name: 'Relation Query: By Kinship',
      component: relationQueryByKinship
    },
   /* 
    {
      path: '/q-relation/association',
      name: 'Relation Query: By Association',
      component: relationQueryByAssociation
    },
     */
    {
      path: '/q-relation/by-social-network',
      name: 'Relation Query: By Socialnetwork',
      component: relationQueryBySocialNetwork
    },
    /*
    {
      path: '/q-relation/two-person',
      name: 'Relation Query: By TwoPerson',
      component: relationQueryTwoPerson
    },
    */
    {
      path: '/visualization/SNA',
      name: 'Visualization: SNA',
      component: visualizationBySNA
    },
    /*
    {
      path: '/visualization/GIS',
      name: 'Visualization: GIS',
      component: visualizationByGIS
    },
    {
      path: '/visualization/Graphs',
      name: 'Visualization: Graphs',
      component: visualizationByGraphs
    },
    */
  ]
})
