<template>
<div class = "wrapper">
  <div class = "mt-3 pt-1 pl-1" style = "text-align:left">
    <h5>{{$t('navbarLeft.entityQueryByEntry')}}</h5>
  </div>
  <div class="hello">
    <b-card header-tag="header" footer-tag="footer">
      <template v-slot:header>
        <h6 class="mb-0">{{$t('globalTerm.queryInput')}}</h6>
      </template>
      <b-card-text class = "card-item-title">{{$t('globalTerm.requiredInput')}}</b-card-text>             
      <div class = "card-item-body px-3">
        <b-row class = "py-3 my-3">
          <b-col cols="8" style = "text-align:left">
            <b-card-text class = "card-item-title">{{$t('globalTerm.entry')}}</b-card-text>    
            <b-card>
              <b-row class="pl-3" style = "text-align:center">
                <b-col>
                  <span v-if="this.entryTable.length==0" style = "line-height:31px">**{{$t('globalTerm.all')}}**</span>
                  <span v-else>{{entryTable[0]['eNameChn']}}
                    <span v-if="this.entryTable.length>1">及另外{{this.entryTable.length-1}}種入仕途徑</span>
                  </span>
                  <view-selected name="entry" :fields="this.entryField" :items="this.entryTable" @update:items="val=>this.entryTable=val"></view-selected>
                </b-col>
              </b-row> 
            </b-card>   
          </b-col>
          <b-col  cols="4" style = "text-align:left">
            <select-entry @getEntryName="handleGetEntry" style = "margin-top:56px"></select-entry>
          </b-col>
        </b-row>
      </div>           
      <b-card-text class = "card-item-title pt-3">{{$t('globalTerm.alternativeInput')}}</b-card-text>          
      <div class  = "card-item-body px-3">
        <!-- 人物地點 -->
        <b-row class = "px-3 mb-3">
          <b-card-text class = "card-item-title mt-3">
            <b-form-checkbox switch size="lg" id="checkbox-1" v-model= "formData.usePeoplePlace" name="checkbox-1"
              value="1" unchecked-value="0">
                <span style="font-size:16px">{{$t('globalTerm.person')}}{{$t('globalTerm.place')}}</span>
            </b-form-checkbox>
          </b-card-text> 
        </b-row>
        <b-row class = "px-3 mb-3" v-if="formData.usePeoplePlace==='1'">
          <b-col cols="8" style = "text-align:left">
            <b-form-radio-group
              id="btn-radios"
              v-model="formData.locationType"
              :options="locationOptions"
              size="sm"
              buttons
              button-variant="outline-primary"
              name="radio-btn-outline"
            ></b-form-radio-group>
          </b-col>
          <b-col cols="4">
          </b-col>
        </b-row>
        <b-row class = "py-3 my-3" v-if="formData.usePeoplePlace ==='1'">
          <b-col cols="8" style = "text-align:left"> 
            <b-card>
              <b-row class="pl-3" style = "text-align:center">
                <b-col>
                  <span v-if="this.peoplePlaceTable.length==0" style = "line-height:31px">**{{$t('globalTerm.all')}}**</span>
                  <span v-else>{{peoplePlaceTable[0]['pNameChn']}}
                    <span v-if="this.peoplePlaceTable.length>1">及另外{{peoplePlaceTable.length-1}}個地點</span>
                  </span>
                  <view-selected name='peoplePlace' :fields="this.peoplePlaceField" :items="this.peoplePlaceTable" @update:items="val=>this.peoplePlaceTable=val"></view-selected>
                </b-col>
              </b-row> 
            </b-card>   
          </b-col>
          <b-col cols="4" style = "text-align:left" >
            <b-button-group>
            <select-place @getPlaceName="handleGetPeoplePlace" name="people" style = "margin-top:16px"></select-place>
            <!--
            <import-place @getPlaceName="handleGetPeoplePlace" name="people" style = "margin-top:16px"></import-place>
            -->
            </b-button-group>
          </b-col>
        </b-row> 
        <!-- 日期 -->
        <b-row class = "px-3 mb-3">
          <b-card-text class = "card-item-title mt-3">
            <b-form-checkbox switch size="lg" id="checkbox-2" v-model= "formData.useDate" name="checkbox-2"
              value="1" unchecked-value="0">
              <span style="font-size:16px">{{$t('globalTerm.date')}}</span>
            </b-form-checkbox>  
          </b-card-text> 
        </b-row>
        <b-row class = "px-3 mb-3" v-if="formData.useDate==='1'">
          <b-col cols="6" style = "text-align:left">
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
          <b-col cols="6">
          </b-col>
        </b-row>
        <b-row class = "px-3 mb-3"  v-if="formData.useDate==='1'">
          <b-col>
            <label for="date-start-time" class = "user-input-label">{{$t('globalTerm.startTime')}}:</label>
            <b-form-input id="date-start-time" v-model="formData.dateStartTime" placeholder="" 
              :state="validation('dateStartTime')" :disabled="formData.useDate==='0'?true:false"></b-form-input>
              <b-form-invalid-feedback :state="validation('dateStartTime')">
                Invalid year 
              </b-form-invalid-feedback>
            </b-col>
          <b-col>
             <label for="date-end-time" class = "user-input-label">{{$t('globalTerm.endTime')}}:</label>
             <b-form-input id="date-end-time" v-model="formData.dateEndTime" placeholder="" 
             :state="validation('dateEndTime')" :disabled="formData.useDate==='0'?true:false"></b-form-input>
              <b-form-invalid-feedback :state="validation('dateEndTime')">
                Invalid year 
              </b-form-invalid-feedback>
           </b-col>
           <b-col cols="4"></b-col>
        </b-row>
        <!-- 使用xy坐标 -->  
        <b-row class = "px-1 py-3 my-3" style = "text-align:left">
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
      <b-row class = "px-3 mb-3">
        <b-col></b-col>
        <b-col  class = "p-3">
            <b-button href="#" variant="primary" style = "width:100%;margin-top:38px" 
            :disabled="isInvalid||isBusy" @click="handleSubmit">
              <span v-if="!isBusy">{{$t('globalTerm.search')}}</span>
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
  <div class="hello" v-if="result!==undefined">
    <b-card header-tag="header" footer-tag="footer">
      <template v-slot:header>
          <h6 class="mb-0">{{$t('globalTerm.resultShow')}}</h6>
      </template>
      <query-result name="entry" :items="result.entry" :fields="resultField"></query-result>
    </b-card>
  </div>
