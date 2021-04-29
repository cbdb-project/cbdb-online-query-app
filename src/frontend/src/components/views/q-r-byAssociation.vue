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
              <select-relation
                @getRelation="handleGetRelation"
                name="relation"
                style="margin-top:56px"
              >
              </select-relation>
            </b-col>
            <b-col cols="2"> </b-col>
          </b-row>
        </div>
        <b-card-text class="card-item-title pt-3">{{
          $t("globalTerm.alternativeInput")
        }}</b-card-text>
        <div class="card-item-body px-3">
          <!-- 人物地點 -->
          <b-row class="px-3 mb-3">
            <b-card-text class="card-item-title mt-3">
              <b-form-checkbox
                switch
                size="lg"
                id="checkbox-1"
                v-model="formData.usePeoplePlace"
                name="checkbox-1"
                value="1"
                unchecked-value="0"
              >
                <span style="font-size:16px"
                  >{{ $t("globalTerm.person")
                  }}{{ $t("globalTerm.place") }}</span
                >
              </b-form-checkbox>
            </b-card-text>
          </b-row>
          <b-row class="py-3 my-3" v-if="formData.usePeoplePlace === '1'">
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
                <!--
            <import-place @getPlaceName="handleGetPeoplePlace" name="people" style = "margin-top:16px"></import-place>
            -->
              </b-button-group>
            </b-col>
          </b-row>

          <!-- 指數年的api還沒加，先註釋掉 -->
          <!--
        <b-row class = "px-3 mb-3">
          <b-card-text class = "card-item-title mt-3">
            <b-form-checkbox switch size="lg" id="checkbox-2" v-model= "formData.indexYear" name="checkbox-2"
              value="t" unchecked-value="f">
              <span style="font-size:16px">{{$t('entityQueryByOffice.indexYearRange')}}</span>
            </b-form-checkbox>  
          </b-card-text> 
        </b-row>
        <b-row class = "px-3 mb-3"  v-if="formData.indexYear==='t'">
          <b-col>
            <label for="index-start-time" class = "user-input-label">{{$t('globalTerm.startTime')}}:</label>
            <b-form-input id="index-start-time" v-model="formData.indexStartTime" placeholder="" 
              :state="validation('indexStartTime')" :disabled="formData.indexYear==='f'?true:false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexStartTime')">
                Invalid year 
              </b-form-invalid-feedback>
          </b-col>
          <b-col>
             <label for="index-end-time" class = "user-input-label">{{$t('globalTerm.endTime')}}:</label>
             <b-form-input id="index-end-time" v-model="formData.indexEndTime" placeholder="" 
             :state="validation('indexEndTime')" :disabled="formData.indexYear==='f'?true:false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexEndTime')">
                Invalid year 
              </b-form-invalid-feedback>
           </b-col>
           <b-col cols="4"></b-col>
        </b-row>
        --></div>
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
        <b-row v-if="isBusy">
          <b-col>
            <warning-text :text="this.$t('globalTerm.searchTimeLong')">
            </warning-text>
          </b-col>
        </b-row>
      </b-card>
    </div>
    <div class="hello" v-if="result !== undefined">
      <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
          <h6 class="mb-0">{{ $t("globalTerm.resultShow") }}</h6>
        </template>
        <query-result
          name="ass-result"
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
  peoplePlaceGetter,
  relationGetter
} from "@/components/utility/utility-functions";
import queryResult from "@/components/utility/query-result.vue";
import selectRelation from "@/components/utility/select-relationship.vue";
import selectPlace from "@/components/utility/select-place.vue";
import viewSelected from "@/components/utility/view-selected.vue";
import warningText from "@/components/utility/warning-text.vue";
//import importPlace from '@/components/utility/import-place.vue'

