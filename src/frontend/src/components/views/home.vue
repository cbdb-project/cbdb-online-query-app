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
  </div>
</template>

<script>
import { isNull } from "@/components/utility/utility-functions.js";
export default {
  name: "Hello"
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
