<template>
<div class = "wrapper">
  <div class = "mt-3 pt-1 pl-1" style = "text-align:left">
  <h5>{{$t('navbarLeft.relationQueryByKinship')}}</h5>
  </div>
  <div class="hello">
    <b-card header-tag="header" footer-tag="footer">
      <template v-slot:header>
        <h6 class="mb-0">{{$t('globalTerm.queryInput')}}</h6>
      </template>
      <b-card-text class = "card-item-title">{{$t('globalTerm.requiredInput')}}</b-card-text>             
      <div class  = "card-item-body px-3">
        <b-row class = "py-3 my-3">
          <b-col cols="8" style = "text-align:left">
            <b-card-text class = "card-item-title">{{$t('globalTerm.person')}}</b-card-text>    
            <b-card>
              <b-row class="pl-3" style = "text-align:center">
                <b-col>
                  <span v-if="this.personTable.length==0" style = "line-height:31px">**{{$t('globalTerm.all')}}**</span>
                  <span v-else>{{personTable[0]['personNameCh']}}
                    <span v-if="this.personTable.length>1">及另外{{this.personTable.length-1}}個人物</span>
                  </span>
                  <view-selected name="person" :fields="this.personField" :items="this.personTable" @update:items="val=>this.personTable=val"></view-selected>
                </b-col>
              </b-row>
            </b-card>
          </b-col>
          <b-col cols="4" style = "text-align:left">
            <select-person @getPersonName="handleGetPerson" selectMode='multi' style="margin-top:56px">
            </select-person>
          </b-col>
        </b-row>
        <b-row class = "mb-3 pb-3">
           <b-col cols="3">
             <label for="max-loop" class = "user-input-label">{{$t('relationQueryByKinship.maxLoop')}}:
               <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
              </label>
             <b-form-input id="max-loop" v-model="formData.MLoop" placeholder="" 
             :state="validation('indexEndTime')" :disabled="false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexEndTime')">
                Invalid number
              </b-form-invalid-feedback>
           </b-col>
        </b-row>
        <b-row class = "my-3">
          <b-col cols="8" style = "text-align:left">
            <b-form-radio-group
              id="btn-radios"
              v-model="formData.kinshipType"
              :options="kinshipOptions"
              size="sm"
              buttons
              button-variant="outline-primary"
              name="radio-btn-outline"
            ></b-form-radio-group>
          </b-col>
          <b-col cols="4">
          </b-col>
        </b-row>
        <b-row class = "px-3 mb-3"  v-if="formData.kinshipType===0">
          <b-col>
            <label for="max-ancestor-gen" class = "user-input-label">{{$t('relationQueryByKinship.maxAncestorGen')}}:</label>
            <b-form-input id="max-ancestor-gen" v-model="formData.MAncGen" placeholder="" 
              :state="validation('indexStartTime')" :disabled="false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexStartTime')">
                Invalid number
              </b-form-invalid-feedback>
            </b-col>
          <b-col>
             <label for="max-descend-gen" class = "user-input-label">{{$t('relationQueryByKinship.maxDescendGen')}}:</label>
             <b-form-input id="max-descend-gen" v-model="formData.MDecGen" placeholder="" 
             :state="validation('indexEndTime')" :disabled="false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexEndTime')">
                Invalid number
              </b-form-invalid-feedback>
           </b-col>
          <b-col>
            <label for="max-collaternal-links" class = "user-input-label">{{$t('relationQueryByKinship.maxCollaternalLinks')}}:</label>
            <b-form-input id="max-collaternal-links" v-model="formData.MColLink" placeholder="" 
              :state="validation('indexStartTime')" :disabled="false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexStartTime')">
                Invalid number
              </b-form-invalid-feedback>
            </b-col>
          <b-col>
             <label for="max-marriage-links" class = "user-input-label">{{$t('relationQueryByKinship.maxMarriageLinks')}}:</label>
             <b-form-input id="max-marriage-links" v-model="formData.MMarLink" placeholder="" 
             :state="validation('indexEndTime')" :disabled="false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexEndTime')">
                Invalid number 
              </b-form-invalid-feedback>
           </b-col>
        </b-row>
      </div>
      <!--
      <b-alert show variant="warning"  class = "px-3 py-2 mx-3" style = "width:66%">{{$t('entityQueryByPerson.checkRemind')}}</b-alert>
      -->
      <b-row class = "px-3 mb-3">
        <b-col></b-col>
        <b-col class = "p-3">
          <a v-b-tooltip.hover  :title="isInvalid?$t('globalTerm.invalidInput'):''">
            <b-button href="#" variant="primary" 
              style = "width:100%;margin-top:16px" :disabled="isInvalid||isBusy"
              @click="handleSubmit">
              <span v-if="!isBusy">{{$t('globalTerm.search')}}</span>
              <b-spinner small v-else></b-spinner>
            </b-button>
          </a>
        </b-col>
        <b-col></b-col>
      </b-row>    
    </b-card>
  </div>
  <div class="hello" v-if="result!==undefined">
    <b-card header-tag="header" footer-tag="footer">
      <template v-slot:header>
          <h6 class="mb-0">{{$t('globalTerm.resultShow')}}</h6>
      </template>
      <query-result name="kin-result" :items="result.kins" :fields="resultField"></query-result>
    </b-card>
  </div>
</div>
</template>

