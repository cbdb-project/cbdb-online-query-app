<template>
  <b-nav vertical class="nav-left">
    <b-nav-item exact to = "/index" exact-active-class="active">首頁</b-nav-item>
    <b-nav-item> 
      <b-button v-b-toggle.collapse-a variant="link" class = "text-decoration-none" v-on:click="toogleIcon(1)">
        <!--text-decoration-none -> bootstrap 4.3  -->
        <span class = "collapse-head-text">實體查詢</span>
      </b-button>
      <svg  v-bind:class = "{rotate: isRotate1}"
      t="1575729721049" class="svg-icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2110" width="200" height="200">
          <path d="M334.4384 127.8976c-5.2224 0-10.5472 1.9456-14.4384 5.9392-7.9872 7.9872-7.9872 20.992 0 28.9792l334.6432 334.6432c7.9872 7.9872 7.9872 20.992 0 28.9792L319.8976 861.184c-7.9872 7.9872-7.9872 20.992 0 28.9792 3.9936 3.9936 9.216 5.9392 14.4384 5.9392s10.5472-1.9456 14.4384-5.9392l349.184-349.184c15.9744-15.9744 15.9744-41.8816 0-57.9584l-349.184-349.184c-3.8912-3.8912-9.1136-5.9392-14.336-5.9392z" p-id="2111"></path>
      </svg>
    </b-nav-item>
      <b-collapse id="collapse-a" class="mb-2" :visible = "true">
        <b-nav-item exact to = "/q-entity/by-person" exact-active-class="active">通過人物查詢</b-nav-item>
        <b-nav-item to = "/q-entity/by-office">通過官職查詢</b-nav-item>
        <b-nav-item to = "/q-entity/by-entry">通過入仕途徑查詢</b-nav-item>
        <b-nav-item to = "/q-entity/by-place">通過地點查詢</b-nav-item>
      </b-collapse>
    <b-nav-item> 
      <b-button v-b-toggle.collapse-b variant="link" class = "text-decoration-none" v-on:click="toogleIcon(2)">
        <!--text-decoration-none -> bootstrap 4.3  -->
        <span class = "collapse-head-text">關係查詢</span>
      </b-button>
      <svg  v-bind:class = "{rotate: isRotate2}"
      t="1575729721049" class="svg-icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2110" width="200" height="200">
          <path d="M334.4384 127.8976c-5.2224 0-10.5472 1.9456-14.4384 5.9392-7.9872 7.9872-7.9872 20.992 0 28.9792l334.6432 334.6432c7.9872 7.9872 7.9872 20.992 0 28.9792L319.8976 861.184c-7.9872 7.9872-7.9872 20.992 0 28.9792 3.9936 3.9936 9.216 5.9392 14.4384 5.9392s10.5472-1.9456 14.4384-5.9392l349.184-349.184c15.9744-15.9744 15.9744-41.8816 0-57.9584l-349.184-349.184c-3.8912-3.8912-9.1136-5.9392-14.336-5.9392z" p-id="2111"></path>
      </svg>
    </b-nav-item>
      <b-collapse id="collapse-b" class="mb-2" :visible = "true">
        <b-nav-item to = "/q-relation/kinship">查詢親屬關係</b-nav-item>
        <b-nav-item to = "/q-relation/association">查詢社會關係</b-nav-item>
        <b-nav-item to = "/q-relation/social-network">查詢關係網絡</b-nav-item>
        <b-nav-item to = "/q-relation/two-person">查詢兩人關係</b-nav-item>
      </b-collapse>
    <b-nav-item to = "/visualization">可視化分析</b-nav-item>
    <b-nav-item to = "/statistics">統計分析</b-nav-item>
  </b-nav>
</template>

<script>
export default {
  name: 'navbarLeft',
  data () {
    return {
      /*
        isRotate[n] V型按钮的旋转状态，是否顺时针转90度。当控制折叠的按钮被点选时 isRotate 的值会 toogle
      */
      isRotate1:true,
      isRotate2:true
    }
  },
  methods:{
    //toogleIcon 操作V型按钮的旋转
    toogleIcon: function(idx){
      if(idx == 1)this.isRotate1 = !this.isRotate1
      else if(idx == 2)this.isRotate2 = !this.isRotate2
      
    }
  }
}
</script>
<style scoped>
  .svg-icon{
    padding: 0;
    margin-left:-0.4em;
    width:1em;
    height: 1em;
    transition:all 0.4s
  }
  .rotate{
      transform: rotate(90deg);
      transition: all 0.4s;
  }
  .collapse-head-text
  {
      color:#4D4D4D
  }
  .active{
      background-color: #409EFF;
      color:#FFFFFF;
  }
  .nav-left{
      width:auto;

  }
  .nav-item{
    min-width: 200px;
  }
</style>