</div>
</template>

<script>
import {
  isNull,
  yearValidation,
  peoplePlaceGetter,
  entryGetter
} from '@/components/utility/utility-functions.js'
import queryResult from '@/components/utility/query-result.vue'
import selectEntry from '@/components/utility/select-entry.vue'
import selectPlace from '@/components/utility/select-place.vue'
//import importPlace from '@/components/utility/import-place.vue'
import viewSelected from '@/components/utility/view-selected.vue'
export default {
  name: 'entityQueryByEntry',
  components: {
    queryResult,
    selectEntry,
    selectPlace,
    //importPlace,
    viewSelected
  },
  data() {
    return {
      isBusy: false,
      /*表單數據放這裡*/
      formData: {
        //用计算属性
        entry: [],
        peoplePlace: [],
        dateStartTime: '',
        dateEndTime: '',
        dateType: 'entry',
        useDate: '0',
        usePeoplePlace: '0',
        useXy: '1',
        locationType: 'peAddr'
      },
      entryField: [],
      entryTable: [],
      peoplePlaceField: [],
      peoplePlaceTable: [],
      resultField: [{
          key: 'PersonID',
          label: '人物代碼',
          sortable: true
        },
        {
          key: 'Name',
          label: 'Name',
          sortable: true
        },
        {
          key: 'NameChn',
          label: '人物姓名',
          sortable: true
        },
        {
          key: 'Sex',
          label: 'Sex',
          sortable: true
        },
        {
          key: 'IndexYear',
          label: 'Index Year',
          sortable: true
        },
        {
          key: 'EntryDesc',
          label: '入仕途徑',
          sortable: true
        },
        {
          key: 'EntryChn',
          label: 'Entry Description',
          sortable: true
        },
        {
          key: 'EntryYear',
          label: '入仕年',
          sortable: true
        },
        {
          key: 'EntryRank',
          label: '考試排名',
          sortable: true
        },
        {
          key: 'KinType',
          label: '親屬類型',
          sortable: true
        },
        {
          key: 'KinName',
          label: 'Kin Name',
          sortable: true
        },
        {
          key: 'KinChn',
          label: '親屬姓名',
          sortable: true
        },
        {
          key: 'Association',
          label: '社會關係',
          sortable: true
        },
        {
          key: 'AssoName',
          label: 'Associate Name',
          sortable: true
        },
        {
          key: 'AssocChn',
          label: '社會關係人姓名',
          sortable: true
        },
        {
          key: 'AddrID',
          label: '人物地點ID',
          sortable: true
        },
        {
          key: 'AddrName',
          label: 'Address Name',
          sortable: true
        },
        {
          key: 'AddrChn',
          label: '人物地點名',
          sortable: true
        },
        {
          key: 'X',
          label: '經度',
          sortable: true
        },
        {
          key: 'Y',
          label: '緯度',
          sortable: true
        },
        {
          key: 'xy_count',
          label: 'XY Count',
          sortable: true
        },
        {
          key: 'ParentState',
          label: 'Parents State',
          sortable: true
        },
        {
          key: 'ParentStateChn',
          label: '父母情況',
          sortable: true
        },
        {
          key: 'EntryPlace',
          label: 'Entry Place',
          sortable: true
        },
        {
          key: 'EntryPlaceChn',
          label: '入仕地點',
          sortable: true
        },
        {
          key: 'EntryX',
          label: '入仕地點經度',
          sortable: true
        },
        {
          key: 'EntryY',
          label: '入仕地點緯度',
          sortable: true
        },
        {
          key: 'entry_xy_count',
          label: 'Entry XY Count',
          sortable: true
        }
      ],
      result: undefined
    }
  },
  methods: {
    //判斷輸入欄是否為空
    isNull: isNull,
    validation: yearValidation,
    //获取人物籍贯信息
    handleGetPeoplePlace: function(i) {
      peoplePlaceGetter(i, this)
    },
    //获取入仕途径信息
    handleGetEntry: function(i) {
      entryGetter(i, this)
    },
    async handleSubmit() {
      //提交表单的时候先清空原有數據
      this.isBusy = true;
      let vm = this
      let f = vm.formData
      let useXy = f.useXy
      if (f.usePeoplePlace === '0') useXy = 0
      let data = {
        "entry": vm.getEntryTableId,
        "usePeoplePlace": parseInt(f.usePeoplePlace),
        "peoplePlace": vm.getPeoplePlaceTableId,
        "locationType": f.locationType,
        "useDate": parseInt(f.useDate, 10),
        "dateType": f.dateType,
        "dateStartTime": parseInt(f.dateStartTime, 10),
        "dateEndTime": parseInt(f.dateEndTime, 10),
        "useXy": useXy,
        "start": 0,
        "list": 65535
      }
      data = JSON.stringify(data)
      let query = `${vm.$store.state.global.apiAddress}query_entry_postings?RequestPlayload=${data}`
      //console.log(query)
      this.axios.post(query)
        .then(res => {
            vm.result = {}
            vm.result.entry = res.data.data
          },
          (error) => {
            alert('Network Error...')
          }
        )
        .finally(() => {
          vm.isBusy = false
        })
    }
  },
  computed: {
    locationOptions() {
      return [{
          text: 'Household addr. only',
          value: 'pAddr'
        },
        {
          text: 'Entry location addr. only',
          value: 'eAddr'
        },
        {
          text: 'Household & Entry location addr.',
          value: 'peAddr'
        }
      ]
    },
    dateOptions() {
      return [{
          text: this.$t('entityQueryByEntry.entryYear'),
          value: 'entry'
        },
        {
          text: this.$t('entityQueryByEntry.indexYear'),
          value: 'index'
        },
      ]
    },
    isInvalid() {
      return (this.getEntryTableId.length == 0) || this.validation('dateEndTime') === false || this.validation('dateStartTime') === false
    },
    getPeoplePlaceTableId() {
      return this.peoplePlaceTable.map(i => i['pId'])
    },
    getEntryTableId() {
      return this.entryTable.map(i => i['eId'])
    }
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