<script>
import {
  isNull,
  yearValidation,
  personGetter,
  kinshipOptions
} from '@/components/utility/utility-functions.js'
import queryResult from '@/components/utility/query-result.vue'
import selectPerson from '@/components/utility/select-person.vue'
import viewSelected from '@/components/utility/view-selected.vue'
//開發用的假數據
export default {
  name: 'relationQueryByKinship',
  components: {
    queryResult,
    selectPerson,
    viewSelected
  },
  data() {
    return {
      //控制加載標誌的出現
      isBusy: false,
      /*表單數據放這裡*/
      formData: {
        //用计算属性
        person: [],
        //MLoop太大會導致查詢時間非常長長長長長
        MLoop: 5,
        MAncGen: 1,
        MDecGen: 1,
        MColLink: 1,
        MMarLink: 1,
        kinshipType: 1,
      },
      personField: [],
      personTable: [],
      resultField: [{
          key: 'rId',
          label: '根節點人物代碼',
          sortable: true
        },
        {
          key: 'rName',
          label: 'Root Name',
          sortable: true
        },
        {
          key: 'rNameChn',
          label: '根節點人物名',
          sortable: true
        },
        {
          key: 'pId',
          label: '人物ID',
          sortable: true
        },
        {
          key: 'pName',
          label: 'Person Name',
          sortable: true
        },
        {
          key: 'pNameChn',
          label: '人物姓名',
          sortable: true
        },
        {
          key: 'pAddrID',
          label: '人物地點ID',
          sortable: true
        },
        {
          key: 'pAddrType',
          label: 'Address Type',
          sortable: true
        },
        {
          key: 'pAddrTypeChn',
          label: '人物地點類型',
          sortable: true
        },
        {
          key: 'pAddrName',
          label: 'Address Name',
          sortable: true
        },
        {
          key: 'pAddrNameChn',
          label: '人物地點名',
          sortable: true
        },
        {
          key: 'pX',
          label: '人物地點經度',
          sortable: true
        },
        {
          key: 'pY',
          label: '人物地點緯度',
          sortable: true
        },
        {
          key: 'Id',
          label: '親屬代碼',
          sortable: true
        },
        {
          key: 'Name',
          label: 'Kin Name',
          sortable: true
        },
        {
          key: 'NameChn',
          label: '親屬名',
          sortable: true
        },
        {
          key: 'Sex',
          label: '親屬性别',
          sortable: true
        },
        {
          key: 'IndexYear',
          label: '親屬指数年',
          sortable: true
        },
        {
          key: 'pkinship',
          label: '親屬关系',
          sortable: true
        },
        {
          key: 'rKinship',
          label: '與根節點人物的親屬关系',
          sortable: true
        },
        {
          key: 'up',
          label: '向上查找的距離',
          sortable: true
        },
        {
          key: 'down',
          label: '向下查找的距離',
          sortable: true
        },
        {
          key: 'col',
          label: '同輩關係查找的距離',
          sortable: true
        },
        {
          key: 'mar',
          label: '姻親關係查找的距離',
          sortable: true
        },
        {
          key: 'AddrID',
          label: '親屬人物地點ID',
          sortable: true
        },
        {
          key: 'AddrType',
          label: 'Kin Address Type',
          sortable: true
        },
        {
          key: 'AddrTypeChn',
          label: '親屬人物地點類型',
          sortable: true
        },
        {
          key: 'AddrName',
          label: 'Kin Address Name',
          sortable: true
        },
        {
          key: 'AddrNameChn',
          label: '親屬人物地點名',
          sortable: true
        },
        {
          key: 'X',
          label: '親屬人物地點經度',
          sortable: true
        },
        {
          key: 'Y',
          label: '親屬人物地點緯度',
          sortable: true
        },
        {
          key: 'pDistance',
          label: '与亲属地點距離',
          sortable: true
        },
        {
          key: 'rDistance',
          label: '亲属與根節點人物地點距離',
          sortable: true
        },
        {
          key: 'xy_count',
          label: '結果中与亲属同一地點人數',
          sortable: true
        },
        {
          key: 'Notes',
          label: '_______備註______',
          sortable: true
        },
      ],
      //後端傳回來的數據放這裡
      result: undefined
    }
  },
  methods: {
    //判斷輸入欄是否為空
    isNull: isNull,
    validation: yearValidation,
    handleGetPerson: function(i) {
      personGetter(i, this)
    },
    async handleSubmit() {
      //提交表单的时候先清空原有數據
      this.personInfo = {}
      this.isBusy = true;
      let vm = this
      let f = vm.formData
      let data = {
        "people": vm.getPersonTableId,
        "mCircle": f.kinshipType,
        "MAncGen": f.MAncGen,
        "MDecGen": f.MDecGen,
        "MColLink": f.MColLink,
        "MMarLink": f.MMarLink,
        "MLoop": f.MLoop,
        "start": 0,
        "list": 65535
      }
      data = JSON.stringify(data)
      let query = `${vm.$store.state.global.apiAddress}query_relatives?RequestPlayload=${data}`
      console.log(query)
      this.axios.post(query)
        .then(res => {
            vm.result = {}
            vm.result.kins = res.data.data
          },
          (error) => {
            alert('Network Error...')
          }
        )
        .finally(() => {
          vm.isBusy = false
        })
    },
  },
  computed: {
    queryFormular() {
      return `person-id:'${this.formData.personId}';`
    },
    isInvalid() {
      return this.personTable.length === 0
    },
    getPersonTableId() {
      return this.personTable.map(i => i['personId'])
    },
    kinshipOptions: kinshipOptions
  },
  watch: {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.user-input-label{
 text-align:left;
 width:100%
}
.query-condition-button{
  width:224px;
  margin:6px 0;
}
.card-item-body{
  text-align:center;
  margin: 6px 0;
}
.bread-crumb{
  width:30%;
  background-color: transparent
}
.hello{
  margin-top:24px;
  text-align: left;
}
.card-item-title{
  font-weight: bold;
}
</style>
