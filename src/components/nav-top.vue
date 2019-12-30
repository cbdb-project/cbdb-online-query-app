<template>
<div>
  <b-navbar toggleable="lg" variant="faded" type="light" id = "navbar-body">
    <b-navbar-brand href="/">
     <img src="../assets/logo.png" alt="Logo" id = "cbdb-logo" >
     <span style = "position:absolute;left:80px;top:12px">CBDB Web 查詢系統</span>
    </b-navbar-brand>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item href="#">幫助</b-nav-item>
        <b-nav-item href="#" >報告</b-nav-item>
        <b-nav-item-dropdown text="語言" right>
          <b-dropdown-item href="#">English</b-dropdown-item>
          <b-dropdown-item href="#">中文</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>{{user.name}}</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
  </b-navbar>
</div>
</template>

<script>
export default {
  name: 'NavbarTop',
  data () {
    return {
    }
  },
  computed:{
    lang(){
      switch(this.$store.state.lang) {
          //
      } 
      return 'Language'
    },
    user(){
      return this.$store.state.user
    }
  }
}
</script>

<style scoped>
  #cbdb-logo{
    position: absolute;
    top:0;
    left:8px;
    width:56px;
    height: 56px;
    
  }
  #navbar-body{
    margin-top:10px;
  }

</style>