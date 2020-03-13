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
                  <div v-if="this.formData.office.length==0" style = "line-height:31px">**{{$t('globalTerm.all')}}**</div>
                  <div v-else>{{formData.office[0]}}
                    <span v-if="this.formData.office.length>1">及另外{{this.formData.office.length-1}}個官職</span>
                    <b-button  variant="outline-primary" size = sm>查看已選</b-button>
                  </div>
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
                  <div v-if="this.formData.officePlace.length==0" style = "line-height:31px">**{{$t('globalTerm.all')}}**</div>
                  <div v-else>{{formData.officePlace[0]}}
                    <span v-if="this.formData.officePlace.length>1">及另外{{this.formData.officePlace.length-1}}個地點</span>
                    <b-button  variant="outline-primary" size = sm>查看已選</b-button>
                  </div>
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
                  <div v-if="this.formData.peoplePlace.length==0" style = "line-height:31px">**{{$t('globalTerm.all')}}**</div>
                  <div v-else>{{formData.officePlace[0]}}
                    <span v-if="this.formData.peoplePlace.length>1">及另外{{this.formData.peoplePlace.length-1}}個地點</span>
                    <b-button  variant="outline-primary" size = sm>查看已選</b-button>
                  </div>
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
              value="t" unchecked-value="f">
              <span style="font-size:16px">{{$t('globalTerm.date')}}({{$t('globalTerm.indexYear')}})</span>
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
import {isNull,yearValidation} from '@/components/utility/utility-functions.js'
import queryResult from '@/components/utility/query-result.vue'
import selectOffice from '@/components/utility/select-office.vue'
import selectPlace from '@/components/utility/select-place.vue'
import importPlace from '@/components/utility/import-place.vue'
export default {
  name: 'entityQueryByOffice',
  components:
  {
      queryResult,
      selectOffice,
      selectPlace,
      importPlace
  },
  data () {
    return {
      isBusy:false,
      /*表單數據放這裡*/
      formData:{
        office:[],
        officePlace:[],
        peoplePlace:[],
        indexStartTime:'',
        indexEndTime:'',
        indexYear:'f',
        useOfficePlace:'0',
        usePeoplePlace:'0'
      },
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
    handleGetOffice: function(selectedOffice){
      this.formData.office = selectedOffice.map(i => i.officeNameCh);
      console.log(this.formData.office)
      // this.formData.officeEnType = selectedOffice[0]['typeName'];
      // this.formData.officeChType = selectedOffice[0]['typeNameCh'];
    },
    //获取查询的人物地点
     handleGetPeoplePlace: function(selectedPlace){
       this.formData.peoplePlace = selectedPlace.map(i => i.pId);
     },
    //获取官职地点
    handleGetOfficePlace: function(selectedPlace){
       this.formData.officePlace = selectedPlace.map(i => i.pId);
    },
    //To Do
    testData: function(){
      console.log("测试");
      console.log(this.formData.officeChPlace);
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
    queryFormular(){
      return `office-ch-name:'${this.formData.officeChName}',office-en-name:'${this.formData.officeEnName}',office-ch-type:'${this.formData.officeChType}',office-en-type:'${this.formData.officeEnType}',office-ch-place:'${this.formData.officeChPlace}',office-en-place:'${this.formData.officeEnPlace}',person-ch-place:'${this.formData.personChPlace}',person-en-place:'${this.formData.personEnPlace}',start-time:'${this.formData.startTime}',end-time:'${this.formData.endTime}'index-year:'${this.formData.indexYear}';`
    },
    isInvalid(){
      return this.formData.office.length==0||this.validation('indexStartTime')===false || this.validation('indexEndTime')===false
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
