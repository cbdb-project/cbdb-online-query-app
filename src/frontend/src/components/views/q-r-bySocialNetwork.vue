<template>
  <div class="wrapper">
    <div class="mt-3 pt-1 pl-1" style="text-align:left">
      <h5></h5>
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
          <!-- 人物 -->
          <b-row class="py-3 my-3">
            <b-col cols="8" style="text-align:left">
              <b-card-text class="card-item-title">{{
                $t("globalTerm.person")
              }}</b-card-text>
              <b-card>
                <b-row class="pl-3" style="text-align:center">
                  <b-col>
                    <span
                      v-if="this.personTable.length == 0"
                      style="line-height:31px"
                      >**{{ $t("globalTerm.all") }}**</span
                    >
                    <span v-else
                      >{{ personTable[0]["personNameCh"] }}
                      <span v-if="this.personTable.length > 1"
                        >及另外{{ this.personTable.length - 1 }}個人物</span
                      >
                    </span>
                    <view-selected
                      name="person"
                      :fields="this.personField"
                      :items="this.personTable"
                      @update:items="val => (this.personTable = val)"
                    ></view-selected>
                  </b-col>
                </b-row>
              </b-card>
            </b-col>
            <b-col cols="4" style="text-align:left">
              <select-person
                @getPersonName="handleGetPerson"
                selectMode="multi"
                style="margin-top:56px"
              >
              </select-person>
            </b-col>
          </b-row>
          <!-- 人物地點 -->
          <b-row class="py-3 my-3">
            <b-col cols="8" style="text-align:left">
              <b-card-text class="card-item-title">{{
                $t("globalTerm.place")
              }}</b-card-text>
              <b-card>
                <b-row class="pl-3" style="text-align:center">
                  <b-col>
                    <span
                      v-if="this.peoplePlaceTable.length == 0"
                      style="line-height:31px"
                      >**{{ $t("globalTerm.all") }}**</span
                    >
                    <span v-else
                      >{{ peoplePlaceTable[0]["pNameChn"] }}
                      <span v-if="this.peoplePlaceTable.length > 1"
                        >及另外{{ peoplePlaceTable.length - 1 }}個地點</span
                      >
                    </span>
                    <view-selected
                      name="peoplePlace"
                      :fields="this.peoplePlaceField"
                      :items="this.peoplePlaceTable"
                      @update:items="val => (this.peoplePlaceTable = val)"
                    ></view-selected>
                  </b-col>
                </b-row>
              </b-card>
            </b-col>
            <b-col cols="4" style="text-align:left">
              <b-button-group>
                <select-place
                  @getPlaceName="handleGetPeoplePlace"
                  name="people"
                  style="margin-top:56px"
                ></select-place>
              </b-button-group>
            </b-col>
          </b-row>
          <!-- 社會關係 -->
          <b-row class="py-3 my-3">
            <b-col cols="8" style="text-align:left">
              <b-card-text class="card-item-title">{{
                $t("globalTerm.association")
              }}</b-card-text>
              <b-card>
                <b-row class="pl-3" style="text-align:center">
                  <b-col>
                    <span
                      v-if="this.relationTable.length === 0"
                      style="line-height:31px"
                      >**{{ $t("globalTerm.all") }}**</span
                    >
                    <span v-else
                      >{{ this.relationTable[0]["aNameChn"] }}
                      <span v-if="this.relationTable.length > 1"
                        >及另外{{ this.relationTable.length - 1 }}種關係</span
                      >
                    </span>
                    <view-selected
                      name="relation"
                      :fields="this.relationField"
                      :items="this.relationTable"
                      @update:items="val => (this.relationTable = val)"
                    ></view-selected>
                  </b-col>
                </b-row>
              </b-card>
            </b-col>
            <b-col cols="2" style="text-align:left">
              <select-relation-network
                @getRelation="handleGetRelation"
                name="relation"
                style="margin-top:56px"
              >
              </select-relation-network>
            </b-col>
          </b-row>
          <b-card-text class="card-item-title pt-3" style="text-align:left"
            >Search Options</b-card-text
          >
          <b-row class="pb-3 mb-3">
            <b-col cols="4">
              <label for="index-end-time" class="user-input-label">
                {{ $t("relationQueryBySocialNetwork.maxNodeDistance") }}
              </label>
              <b-form-input
                id="index-end-time"
                v-model="formData.endTime"
                placeholder=""
                :state="validation('indexEndTime')"
                :disabled="false"
              ></b-form-input>
              <b-form-invalid-feedback :state="validation('indexEndTime')">
                Invalid number
              </b-form-invalid-feedback>
            </b-col>
            <b-col cols="4">
              <label for="index-end-time" class="user-input-label">
                {{ $t("relationQueryBySocialNetwork.maxLoop") }}
              </label>
              <b-form-input
                id="index-end-time"
                v-model="formData.endTime"
                placeholder=""
                :state="validation('indexEndTime')"
                :disabled="false"
              ></b-form-input>
              <b-form-invalid-feedback :state="validation('indexEndTime')">
                Invalid number
              </b-form-invalid-feedback>
            </b-col>
          </b-row>
          <b-row class="py-3 mb-3">
            <b-col cols="3" style="text-align:left">
              <b-card-text class="card-item-title">{{
                $t("globalTerm.gen")
              }}</b-card-text>
              <b-card-text class="card-item-title mt-3 ml-3">
                <b-form-checkbox
                  switch
                  size="lg"
                  id="checkbox-2"
                  v-model="formData.includeMale"
                  name="checkbox-2"
                  value="1"
                  unchecked-value="0"
                >
                  <span style="font-size:16px">{{
                    $t("globalTerm.male")
                  }}</span>
                </b-form-checkbox>
              </b-card-text>
              <b-card-text class="card-item-title mt-3 ml-3">
                <b-form-checkbox
                  switch
                  size="lg"
                  id="checkbox-3"
                  v-model="formData.includeFemale"
                  name="checkbox-3"
                  value="1"
                  unchecked-value="0"
                >
                  <span style="font-size:16px">{{
                    $t("globalTerm.female")
                  }}</span>
                </b-form-checkbox>
              </b-card-text>
            </b-col>
            <b-col cols="6"> </b-col>
          </b-row>
        </div>
        <b-card-text class="card-item-title pt-3">{{
          $t("globalTerm.alternativeInput")
        }}</b-card-text>
        <div class="card-item-body px-3">
          <b-row class="px-3 mb-3">
            <b-card-text class="card-item-title mt-3">
              <b-form-checkbox
                switch
                size="lg"
                id="checkbox-4"
                v-model="formData.includeKinship"
                name="checkbox-4"
                value="1"
                unchecked-value="0"
              >
                <span style="font-size:16px">{{
                  $t("relationQueryBySocialNetwork.includeKinship")
                }}</span>
              </b-form-checkbox>
            </b-card-text>
          </b-row>
          <b-row class="px-3 mb-3" v-if="formData.includeKinship === '1'">
            <b-col cols="8" style="text-align:left">
              <b-form-radio-group
                id="btn-radios"
                v-model="formData.kinship.kinshipType"
                :options="kinshipOptions"
                size="sm"
                buttons
                button-variant="outline-primary"
                name="radio-btn-outline"
              ></b-form-radio-group>
            </b-col>
            <b-col cols="4"> </b-col>
          </b-row>
          <b-row
            class="px-3 mb-3"
            v-if="
              formData.includeKinship === '1' &&
                formData.kinship.kinshipType === 0
            "
          >
            <b-col>
              <label for="max-ancestor-gen" class="user-input-label"
                >{{ $t("relationQueryByKinship.maxAncestorGen") }}:</label
              >
              <b-form-input
                id="max-ancestor-gen"
                v-model="formData.MAncGen"
                placeholder=""
                :state="validation('indexStartTime')"
                :disabled="false"
              ></b-form-input>
              <b-form-invalid-feedback :state="validation('indexStartTime')">
                Invalid number
              </b-form-invalid-feedback>
            </b-col>
            <b-col>
              <label for="max-descend-gen" class="user-input-label"
                >{{ $t("relationQueryByKinship.maxDescendGen") }}:</label
              >
              <b-form-input
                id="max-descend-gen"
                v-model="formData.MDecGen"
                placeholder=""
                :state="validation('indexEndTime')"
                :disabled="false"
              ></b-form-input>
              <b-form-invalid-feedback :state="validation('indexEndTime')">
                Invalid number
              </b-form-invalid-feedback>
            </b-col>
            <b-col>
              <label for="max-collaternal-links" class="user-input-label"
                >{{ $t("relationQueryByKinship.maxCollaternalLinks") }}:</label
              >
              <b-form-input
                id="max-collaternal-links"
                v-model="formData.MColLink"
                placeholder=""
                :state="validation('indexStartTime')"
                :disabled="false"
              ></b-form-input>
              <b-form-invalid-feedback :state="validation('indexStartTime')">
                Invalid number
              </b-form-invalid-feedback>
            </b-col>
            <b-col>
              <label for="max-marriage-links" class="user-input-label"
                >{{ $t("relationQueryByKinship.maxMarriageLinks") }}:</label
              >
              <b-form-input
                id="max-marriage-links"
                v-model="formData.MMarLink"
                placeholder=""
                :state="validation('indexEndTime')"
                :disabled="false"
              ></b-form-input>
              <b-form-invalid-feedback :state="validation('indexEndTime')">
                Invalid number
              </b-form-invalid-feedback>
            </b-col>
          </b-row>
          <b-row
            class="px-3 my-3"
            style="text-align:left"
            v-if="formData.includeKinship === '1'"
          >
            <b-col>
              <b-form-checkbox
                id="checkbox-kinarg"
                v-model="this.formData.kinarg"
                size="md"
                name="checkbox-kinarg"
                value="1"
                unchecked-value="0"
              >
                使用親屬的距離參數
              </b-form-checkbox>
            </b-col>
          </b-row>
          <b-row class="px-3 mb-3">
            <b-card-text class="card-item-title mt-3">
              <b-form-checkbox
                switch
                size="lg"
                id="checkbox-1"
                v-model="formData.indexYear"
                name="checkbox-1"
                value="t"
                unchecked-value="f"
              >
                <span style="font-size:16px">{{
                  $t("globalTerm.indexYear")
                }}</span>
              </b-form-checkbox>
            </b-card-text>
          </b-row>
          <b-row class="px-3 mb-3" v-if="formData.indexYear === 't'">
            <b-col>
              <label for="index-start-time" class="user-input-label"
                >{{ $t("globalTerm.startTime") }}:</label
              >
              <b-form-input
                id="index-start-time"
                v-model="formData.startTime"
                placeholder=""
                :state="validation('indexStartTime')"
                :disabled="formData.indexYear === 'f' ? true : false"
              ></b-form-input>
              <b-form-invalid-feedback :state="validation('indexStartTime')">
                Invalid year
              </b-form-invalid-feedback>
            </b-col>
            <b-col>
              <label for="index-end-time" class="user-input-label"
                >{{ $t("globalTerm.endTime") }}:</label
              >
              <b-form-input
                id="index-end-time"
                v-model="formData.endTime"
                placeholder=""
                :state="validation('indexEndTime')"
                :disabled="formData.indexYear === 'f' ? true : false"
              ></b-form-input>
              <b-form-invalid-feedback :state="validation('indexEndTime')">
                Invalid year
              </b-form-invalid-feedback>
            </b-col>
            <b-col cols="4"></b-col>
          </b-row>
        </div>
        <b-row class="px-3 mb-3">
          <b-col></b-col>
          <b-col class="p-3">
            <a
              v-b-tooltip.hover
              :title="isInvalid ? $t('globalTerm.invalidInput') : ''"
            >
              <b-button
                href="#"
                variant="primary"
                style="width:100%;margin-top:16px"
                :disabled="isInvalid || isBusy"
                @click="handleSubmit"
              >
                <span v-if="!isBusy">{{ $t("globalTerm.search") }}</span>
                <b-spinner small v-else></b-spinner>
              </b-button>
            </a>
          </b-col>
          <b-col></b-col>
        </b-row>
      </b-card>
    </div>
    <div class="hello" v-if="result !== undefined">
      <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
          <h6 class="mb-0">{{ $t("globalTerm.resultShow") }}</h6>
        </template>
        <query-result
          name="network-result"
          :items="result.ass"
          :fields="resultField"
        ></query-result>
      </b-card>
    </div>
  </div>
