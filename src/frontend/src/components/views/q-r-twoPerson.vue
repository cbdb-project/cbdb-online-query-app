<template>
<div class = "wrapper">
  <div class = "mt-3 pt-1 pl-1" style = "text-align:left">
    <h5></h5>
  </div>
  <div class="hello">
    <b-card header-tag="header" footer-tag="footer">
      <template v-slot:header>
        <h6 class="mb-0">{{$t('globalTerm.queryInput')}}</h6>
      </template>
      <b-card-text class = "card-item-title">{{$t('globalTerm.requiredInput')}}</b-card-text>             
      <div class = "card-item-body px-3">
        <!-- 人物 -->
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
        <b-row class = "py-3 my-3">
          <b-col style = "text-align:left"> 
            <b-form-group>
              <b-form-checkbox-group
                id="checkbox-group-1"
                v-model="formData.relOption"
                :options="options"
                name="place-type"
              ></b-form-checkbox-group>
            </b-form-group>
          </b-col>
        </b-row> 
      </div>           
      <b-card-text class = "card-item-title pt-3">{{$t('globalTerm.alternativeInput')}}</b-card-text>          
      <div class  = "card-item-body px-3">
        <!-- 日期 -->
        <b-row class = "px-3 mb-3">
          <b-card-text class = "card-item-title mt-3">
            <b-form-checkbox switch size="lg" id="checkbox-2" v-model= "formData.useDate" name="checkbox-2"
              value="1" unchecked-value="0">
              <span style="font-size:16px">{{$t('globalTerm.date')}}</span>
            </b-form-checkbox>  
          </b-card-text> 
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
      <query-result></query-result>
    </b-card>
  </div>
</div>
</template>

<script>
import {isNull,yearValidation,personGetter} from '@/components/utility/utility-functions.js'
import queryResult from '@/components/utility/query-result.vue'
import selectPerson from '@/components/utility/select-person.vue'
import viewSelected from '@/components/utility/view-selected.vue'
export default {
  name: 'entityQueryByPlace',
  components:
  {
      queryResult,
      selectPerson,
      viewSelected
  },
  data () {
    return {
      isBusy:false,
      /*表單數據放這裡*/
      formData:{
        //用计算属性
        person:[],
        relOption:[]
      },
      personField:[],
      personTable:[],
      options: [
          { text: '包括距離二人', value: 'distanceTwoPerson' },
          { text: '包括親屬關係', value: 'kinship' },
        ],
    }
  },
  methods:{
    //判斷輸入欄是否為空
    isNull:isNull,
    validation:yearValidation,
    //获取人物籍贯信息
    handleGetPerson: function(i){
      personGetter(i,this)
    },
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
  },
  computed:{
    locationOptions(){
      return  [
          { text: 'Household addr. only', value: 'pAddr' },
          { text: 'Entry location addr. only', value: 'eAddr' },
          { text: 'Household & Entry location addr.', value: 'peAddr' }
        ]
      },
    dateOptions(){
      return  [
          { text: this.$t('entityQueryByEntry.entryYear'), value: 'entry' },
          { text: this.$t('entityQueryByEntry.indexYear'), value: 'index' },
        ]
      },
    isInvalid(){
      return (this.personTable.length===0)||this.validation('dateEndTime')===false || this.validation('dateStartTime')===false
    },
    getPersonTableId(){return this.personTable.map(i => i['eId'])}
    },
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
