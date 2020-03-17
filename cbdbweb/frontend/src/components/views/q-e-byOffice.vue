<template>
<div class="wrapper">
  <div class = "mt-3 pt-1 pl-1" style = "text-align:left">
      <h5>{{$t('navbarLeft.entityQueryByOffice')}}</h5>
  </div>
  <div class="hello">
    <b-card header-tag="header" footer-tag="footer">
      <template v-slot:header>
        <h6 class="mb-0">{{$t('globalTerm.queryInput')}}</h6>
      </template>
      <b-card-text class = "card-item-title">{{$t('globalTerm.requiredInput')}}</b-card-text>             
      <div class = "card-item-body">
        <b-row class = "p-3 my-3">
          <b-col cols="8" style = "text-align:left">
            <b-card-text class = "card-item-title">{{$t('globalTerm.office')}}</b-card-text>    
            <b-card>
              <b-row class="pl-3" style = "text-align:center">
                <b-col>
                  <span v-if="this.officeTable.length==0" style = "line-height:31px">**{{$t('globalTerm.all')}}**</span>
                  <span v-else>{{officeTable[0].officeNameCh}}
                    <span v-if="this.officeTable.length>1">及另外{{officeTable.length-1}}個官職</span>
                  </span>
                  <view-selected name='office' :fields="this.officeField" :items="this.officeTable" @update:items="val=>this.officeTable=val"></view-selected>   
                  </b-col>
              </b-row> 
            </b-card>   
          </b-col>
          <b-col cols="4" style = "text-align:left">
            <select-office @getOfficeName="handleGetOffice" style = "margin-top:56px"></select-office>
          </b-col>
        </b-row>
      </div>
      <b-card-text class = "card-item-title pt-3">{{$t('globalTerm.alternativeInput')}}</b-card-text>             
      <div class  = "card-item-body px-3">
        <!-- 职官地點 -->
        <b-row class = "px-3 mb-3">
          <b-card-text class = "card-item-title mt-3">
            <b-form-checkbox switch size="lg" id="checkbox-0" v-model= "formData.useOfficePlace" name="checkbox-0"
              value="1" unchecked-value="0">
                <span style="font-size:16px">{{$t('globalTerm.office')}}{{$t('globalTerm.place')}}</span>
            </b-form-checkbox>
          </b-card-text> 
        </b-row>
        <b-row class = "py-3 my-3" v-if="formData.useOfficePlace ==='1'">
          <b-col cols="8" style = "text-align:left"> 
            <b-card>
              <b-row class="pl-3" style = "text-align:center">
                <b-col>
                  <span v-if="this.officePlaceTable.length==0" style = "line-height:31px">**{{$t('globalTerm.all')}}**</span>
                  <span v-else>{{officePlaceTable[0]['placeNameCh']}}
                    <span v-if="this.officePlaceTable.length>1">及另外{{officePlaceTable.length-1}}個地點</span>
                  </span>
                  <view-selected name='officePlace' :fields="this.officePlaceField" :items="this.officePlaceTable" @update:items="val=>this.officePlaceTable=val"></view-selected>
                </b-col>
              </b-row> 
            </b-card>   
          </b-col>
          <b-col cols="4" style = "text-align:left" >
            <b-button-group>
            <select-place @getPlaceName="handleGetOfficePlace" name="office" style = "margin-top:16px"></select-place>
            <import-place @getPlaceName="handleGetOfficePlace" name="office" style = "margin-top:16px"></import-place>
            </b-button-group>
          </b-col>
        </b-row> 
        <!-- 人物地點 -->
        <b-row class = "px-3 mb-3">
          <b-card-text class = "card-item-title mt-3">
            <b-form-checkbox switch size="lg" id="checkbox-1" v-model= "formData.usePeoplePlace" name="checkbox-1"
              value="1" unchecked-value="0">
                <span style="font-size:16px">{{$t('globalTerm.person')}}{{$t('globalTerm.place')}}</span>
            </b-form-checkbox>
          </b-card-text> 
        </b-row>
        <b-row class = "py-3 my-3" v-if="formData.usePeoplePlace ==='1'">
          <b-col cols="8" style = "text-align:left"> 
            <b-card>
              <b-row class="pl-3" style = "text-align:center">
                <b-col>
                  <span v-if="this.peoplePlaceTable.length==0" style = "line-height:31px">**{{$t('globalTerm.all')}}**</span>
                  <span v-else>{{peoplePlaceTable[0]['placeNameCh']}}
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
            <import-place @getPlaceName="handleGetPeoplePlace" name="people" style = "margin-top:16px"></import-place>
            </b-button-group>
          </b-col>
        </b-row> 
        <!-- 日期 -->
        <b-row class = "px-3 mb-3">
          <b-card-text class = "card-item-title mt-3">
            <b-form-checkbox switch size="lg" id="checkbox-2" v-model= "formData.indexYear" name="checkbox-2"
              value="1" unchecked-value="0">
              <span style="font-size:16px">{{$t('globalTerm.date')}}({{$t('globalTerm.indexYear')}})</span>
            </b-form-checkbox>  
          </b-card-text> 
        </b-row>
        <b-row class = "px-3 mb-3"  v-if="formData.indexYear==='1'">
          <b-col>
            <label for="index-start-time" class = "user-input-label">{{$t('globalTerm.startTime')}}:</label>
            <b-form-input id="index-start-time" v-model="formData.indexStartTime" placeholder="" 
              :state="validation('indexStartTime')" :disabled="formData.indexYear==='0'?true:false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexStartTime')">
                Invalid year 
              </b-form-invalid-feedback>
            </b-col>
          <b-col>
             <label for="index-end-time" class = "user-input-label">{{$t('globalTerm.endTime')}}:</label>
             <b-form-input id="index-end-time" v-model="formData.indexEndTime" placeholder="" 
             :state="validation('indexEndTime')" :disabled="formData.indexYear==='0'?true:false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexEndTime')">
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
        <b-col class = "p-3">
            <b-button href="#" variant="primary" style = "width:100%;margin-top:38px" :disabled="isInvalid||isBusy" @click="handleSubmit">
              <span v-if="!isBusy">Go</span>
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
  <div class="hello" v-if="result.tableData!=undefined">
    <b-card header-tag="header" footer-tag="footer">
      <template v-slot:header>
          <h6 class="mb-0">{{$t('globalTerm.resultShow')}}</h6>
      </template>
      <query-result></query-result>
    </b-card>
  </div>
