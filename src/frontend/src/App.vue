<template>
  <div id="app">
    <nav-top id="nav-top"></nav-top>
    <div id="nav-left">
      <nav-left></nav-left>
    </div>
    <div class="main-wrapper">
      <div id="main">
        <router-view />
        <nav-bottom id="nav-bottom"></nav-bottom>
      </div>
    </div>
  </div>
</template>

<script>
import NavTop from "./components/global/nav-top.vue";
import NavLeft from "./components/global/nav-left.vue";
import NavBottom from "./components/global/nav-bottom.vue";
export default {
  components: {
    NavTop,
    NavLeft,
    NavBottom
  },
  name: "App"
};
</script>

<style>
:root {
  --myGap: 32px;
}
#app {
  margin-top: 0;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-width: 100%;
  padding-bottom: 8%;
}
#nav-top {
  border-style: solid;
  border-width: 0 0 1px 0;
  border-color: #d4d4d4;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  background-color: #ffffff;
  position: fixed; /*固定作用*/
  top: 0;
  width: 100%;
  height: 80px;
  z-index: 100;
}
#nav-left {
  position: fixed;
  width: 200px;
  height: 100vh;
  border-style: solid;
  border-width: 0 1px 0 0;
  border-color: #d4d4d4;
  background-color: #ffffff;
}
#nav-bottom {
  padding-top: 32px;
}
#main {
  position: relative;
  top: 80px;
  width: calc((100vw - 200px) - var(--myGap) * 2);
  min-width: 500px;
  margin: 0 auto;
}
.main-wrapper {
  position: absolute;
  display: flex;
  left: 200px;
  margin-left: var(--myGap);
}
</style>
