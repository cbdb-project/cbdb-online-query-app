<template>
  <div>
    <b-navbar toggleable="lg" variant="faded" type="light" id="navbar-body">
      <b-navbar-brand href="/">
        <img src="../../assets/logo.png" alt="Logo" id="cbdb-logo" />
        <span id="cbdb-title">{{ $t("navbarTop.title") }}</span>
      </b-navbar-brand>
      <!-- Right aligned nav items -->
      <b-nav id="nav-list">
        <b-nav-item
          href="https://github.com/yiruka114514/CBDBWebAppGuide/blob/master/CBDBWebGuide.pdf"
          target="_blank"
          >{{ $t("navbarTop.help") }}</b-nav-item
        >
        <b-nav-item
          href="https://github.com/cbdb-project/cbdb-online-query-app/issues"
          target="_blank"
          >{{ $t("navbarTop.report") }}</b-nav-item
        >
        <b-nav-item-dropdown :text="$t('navbarTop.lang')" right>
          <b-dropdown-item @click="changeLang('en')">English</b-dropdown-item>
          <b-dropdown-item @click="changeLang('zh-cmn-Hant')"
            >中文</b-dropdown-item
          >
        </b-nav-item-dropdown>
        <!-- 用戶資訊
        <b-nav-item-dropdown right>
          <template v-slot:button-content>
            <em>{{user.name}}</em>
          </template>
          <b-dropdown-item href="#">{{$t('navbarTop.user.profile')}}</b-dropdown-item>
          <b-dropdown-item @click = "logOut">{{$t('navbarTop.user.logOut')}}</b-dropdown-item>
        </b-nav-item-dropdown>
        -->
      </b-nav>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "navbarTop",
  data() {
    return {};
  },
  computed: {
    user() {
      return this.$store.state.local.user;
    }
  },
  methods: {
    changeLang: function(lang) {
      if (this.$i18n.locale != lang) {
        this.$i18n.locale = lang;
        localStorage.lang = lang;
      }
    },
    logOut: function() {}
  }
};
</script>

<style scoped>
#cbdb-logo {
  width: 56px;
  height: 56px;
}
#navbar-body {
  display: flex;
  justify-content: space-between;
  align-content: center;
}
#cbdb-title {
  line-height: 56px;
  padding: 15px;
}
#nav-list {
  display: flex;
  justify-content: flex-start;
}
</style>
