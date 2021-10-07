<template>
  <div class="wrapper">
    <div class="mt-3 pt-1 pl-1" style="text-align:left">
      <h5>{{ $t("navbarLeft.entityQueryByPlace") }}</h5>
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
          <!-- 人物地點 -->
          <b-row class="px-3 mb-3">
            <b-card-text class="card-item-title mt-3">
              <span style="font-size:16px">{{ $t("globalTerm.place") }}</span>
            </b-card-text>
          </b-row>
          <b-row class="py-3 my-3">
            <b-col cols="8" style="text-align:left">
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
                  style="margin-top:16px"
                ></select-place>
                <import-place
                  @getPlaceName="handleGetPeoplePlace"
                  name="people"
                  style="margin-top:16px"
                ></import-place>
              </b-button-group>
            </b-col>
          </b-row>
          <b-row class="py-3 my-3">
            <b-col style="text-align:left">
              <b-form-group>
                <b-card-text class="card-item-title">{{
                  $t("relationQueryByPlace.locationType")
                }}</b-card-text>
                <b-form-checkbox-group
                  id="checkbox-group-1"
                  v-model="formData.placeType"
                  :options="qOptions"
                  name="place-type"
                ></b-form-checkbox-group>
              </b-form-group>
            </b-col>
          </b-row>
        </div>
        <b-card-text class="card-item-title pt-3">{{
          $t("globalTerm.alternativeInput")
        }}</b-card-text>
        <div class="card-item-body px-3">
          <!-- 日期 -->
          <!-- 开关 -->
          <b-row class="px-3 mb-3">
            <b-card-text class="card-item-title mt-3">
              <b-form-checkbox
                switch
                size="lg"
                id="checkbox-2"
                v-model="formData.useDate"
                name="checkbox-2"
                value="1"
                unchecked-value="0"
              >
                <span style="font-size:16px">{{ $t("globalTerm.date") }}</span>
              </b-form-checkbox>
            </b-card-text>
          </b-row>
          <!-- 日期类型 -->
          <b-row class="px-3 mb-3" v-if="formData.useDate === '1'">
            <b-col cols="6" style="text-align:left">
              <b-form-radio-group
                id="btn-radios"
                v-model="formData.dateType"
                :options="dateOptions"
                size="sm"
                buttons
                button-variant="outline-primary"
                name="radio-btn-outline"
              ></b-form-radio-group>
            </b-col>
            <b-col cols="6"> </b-col>
          </b-row>
          <!-- 年份输入框 -->
          <b-row
            class="px-3 mb-3"
            v-if="formData.useDate === '1' && formData.dateType !== 'dynasty'"
          >
            <b-col>
              <label for="date-start-time" class="user-input-label"
                >{{ $t("globalTerm.startTime") }}:</label
              >
              <b-form-input
                id="date-start-time"
                v-model="formData.dateStartTime"
                placeholder=""
                :state="validation('dateStartTime')"
                :disabled="formData.useDate === '0' ? true : false"
              ></b-form-input>
              <b-form-invalid-feedback :state="validation('dateStartTime')">
                Invalid year
              </b-form-invalid-feedback>
            </b-col>
            <b-col>
              <label for="date-end-time" class="user-input-label"
                >{{ $t("globalTerm.endTime") }}:</label
              >
              <b-form-input
                id="date-end-time"
                v-model="formData.dateEndTime"
                placeholder=""
                :state="validation('dateEndTime')"
                :disabled="formData.useDate === '0' ? true : false"
              ></b-form-input>
              <b-form-invalid-feedback :state="validation('dateEndTime')">
                Invalid year
              </b-form-invalid-feedback>
            </b-col>
            <b-col cols="4"></b-col>
          </b-row>
          <!-- 朝代输入框 -->
          <b-row
            class="px-3 mb-3"
            v-if="formData.useDate === '1' && formData.dateType === 'dynasty'"
          >
            <b-col>
              <label for="date-start-time" class="user-input-label"
                >{{ $t("globalTerm.startTime") }}:</label
              >
              <b-form-select v-model="formData.dynStart">
                <option v-for="d in dynasty" :key="d.c_dy" :value="d.c_dy">
                  {{
                    $i18n.locale === "zh-cmn-Hant"
                      ? d.c_dynasty_chn
                      : d.c_dynasty
                  }}
                </option>
              </b-form-select>
            </b-col>
            <b-col>
              <label for="date-end-time" class="user-input-label"
                >{{ $t("globalTerm.endTime") }}:</label
              >
              <b-form-select v-model="formData.dynEnd">
                <option v-for="d in dynasty" :key="d.c_dy" :value="d.c_dy">
                  {{
                    $i18n.locale === "zh-cmn-Hant"
                      ? d.c_dynasty_chn
                      : d.c_dynasty
                  }}
                </option>
              </b-form-select>
            </b-col>
            <b-col cols="4"></b-col>
          </b-row>
          <!-- 使用xy坐标 -->
          <b-row class="px-1 py-3 my-3" style="text-align:left">
            <b-col>
              <b-form-checkbox
                id="checkbox-xy"
                v-model="this.formData.useXy"
                size="md"
                name="checkbox-xy"
                value="1"
                unchecked-value="0"
              >
                Use XY Coordinate
              </b-form-checkbox>
            </b-col>
          </b-row>
        </div>
        <b-row class="px-3 mb-3">
          <b-col></b-col>
          <b-col class="p-3">
            <b-button
              href="#"
              variant="primary"
              style="width:100%;margin-top:38px"
              :disabled="isInvalid || isBusy"
              @click="handleSubmit"
            >
              <span v-if="!isBusy">{{ $t("globalTerm.search") }}</span>
              <b-spinner small v-else></b-spinner>
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
    <div class="hello" v-if="result !== undefined">
      <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
          <h6 class="mb-0">{{ $t("globalTerm.resultShow") }}</h6>
        </template>
        <query-result
          name="place-result"
          :items="result.place"
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
  peoplePlaceGetter
} from "@/components/utility/utility-functions.js";
import dynastyJson from "@/assets/dynastyData.json";
import queryResult from "@/components/utility/query-result.vue";
import selectPlace from "@/components/utility/select-place.vue";
import importPlace from "@/components/utility/import-place.vue";
import viewSelected from "@/components/utility/view-selected.vue";
export default {
  name: "entityQueryByPlace",
  components: {
    queryResult,
    selectPlace,
    importPlace,
    viewSelected
  },
  data() {
    return {
      isBusy: false,
      /*表單數據放這裡*/
      formData: {
        //用计算属性
        peoplePlace: [],
        placeType: [],
        dateStartTime: "",
        dateEndTime: "",
        dynStart: "",
        dynEnd: "",
        dateType: "index",
        useDate: "0",
        useXy: "1"
      },
      dynasty: dynastyJson,
      peoplePlaceField: [],
      peoplePlaceTable: [],
      resultField: [
        {
          key: "Name",
          label: "Name",
          sortable: true
        },
        {
          key: "NameChn",
          label: "人物姓名",
          sortable: true
        },
        {
          key: "IndexYear",
          label: "Index Year",
          sortable: true
        },
        {
          key: "AddrName",
          label: "Address Name",
          sortable: true
        },
        {
          key: "AddrChn",
          label: "地址名稱",
          sortable: true
        },
        {
          key: "AssoName",
          label: "Associate Name",
          sortable: true
        },
        {
          key: "AssocChn",
          label: "社會關係人姓名",
          sortable: true
        },
        {
          key: "AssocFirstYear",
          label: "First Year",
          sortable: true
        },
        {
          key: "AssocLastYear",
          label: "Last Year",
          sortable: true
        },
        {
          key: "Category",
          label: "Category",
          sortable: true
        },
        {
          key: "Relation",
          label: "Relation",
          sortable: true
        },
        {
          key: "RelationChn",
          label: "地址關係詳細類別",
          sortable: true
        },
        {
          key: "pX",
          label: "地點經度",
          sortable: true
        },
        {
          key: "pY",
          label: "地點緯度",
          sortable: true
        },
        {
          key: "IndexYearType",
          label: "Index Year Type",
          sortable: true
        },
        {
          key: "IndexYearTypeChn",
          label: "指數年類型",
          sortable: true
        },
        {
          key: "IndexYearTypeCode",
          label: "指數年類型代碼",
          sortable: true
        },
        {
          key: "Notes",
          label: "_______備註______",
          sortable: true
        }
      ],
      result: undefined
    };
  },
  methods: {
    //判斷輸入欄是否為空
    isNull: isNull,
    validation: yearValidation,
    //获取人物籍贯信息
    handleGetPeoplePlace: function(i) {
      peoplePlaceGetter(i, this);
    },
    async handleSubmit() {
      //提交表单的时候先清空原有數據
      this.isBusy = true;
      const res = this.waitForServer(this.formData);
      res.then(
        r => {
          this.result.totalPages = r.data.totalPages;
          this.result.tableData = r.data.data;
          this.isBusy = false;
          if (this.result.totalPages > 1) {
            for (let p = 2; p <= this.result.totalPages; p++)
              this.loadMore("api", p).then(res => console.log(res));
          }
        },
        e => {
          alert("something went wrong...");
          this.isBusy = false;
        }
      );
    },
    //To Do
    waitForServer(query) {
      //sendToServer(query)
      //------模擬服務器響應的東西---------
      return new Promise(function(resolve, reject) {
        setTimeout((success = true) => {
          if (success)
            resolve({ status: "200", data: { totalPages: 5, data: [""] } });
          else reject({ status: "404" });
        }, 1000);
      });
    }
  },
  computed: {
    locationOptions() {
      return [
        { text: "Household addr. only", value: "pAddr" },
        { text: "Entry location addr. only", value: "eAddr" },
        { text: "Household & Entry location addr.", value: "peAddr" }
      ];
    },
    dateOptions() {
      return [
        {
          text: this.$t("globalTerm.indexYear"),
          value: "index"
        },
        {
          text: this.$t("entityQueryByPerson.result.dynasty"),
          value: "dynasty"
        }
      ];
    },
    qOptions() {
      return [
        {
          text: this.$t("relationQueryByPlace.individual"),
          value: "individual"
        },
        { text: this.$t("relationQueryByPlace.entry"), value: "entry" },
        {
          text: this.$t("relationQueryByPlace.association"),
          value: "association"
        },
        {
          text: this.$t("relationQueryByPlace.officePosting"),
          value: "officePosting"
        },
        {
          text: this.$t("relationQueryByPlace.institutional"),
          value: "institutional"
        },
        { text: this.$t("relationQueryByPlace.kinship"), value: "kinship" },
        { text: this.$t("relationQueryByPlace.associate"), value: "associate" }
      ];
    },
    isInvalid() {
      return (
        this.formData.placeType.length === 0 ||
        this.getPeoplePlaceTableId.length === 0 ||
        this.validation("dateEndTime") === false ||
        this.validation("dateStartTime") === false
      );
    },
    getPeoplePlaceTableId() {
      return this.peoplePlaceTable.map(i => i["pId"]);
    }
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
