<template>
<div class = "wrapper">
  <div class = "mt-3 pt-1 pl-1" style = "text-align:left">
  <h5>{{$t('navbarLeft.entityQueryByPerson')}}</h5>
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
                <b-col>未選擇</b-col>
              </b-row>
            </b-card>
          </b-col>
          <b-col cols="4" style = "text-align:left">
            <select-person @getPersonName="handleGetPerson" selectMode='single' style="margin-top:48px">
            </select-person>
          </b-col>
        </b-row>
        <b-row class = "px-3 mb-3">
          <b-card-text class = "card-item-title mt-3">
            <b-form-checkbox switch size="lg" id="checkbox-1" v-model= "formData.mCircle" name="checkbox-1"
              value="t" unchecked-value="f">
              <span style="font-size:16px">{{$t('globalTerm.mCircle')}}</span>
            </b-form-checkbox>  
          </b-card-text> 
        </b-row>
        <b-row class = "px-3 mb-3"  v-if="formData.mCircle==='f'">
          <b-col>
            <label for="max-ancestor-gen" class = "user-input-label">{{$t('relationQueryByKinship.maxAncestorGen')}}:</label>
            <b-form-input id="max-ancestor-gen" v-model="formData.startTime" placeholder="" 
              :state="validation('indexStartTime')" :disabled="false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexStartTime')">
                Invalid number
              </b-form-invalid-feedback>
            </b-col>
          <b-col>
             <label for="max-descend-gen" class = "user-input-label">{{$t('relationQueryByKinship.maxDescendGen')}}:</label>
             <b-form-input id="max-descend-gen" v-model="formData.endTime" placeholder="" 
             :state="validation('indexEndTime')" :disabled="false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexEndTime')">
                Invalid number
              </b-form-invalid-feedback>
           </b-col>
          <b-col>
            <label for="max-collaternal-links" class = "user-input-label">{{$t('relationQueryByKinship.maxCollaternalLinks')}}:</label>
            <b-form-input id="max-collaternal-links" v-model="formData.startTime" placeholder="" 
              :state="validation('indexStartTime')" :disabled="false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexStartTime')">
                Invalid number
              </b-form-invalid-feedback>
            </b-col>
          <b-col>
             <label for="max-marriage-links" class = "user-input-label">{{$t('relationQueryByKinship.maxMarriageLinks')}}:</label>
             <b-form-input id="max-marriage-links" v-model="formData.endTime" placeholder="" 
             :state="validation('indexEndTime')" :disabled="false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexEndTime')">
                Invalid number 
              </b-form-invalid-feedback>
           </b-col>
           <!-- TO DO: Max Loop 到底属于哪个层级？要验证 -->
           <b-col>
             <label for="max-loop" class = "user-input-label">{{$t('relationQueryByKinship.maxLoop')}}:
               <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
              </label>
             <b-form-input id="max-loop" v-model="formData.endTime" placeholder="" 
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
              <span v-if="!isBusy">Go</span>
              <b-spinner small v-else></b-spinner>
            </b-button>
          </a>
        </b-col>
        <b-col></b-col>
      </b-row>    
    </b-card>
  </div>
  <div class="hello">
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
import selectPerson from '@/components/utility/select-person.vue'
//開發用的假數據
import dataJson from '@/assets/person_data_dev.json'
export default {
  name: 'relationQueryByKinship',
  components:
  {
    queryResult,
    selectPerson,
  },
  data () {
    return {
      //控制加載標誌的出現
      isBusy: false,
      /*表單數據放這裡*/
      formData:{
        person:[],
        mCircle:'f'
      },
      //後端傳回來的數據放這裡
      personInfo:{

      },
    }
  },
  methods:{
    //生成各種年份詳情 xxx-year-details-xxx 的id
    genDetails(n,i){
      return n+"-details-"+i
    },
    //判斷數據是否有效（非空且不為0）
    isValidVar(n){
        if(n&&n.length != 0&&n!=='0')return true
        else return false 
    },
    //判斷人物的性別
    personGen(isF){
      if(isF === "false")return this.$t('globalTerm.male');
      else if (isF === "true")return this.$t('globalTerm.female');
      else return ''
    },
    //判斷是否
    isOrNot(str){
      if(str === "false")return this.$t('globalTerm.false');
      else if (str === "true")return this.$t('globalTerm.true');
      else return ''
    },
    //判斷輸入欄是否為空
    isNull:isNull,
    //判斷年代輸入是否有效
    validation:function(){return null},
    //获取查询的人物
    handleGetPerson: function(selectedPerson){
      this.formData.person = selectedPerson[0]['personId'];
    },
    async handleSubmit(){
      //提交表单的时候先清空原有數據
      this.personInfo = {}
      this.isBusy = true;
      //加了async修饰符res变成结果？
      const res = this.waitForServer(this.formData)
      res.then((r)=>
        {
          this.personInfo = r.data
          this.isBusy = false
        },
        (e)=>{
          alert('something went wrong...')
          this.isBusy = false
        }
      )
    },
    waitForServer(query){
      //sendToServer(query)
      //------模擬服務器響應的東西---------
      return new Promise(function(resolve,reject){
        setTimeout((success=true)=>{
          if(success)resolve({status:'200',data:dataJson})
          else reject({status:'404'})
        },3000)
      })
    },
  },
  computed:{
    queryFormular(){
      return `person-id:'${this.formData.personId}';`
    },
    isInvalid(){
      return this.formData.person.length == 0
    }
  },
  watch:{

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
