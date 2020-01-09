<template>
<div>
  <b-navbar toggleable="lg" variant="faded" type="light" id = "navbar-body">
    <b-navbar-brand href="/">
     <img src="../assets/logo.png" alt="Logo" id = "cbdb-logo" >
     <span style = "position:absolute;left:80px;top:12px">{{$t('navbarTop.title')}}</span>
    </b-navbar-brand>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item href="#">{{$t('navbarTop.help')}}</b-nav-item>
        <b-nav-item href="#" >{{$t('navbarTop.report')}}</b-nav-item>
        <b-nav-item-dropdown :text="$t('navbarTop.lang')" right>
          <b-dropdown-item @click = "changeLang('en')">English</b-dropdown-item>
          <b-dropdown-item @click = "changeLang('zh-cmn-Hant')">中文</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>{{user.name}}</em>
          </template>
          <b-dropdown-item href="#">{{$t('navbarTop.user.profile')}}</b-dropdown-item>
          <b-dropdown-item @click = "logOut">{{$t('navbarTop.user.logOut')}}</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
  </b-navbar>
</div>
</template>

<script>
export default {
  name: 'navbarTop',
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
  },
  methods:{
    changeLang: function(lang){
      if(this.$i18n.locale != lang){
        this.$i18n.locale = lang;
        localStorage.lang = lang
      }
    },
    logOut:function(){

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