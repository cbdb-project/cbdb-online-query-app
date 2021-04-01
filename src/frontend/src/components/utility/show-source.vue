<template>
  <div>
    <!-- 來源 頁碼-->
    <b-row class="px-3 mb-3">
      <b-col>
        {{ $t("globalTerm.source") }}: {{ sNameChn
        }}<span v-if="sNameChn && sName">/ {{ sName }}</span>
      </b-col>
      <b-col v-if="sPages"> {{ $t("globalTerm.pages") }}: {{ sPages }} </b-col>
    </b-row>
    <!-- 註 -->
    <b-row class="px-3" v-if="sNotes">
      <b-col>
        {{ $t("globalTerm.notes") }}:
        <p>{{ sNotes }}</p>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: "showSource",
  props: ["sName", "sNameChn", "sPages", "sNotes"]
  //sName:來源-英文
  //sNameChn:來源-中文
  //sPages: 頁碼/id
  //sNotes: 注
};
</script>
