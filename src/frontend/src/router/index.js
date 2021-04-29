import Vue from "vue";
import Router from "vue-router";
const Home = () => import("@/components/views/home");
//import Home from '@/components/views/home'
//const entityQueryByPerson = () => import('@/components/views/q-e-byPerson')
import entityQueryByPerson from "@/components/views/q-e-byPerson";
const entityQueryByEntry = () => import("@/components/views/q-e-byEntry");
//import entityQueryByEntry from '@/components/views/q-e-byEntry'
const entityQueryByOffice = () => import("@/components/views/q-e-byOffice");
//import entityQueryByOffice from '@/components/views/q-e-byOffice'
//const relationQueryByPlace = () => import('@/components/views/q-r-byPlace')
import relationQueryByPlace from "@/components/views/q-r-byPlace";
//const relationQueryByKinship = () => import('@/components/views/q-r-byKinship')
import relationQueryByKinship from "@/components/views/q-r-byKinship";
const relationQueryByAssociation = () =>
  import("@/components/views/q-r-byAssociation");
//import relationQueryByAssociation from '@/components/views/q-r-byAssociation'
const relationQueryBySocialNetwork = () =>
  import("@/components/views/q-r-bySocialNetwork");
//import relationQueryBySocialNetwork from '@/components/views/q-r-bySocialNetwork'
//const relationQueryTwoPerson = () => import('@/components/views/q-r-twoPerson')
import relationQueryTwoPerson from "@/components/views/q-e-byPerson-test";
//import visualizationBySNA from '@/components/views/vis-bySNA'
Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/index",
      name: "Index",
      component: Home
    },
    { path: "/", redirect: { name: "Index" } },
    {
      path: "/help",
      name: "Help"
    },
    {
      path: "/q-entity/by-person",
      name: "Entity Query: By Person",
      component: entityQueryByPerson
    },
    {
      path: "/q-entity/by-office",
      name: "Entity Query: By Office",
      component: entityQueryByOffice
    },
    {
      path: "/q-entity/by-entry",
      name: "Entity Query: By Entry",
      component: entityQueryByEntry
    },
    {
      path: "/q-relation/by-place",
      name: "Relation Query: By Place",
      component: relationQueryByPlace
    },
    {
      path: "/q-relation/kinship",
      name: "Relation Query: By Kinship",
      component: relationQueryByKinship
    },

    {
      path: "/q-relation/association",
      name: "Relation Query: By Association",
      component: relationQueryByAssociation
    },
    {
      path: "/q-relation/by-social-network",
      name: "Relation Query: By Socialnetwork",
      component: relationQueryBySocialNetwork
    },
    {
      path: "/q-relation/two-person",
      name: "Relation Query: Two Person",
      component: relationQueryTwoPerson
    }
    /*
    {
      path: '/visualization/SNA',
      name: 'Visualization: SNA',
      component: visualizationBySNA
    },
    {
      path: '/visualization/GIS',
      name: 'Visualization: people',
      component: visualizationByPeople
    },
    {
      path: '/visualization/Graphs',
      name: 'Visualization: Graphs',
      component: visualizationByGraphs
    },
    */
  ]
});