</template>

<script>
import {
  isNull,
  yearValidation,
  personGetter,
  peoplePlaceGetter,
  relationGetter,
  kinshipOptions
} from "@/components/utility/utility-functions.js";
import queryResult from "@/components/utility/query-result.vue";
import selectRelationNetwork from "@/components/utility/select-relation-network.vue";
import selectPerson from "@/components/utility/select-person.vue";
import selectPlace from "@/components/utility/select-place.vue";
import viewSelected from "@/components/utility/view-selected.vue";
export default {
  name: "relationQueryBySocialNetwork",
  components: {
    queryResult,
    selectRelationNetwork,
    selectPerson,
    selectPlace,
    viewSelected
    //importPlace
  },
  data() {
    return {
      //控制加載標誌的出現
      isBusy: false,
      /*表單數據放這裡*/
      formData: {
        person: [],
        place: [],
        association: [],
        includeKinship: "0",
        kinship: {
          kinshipType: 0
        },
        //usePeoplePlace:"0",
        includeMale: "1",
        includeFemale: "1"
      },
      //後端傳回來的數據放這裡
      result: undefined,
      peoplePlaceTable: [],
      peoplePlaceField: [],
      relationTable: [],
      relationField: [],
      personField: [],
      personTable: []
    };
  },
  methods: {
    //判斷輸入欄是否為空
    isNull: isNull,
    validation: yearValidation,
    //获取查询的人物
    handleGetPerson: function(i) {
      personGetter(i, this);
    },
    handleGetPeoplePlace: function(i) {
      peoplePlaceGetter(i, this);
    },
    handleGetRelation: function(i) {
      relationGetter(i, this);
    },
    async handleSubmit() {
      //提交表单的时候先清空原有數據
      this.personInfo = {};
      this.isBusy = true;
      //加了async修饰符res变成结果？
      const res = this.waitForServer(this.formData);
      res.then(
        r => {
          this.personInfo = r.data;
          this.isBusy = false;
        },
        e => {
          alert("something went wrong...");
          this.isBusy = false;
        }
      );
    },
    waitForServer(query) {
      //sendToServer(query)
      //------模擬服務器響應的東西---------
      return new Promise(function(resolve, reject) {
        setTimeout((success = true) => {
          if (success) resolve({ status: "200", data: {} });
          else reject({ status: "404" });
        }, 3000);
      });
    }
  },
  computed: {
    isInvalid() {
      return this.isNull("personId") == true;
    },
    kinshipOptions: kinshipOptions,
    getPersonTableId() {
      return this.personTable.map(i => i["personId"]);
    },
    getPeoplePlaceTableId() {
      return this.peoplePlaceTable.map(i => i["pId"]);
    },
    getRelationTableId() {
      return this.relationTable.map(i => i["aId"]);
    }
  },
  watch: {}
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