</div>
</template>

<script>
import {isNull,yearValidation,peoplePlaceGetter,officePlaceGetter,officeGetter} from '@/components/utility/utility-functions.js'
import queryResult from '@/components/utility/query-result.vue'
import selectOffice from '@/components/utility/select-office.vue'
import selectPlace from '@/components/utility/select-place.vue'
import importPlace from '@/components/utility/import-place.vue'
import viewSelected from '@/components/utility/view-selected.vue'
export default {
  name: 'entityQueryByOffice',
  components:
  {
      queryResult,
      selectOffice,
      selectPlace,
      importPlace,
      viewSelected
  },
  data () {
    return {
      isBusy:false,
      /*表單數據放這裡*/
      formData:{
        //office officePlace peoplePlace 在表单提交之前都是空的
        //所有涉及这三个变量的计算现在用计算属性
        office:[],
        officePlace:[],
        peoplePlace:[],
        indexStartTime:'',
        indexEndTime:'',
        //是否使用可选条件以布尔值为准！！！
        indexYear:'0',
        useOfficePlace:'0',
        usePeoplePlace:'0',
        useXy:'1'
      },
      officeTable:[],
      officeField:[],
      peoplePlaceField:[],
      officePlaceField:[],
      officePlaceTable:[],
      peoplePlaceTable:[],
      result:{
        totalPages:undefined,
        tableData:undefined
      }
    }
  },
  methods:{
    //判斷輸入欄是否為空
    isNull:isNull,
    validation:yearValidation,
    //获取查询的官职名
    handleGetOffice: function(i){
      officeGetter(i,this)
    },
    //获取查询的人物地点
     handleGetPeoplePlace: function(i){
      peoplePlaceGetter(i,this)
     },
    //获取官职地点
    handleGetOfficePlace: function(i){
      officePlaceGetter(i,this)
    },
    //To Do
    async handleSubmit(){
      //提交表单的时候先清空原有數據
      this.isBusy = true;
      const res = this.waitForServer(this.formData)
      res.then((r)=>
        {
          this.result.totalPages = r.data.totalPages
          this.result.tableData = r.data.data
          this.isBusy = false
          if(this.result.totalPages>1){
            for(let p = 2; p <= this.result.totalPages;p++)this.loadMore('api',p).then(res=>console.log(res))
          }
        },
        (e)=>{
          alert('something went wrong...')
          this.isBusy = false
        }
      )
    },
    //To Do
    waitForServer(query){
      //sendToServer(query)
      //------模擬服務器響應的東西---------
      return new Promise(function(resolve,reject){
        setTimeout((success=true)=>{
          if(success)resolve({status:'200',data:{totalPages:5,data:['']}})
          else reject({status:'404'})
        },1000)
      })
    },
    //To Do
    loadMore(api,page){
        return new Promise(function(resolve){
        setTimeout(()=>{resolve('This is Data!')},1000)
      })
    },
  },
  computed:{
    isInvalid(){
      return this.getOfficeTableId.length==0||this.validation('indexStartTime')===false || this.validation('indexEndTime')===false
    },
    tableLength(name){
      return this.formData[name].length
    },
    //formData里的Id改成计算形式了
    getOfficeTableId(){return this.officeTable.map(i=>i['pId'])},
    getPeoplePlaceTableId(){return this.peoplePlaceTable.map(i=>i['pId'])},
    getOfficePlaceTableId(){return this.officePlaceTable.map(i=>i['pId'])}
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
