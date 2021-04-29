<template>
  <div class="wrapper">
    <div class="mt-3 pt-1 pl-1" style="text-align:left">
      <h5>{{ $t("navbarLeft.entityQueryByPerson") }}</h5>
    </div>
    <div class="hello">
      <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
          <h6 class="mb-0">{{ $t("globalTerm.queryInput") }}</h6>
        </template>
        <b-card-text class="card-item-title">{{
          $t("globalTerm.requiredInput")
        }}</b-card-text>
        <div class="card-item-body px-3">
          <b-row class="p-3 mt-3">
            <b-col style="text-align:left">
              <b-card-text class="card-item-title">{{
                $t("selectPerson.personName")
              }}</b-card-text>
              <b-form-input
                id="person-name"
                v-model="formData.personName"
              ></b-form-input>
            </b-col>
          </b-row>
        </div>
        <!--
      <b-alert show variant="warning"  class = "px-3 py-2 mx-3" style = "width:66%">{{$t('entityQueryByPerson.checkRemind')}}</b-alert>
      -->
        <b-row class="px-3 mb-3">
          <b-col></b-col>
          <b-col class="p-3">
            <b-button
              variant="primary"
              style="width:100%;margin-top:16px"
              :disabled="formData.personName.length === 0"
            >
              <a
                v-b-tooltip.hover
                :href="
                  'https://cbdb.fas.harvard.edu/cbdbapi/person.php?name=' +
                    formData.personName
                "
                target="_blank"
              >
                <span>{{ $t("globalTerm.search") }}</span>
              </a>
            </b-button>
          </b-col>
          <b-col></b-col>
        </b-row>
        <!--
      <template v-slot:footer>
        <em>Footer Slot</em>
      </template>
      -->
      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  name: "entityQueryByPerson",
  data() {
    return {
      //控制加載標誌的出現
      isBusy: false,
      /*表單數據放這裡*/
      formData: {
        personName: ""
      }
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.user-input-label {
  text-align: left;
  width: 100%;
}
.query-condition-button {
  width: 224px;
  margin: 6px 0;
}
.card-item-body {
  text-align: center;
  margin: 6px 0;
}
.bread-crumb {
  width: 30%;
  background-color: transparent;
}
.hello {
  margin-top: 24px;
  text-align: left;
}
.card-item-title {
  font-weight: bold;
}
</style>
