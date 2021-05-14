<template>
  <div>
    <div class="hello">
      <!--
      <h1>欢迎使用ss中國歷代人物傳記查询</h1>
      -->
      <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
          <h6 class="mb-0">{{ $t("home.introTitle") }}</h6>
        </template>
        <b-card-text class="card-item-title"> </b-card-text>
        <div class="card-item-body px-3" style="text-align:left">
          <p>
            {{ $t("home.introText") }}
          </p>
          <p>
            {{ $t("home.historyText") }}
          </p>
          <p>
            {{ $t("home.introDetail") }}&nbsp;<a
              href="https://projects.iq.harvard.edu/cbdb/home"
              >https://projects.iq.harvard.edu/cbdb/home</a
            >
          </p>
        </div>
      </b-card>
    </div>
    <div class="hello">
      <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
          <h6 class="mb-0">{{ $t("home.introTitleProject") }}</h6>
        </template>
        <b-card-text class="card-item-title"> </b-card-text>
        <div class="card-item-body px-3" style="text-align:left">
          <p>
            {{ $t("home.introTextProject") }}
          </p>
          <p>
            {{ $t("home.helpFileIntro")
            }}<a
              href="https://github.com/yiruka114514/CBDBWebAppGuide/blob/master/CBDBWebGuide.pdf"
              >{{ $t("home.guide") }}</a
            >
          </p>
          <p>
            {{ $t("home.contribution1")
            }}<a href="https://github.com/cbdb-project/cbdb-online-query-app">{{
              $t("home.githubRepo")
            }}</a
            >{{ $t("home.contribution2") }}
          </p>
        </div>
      </b-card>
    </div>
    <div class="hello">
      <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
          <h6 class="mb-0">{{ $t("home.contributors") }}</h6>
        </template>
        <table>
          <tr>
            <td align="center">
              <a href="https://github.com/pleviumtan"
                ><img
                  src="https://avatars.githubusercontent.com/u/39882329?v=4?s=100"
                  width="100px;"
                  alt=""
                /><br /><sub><b>Łøçꝁë Tân</b></sub></a
              ><br /><a href="#design-pleviumtan" title="Design">🎨</a>
              <a
                href="https://github.com/cbdb-project/cbdb-online-query-app/commits?author=pleviumtan"
                title="Code"
                >💻</a
              >
              <a
                href="https://github.com/cbdb-project/cbdb-online-query-app/commits?author=pleviumtan"
                title="Documentation"
                >📖</a
              >
              <a href="#ideas-pleviumtan" title="Ideas, Planning, & Feedback"
                >🤔</a
              >
            </td>
            <td align="center">
              <a href="https://github.com/CasewardBen"
                ><img
                  src="https://avatars.githubusercontent.com/u/48239811?v=4?s=100"
                  width="100px;"
                  alt=""
                /><br /><sub><b>CasewardBen</b></sub></a
              ><br /><a
                href="https://github.com/cbdb-project/cbdb-online-query-app/commits?author=CasewardBen"
                title="Code"
                >💻</a
              >
              <a href="#data-CasewardBen" title="Data">🔣</a>
            </td>
            <td align="center">
              <a href="https://github.com/IceCodeNew"
                ><img
                  src="https://avatars.githubusercontent.com/u/32576256?v=4?s=100"
                  width="100px;"
                  alt=""
                /><br /><sub><b>IceCodeNew</b></sub></a
              ><br /><a
                href="https://github.com/cbdb-project/cbdb-online-query-app/commits?author=IceCodeNew"
                title="Code"
                >💻</a
              >
              <a
                href="#infra-IceCodeNew"
                title="Infrastructure (Hosting, Build-Tools, etc)"
                >🚇</a
              >
              <a href="#maintenance-IceCodeNew" title="Maintenance">🚧</a>
            </td>
            <td align="center">
              <a href="https://github.com/zhangliyuan2013"
                ><img
                  src="https://avatars.githubusercontent.com/u/41323296?v=4?s=100"
                  width="100px;"
                  alt=""
                /><br /><sub><b>zhangliyuan2013</b></sub></a
              ><br /><a
                href="https://github.com/cbdb-project/cbdb-online-query-app/commits?author=zhangliyuan2013"
                title="Code"
                >💻</a
              >
            </td>
            <td align="center">
              <a href="https://github.com/yuetieqi-meow"
                ><img
                  src="https://avatars.githubusercontent.com/u/44973544?v=4?s=100"
                  width="100px;"
                  alt=""
                /><br /><sub><b>yuetieqi-meow</b></sub></a
              ><br /><a
                href="https://github.com/cbdb-project/cbdb-online-query-app/commits?author=yuetieqi-meow"
                title="Code"
                >💻</a
              >
            </td>
          </tr>
        </table>
      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  name: "home"
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.col {
  text-align: left;
  margin: 10px;
}
.hello {
  margin-top: 24px;
}
h1,
h2,
h6 {
  text-align: left;
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
</style>