export default {
  name: "relationQueryByAssociation",
  components: {
    queryResult,
    selectRelation,
    selectPlace,
    viewSelected,
    warningText
    //importPlace
  },
  data() {
    return {
      //控制加載標誌的出現
      isBusy: false,
      /*表單數據放這裡*/
      formData: {
        place: [],
        association: [],
        usePeoplePlace: 0,
        useXy: 1,
        broad: 0
      },
      //後端傳回來的數據放這裡
      peoplePlaceTable: [],
      peoplePlaceField: [],
      relationTable: [],
      relationField: [],
      resultField: [
        {
          key: "pId",
          label: "人物ID",
          sortable: true
        },
        {
          key: "pName",
          label: "Person Name",
          sortable: true
        },
        {
          key: "pNameChn",
          label: "人物姓名",
          sortable: true
        },
        {
          key: "aId",
          label: "社會關係人ID",
          sortable: true
        },
        {
          key: "aName",
          label: "Associate Name",
          sortable: true
        },
        {
          key: "aNameChn",
          label: "關係人姓名",
          sortable: true
        },
        {
          key: "pIndexYear",
          label: "人物指數年",
          sortable: true
        },
        {
          key: "pSex",
          label: "人物性別",
          sortable: true
        },
        {
          key: "aIndexYear",
          label: "關係人指數年",
          sortable: true
        },
        {
          key: "aSex",
          label: "關係人性別",
          sortable: true
        },
        {
          key: "pAddrID",
          label: "人物地點ID",
          sortable: true
        },
        {
          key: "pAddrName",
          label: "Address Name",
          sortable: true
        },
        {
          key: "pAddrNameChn",
          label: "人物地點名",
          sortable: true
        },
        {
          key: "pX",
          label: "人物地點經度",
          sortable: true
        },
        {
          key: "pY",
          label: "人物地點緯度",
          sortable: true
        },
        {
          key: "aAddrID",
          label: "關係人地點ID",
          sortable: true
        },
        {
          key: "aAddrName",
          label: "Associate Address Name",
          sortable: true
        },
        {
          key: "aAddrNameChn",
          label: "關係人地點名",
          sortable: true
        },
        {
          key: "aX",
          label: "關係人地點經度",
          sortable: true
        },
        {
          key: "aY",
          label: "關係人地點緯度",
          sortable: true
        },
        {
          key: "distance",
          label: "地點距離",
          sortable: true
        },
        {
          key: "p_xy_count",
          label: "結果中同一地點人數",
          sortable: true
        },
        {
          key: "a_xy_count",
          label: "結果中與關係人同一地點人數",
          sortable: true
        },

        {
          key: "pKinshipRelation",
          label: "Kinship Relation",
          sortable: true
        },
        {
          key: "pKinshipRelationChn",
          label: "親屬關係",
          sortable: true
        },
        {
          key: "pKinName",
          label: "Kin Name",
          sortable: true
        },
        {
          key: "pKinNameChn",
          label: "親屬姓名",
          sortable: true
        },
        {
          key: "aKinshipRelation",
          label: "Associate's Kinship Relation",
          sortable: true
        },
        {
          key: "aKinshipRelationChn",
          label: "關係人親屬關係",
          sortable: true
        },
        {
          key: "aKinName",
          label: "Associate's Kin's Name",
          sortable: true
        },
        {
          key: "aKinNameChn",
          label: "關係人親屬之姓名",
          sortable: true
        },
        {
          key: "a_xy_count",
          label: "結果中與關係人同一地點人數",
          sortable: true
        }
      ],
      result: undefined
    };
  },
  methods: {
    isNull: isNull,
    validation: yearValidation,
    //获取查询的人物
    handleGetPerson: function(selectedPerson) {},
    handleGetPeoplePlace: function(i) {
      peoplePlaceGetter(i, this);
    },
    handleGetRelation: function(i) {
      //console.log(i)
      relationGetter(i, this);
    },
    async handleSubmit() {
      //提交表单的时候先清空原有數據
      this.isBusy = true;
      let vm = this;
      let f = vm.formData;
      //console.log(vm.getRelationTableId)
      let data = {
        association: vm.getRelationTableId,
        place: vm.getPeoplePlaceTableId,
        usePeoplePlace: f.usePeoplePlace,
        useXy: f.useXy,
        broad: f.broad
      };
      data = JSON.stringify(data);
      let query = `${vm.$store.state.global.apiAddress}query_associates?RequestPlayload=${data}`;
      //console.log(query)
      this.axios
        .post(query)
        .then(
          res => {
            console.log(res.data.data);
            vm.result = {};
            vm.result.ass = res.data.data;
          },
          error => {
            alert("Network Error...");
          }
        )
        .finally(() => {
          vm.isBusy = false;
        });
    }
  },
  computed: {
    isInvalid() {
      return this.relationTable.length === 0;
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
