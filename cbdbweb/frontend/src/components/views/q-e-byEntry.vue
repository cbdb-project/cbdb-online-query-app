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
      <div class = "card-item-body">
        <b-row class = "p-3 my-3">
          <b-col cols="3"></b-col>
          <b-col><select-place
            @getPlaceName="handleGetPlace"></select-place></b-col>
          <b-col><select-entry
            @getEntryName="handleGetEntry"></select-entry></b-col>
          <b-col cols="3"></b-col>
        </b-row>
      </div>           
      <b-card-text class = "card-item-title">{{$t('globalTerm.alternativeInput')}}</b-card-text>          
      <div class  = "card-item-body px-3 ml-1">
        <b-row class = "px-3 mb-3">
           <b-col>
            <b-form-checkbox id="checkbox-1" v-model= "formData.entryYear" name="checkbox-1"
              value="t" unchecked-value="f" style = "margin:38px 0;text-align:right">
                {{$t('entityQueryByEntry.entryYearRange')}}
            </b-form-checkbox>
           </b-col>
          <b-col>
            <label for="entry-start-time" class = "user-input-label">{{$t('globalTerm.startTime')}}:</label>
            <b-form-input id="entry-start-time" v-model="formData.startTime" placeholder="" 
              :state="validation('entryStartTime')" :disabled="formData.entryYear==='f'?true:false"></b-form-input>
              <b-form-invalid-feedback :state="validation('entryStartTime')">
                Invalid year 
              </b-form-invalid-feedback>
            </b-col>
          <b-col>
             <label for="entry-end-time" class = "user-input-label">{{$t('globalTerm.endTime')}}:</label>
             <b-form-input id="entry-end-time" v-model="formData.endTime" placeholder="" 
             :state="validation('entryEndTime')" :disabled="formData.entryYear==='f'?true:false"></b-form-input>
              <b-form-invalid-feedback :state="validation('entryEndTime')" >
                Invalid year 
              </b-form-invalid-feedback>
           </b-col>
           <b-col cols="3"></b-col>
        </b-row>
        <b-row class = "px-3 mb-3">
           <b-col>
            <b-form-checkbox id="checkbox-2" v-model= "formData.indexYear" name="checkbox-2"
              value="t" unchecked-value="f" style = "margin:38px 0;text-align:right">
              {{$t('entityQueryByEntry.indexYearRange')}}
            </b-form-checkbox>
           </b-col>
          <b-col>
            <label for="index-start-time" class = "user-input-label">{{$t('globalTerm.startTime')}}:</label>
            <b-form-input id="index-start-time" v-model="formData.startTime" placeholder="" 
              :state="validation('indexStartTime')" :disabled="formData.indexYear==='f'?true:false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexStartTime')">
                Invalid year 
              </b-form-invalid-feedback>
            </b-col>
          <b-col>
             <label for="index-end-time" class = "user-input-label">{{$t('globalTerm.endTime')}}:</label>
             <b-form-input id="index-end-time" v-model="formData.endTime" placeholder="" 
             :state="validation('indexEndTime')" :disabled="formData.indexYear==='f'?true:false"></b-form-input>
              <b-form-invalid-feedback :state="validation('indexEndTime')">
                Invalid year 
              </b-form-invalid-feedback>
           </b-col>
           <b-col cols="3"></b-col>
        </b-row>
      </div>
      <b-card-text class = "card-item-title">{{$t('entityQueryByPerson.checkAndSearch')}}</b-card-text>
      <b-row class = "px-3 mb-3">
        <b-col cols="10">
          <!--
          <b-alert show variant="warning" style = "width:66%" class = "px-3 py-2 mb-2">{{$t('entityQueryByPerson.checkRemind')}}</b-alert>
          -->
          <b-card>
            <b-row class = "py-3">
              <b-col>
                {{$t('entityQueryByPerson.personId')}}: <b>{{formData.personId}}</b>
              </b-col>
              <b-col>
                {{$t('entityQueryByPerson.personNameCh')}}:  <b>{{formData.personNameCh}}</b>
              </b-col>
            </b-row>
            <b-row class = "py-3">
              <b-col>
                {{$t('entityQueryByPerson.personIndexYear')}}: <b>{{formData.personIndexYear}}</b>          
              </b-col>
              <b-col>
                  {{$t('entityQueryByPerson.personNameEn')}}: <b>{{formData.personNameEn}}</b>
              </b-col>
            </b-row>  
          </b-card>     
        </b-col>
        <b-col cols="2" class = "p-3">
            <b-button href="#" variant="primary" style = "width:100%;margin-top:38px" :disabled="isInvalid">Go</b-button>
        </b-col>
      </b-row>    
      <!--
      <template v-slot:footer>
        <em>Footer Slot</em>
      </template>
      -->
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
import queryResult from '@/components/utility/query-result.vue'
import selectPerson from '@/components/utility/select-person.vue'
import selectEntry from '@/components/utility/select-entry.vue'
import selectOffice from '@/components/utility/select-office.vue'
import selectTime from '@/components/utility/select-time.vue'
import selectPlace from '@/components/utility/select-place.vue'
import selectRelationship from '@/components/utility/select-relationship.vue'
export default {
  name: 'entityQueryByPerson',
  components:
  {
      queryResult,
      selectPerson,
      selectEntry,
      selectOffice,
      selectTime,
      selectPlace,
      selectRelationship
  },
  data () {
    return {
      /*表單數據放這裡*/
      formData:{
        personEnName:'',
        personChName:'',
        entryEnName:'',
        entryChName:'',
        entryStartTime:'',
        entryEndTime:'',
        indexStartTime:'',
        indexEndTime:'',
        entryYear:'f',
        indexYear:'f'
      }
    }
  },
  methods:{
    //判斷輸入欄是否為空
    isNull(idx){
      return this.formData[idx] == ''
    },
    validation(idx){
      //如果輸入為空，視為有效
      if(this.isNull(idx))return null;
      let year = /^\d{1,4}$/;
      //startTime 一欄只要輸入符合有且僅有1～4位數字的規則，視為有效
      if(idx == 'startTime')return year.test(this.formData[idx])?null:false;
      else if(idx == 'endTime'){
        //先判斷 endTime 一欄是否符合有且僅有1～4位數字的規則，如果不符合，視為無效
        if(year.test(this.formData[idx])){
          //如果 endTime 有輸入數字，同時 startTime 也有輸入數字，判斷 endTime 的數字是否大於 startTime 的數字
          //如果小於，則視為無效
          if(this.validation('startTime') == null && this.isNull('startTime')==false){
            let st = parseInt(this.formData['startTime'], 10);
            let et = parseInt(this.formData['endTime'], 10);
            return et>st?null:false;
          }
          else return null;
        }
        else return false;
      }
    },
    //获取人物信息
    handleGetPerson:function(selectedPerson){
      this.formData.personEnName = selectedPerson[0]['personName'];
      this.formData.personChName = selectedPerson[0]['personNameCh'];
    },
    //获取入仕途径信息
    handleGetEntry: function(selectedPlace){
      this.formData.entryEnName = selectedPlace[0]['entryName'];
      this.formData.entryChName = selectedPlace[0]['entryNameCh'];
    }
  },
  computed:{
    queryFormular(){
      return `office-ch-name:'${this.formData.officeChName}',office-en-name:'${this.formData.officeEnName}',office-ch-type:'${this.formData.officeChType}',office-en-type:'${this.formData.officeEnType}',office-ch-place:'${this.formData.officeChPlace}',office-en-place:'${this.formData.officeEnPlace}',person-ch-place:'${this.formData.personChPlace}',person-en-place:'${this.formData.personEnPlace}',start-time:'${this.formData.startTime}',end-time:'${this.formData.endTime}'index-year:'${this.formData.indexYear}';`
    },
    isInvalid(){
      return this.validation('startTime')==false || this.validation('endTime')==false
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
