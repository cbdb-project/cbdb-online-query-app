<template>
  <div id="app">
    <nav-top id = "nav-top"></nav-top>
      <b-row>
        <div class = "inline-element" id = "nav-left">
          <nav-left></nav-left>
        </div>
        <div class = "inline-element" id = "main">
        <router-view/>
        <nav-bottom id = "nav-bottom"></nav-bottom>
        </div>
      </b-row>
  </div>
</template>

<script>
import NavTop from './components/global/nav-top.vue'
import NavLeft from './components/global/nav-left.vue'
import NavBottom from './components/global/nav-bottom.vue'
export default {
  components:
  {
      NavTop,
      NavLeft,
      NavBottom 
  },
  name: 'App'
}
</script>


<style>
#app {
  margin-top:0;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-width:100%;
    /* 主界面背景色 */
  background-color:#F0F2F5;
  padding-bottom:8%
}
#nav-top{
  border-style:solid;
  border-width: 0 0 1px 0;
  border-color:#D4D4D4;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  background-color: #FFFFFF;
  position:fixed;/*固定作用*/
  top:0;
  width:100%;
  height:80px;
  z-index:100
}
#nav-left
{
  position:fixed;
  top:80px;
  width:18%;
  height:100%;
  min-width:200px;
  border-style:solid;
  border-width: 0 1px 0 0;
  border-color:#D4D4D4;
  background-color: #FFFFFF
}
#nav-bottom
{
  padding-top:32px;
}
#main{
  position:relative;
  top:80px;
  left: 8.3%;
  width: 78%;
  margin: 0 auto;
}



</style>
