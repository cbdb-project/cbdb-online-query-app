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
                <b-col>未選擇</b-col>
              </b-row> 
            </b-card>   
          </b-col>
          <b-col cols="4" style = "text-align:left">
            <select-office @getPlaceName="handleGetOffice" style = "margin-top:46px"></select-office>
          </b-col>
        </b-row>
      </div>
      <b-card-text class = "card-item-title">{{$t('globalTerm.alternativeInput')}}</b-card-text>             
      <div class  = "card-item-body px-3">
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
           <b-col cols="4"></b-col>
        </b-row>
      </div>
      <b-row class = "px-3 mb-3">
        <b-col></b-col>
        <b-col class = "p-3">
            <b-button href="#" variant="primary" style = "width:100%;margin-top:38px" :disabled="isInvalid">Go</b-button>
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
import selectOffice from '@/components/utility/select-office.vue'
export default {
  name: 'entityQueryByOffice',
  components:
  {
      queryResult,
      selectOffice,
  },
  data () {
    return {
      /*表單數據放這裡*/
      formData:{
        officeEnName:'',
        officeChName:'',
        officeEnType:'',
        officeChType:'',
        officeEnPlace:'',
        officeChPlace:'',
        personEnPlace:'',
        personChPlace:'',
        startTime:'',
        endTime:'',
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
    //获取查询的官职名
    handleGetOffice: function(selectedOffice){
      this.formData.officeChName = selectedOffice[0]['officeName'];
      this.formData.officeEnName = selectedOffice[0]['officeNameCh'];
      // this.formData.officeEnType = selectedOffice[0]['typeName'];
      // this.formData.officeChType = selectedOffice[0]['typeNameCh'];
    },
    //获取查询的人物地点
    // handleGetPlace: function(selectedPlace){
    //   this.formData.personEnPlace = selectedPlace[0]['placeName'];
    //   this.formData.personChPlace = selectedPlace[0]['placeNameCh'];
    // },
    //获取官职地点
    handleGetPlace: function(selectedPlace){
      this.formData.officeEnPlace = selectedPlace[0]['placeName'];
      this.formData.officeChPlace = selectedPlace[0]['placeNameCh'];
    },
    testData: function(){
      console.log("测试");
      console.log(this.formData.officeChPlace);
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
