<template>
<div class = "wrapper">
  <div class="hello">
    <b-breadcrumb :items="items" class = "bread-crumb"></b-breadcrumb>
    <b-card header-tag="header" footer-tag="footer">
      <template v-slot:header>
        <h6 class="mb-0">{{$t('globalTerm.queryInput')}}</h6>
      </template>
      <b-card-text class = "card-item-title">{{$t('globalTerm.userInput')}}</b-card-text>             
      <div class  = "card-item-body px-3">
        <b-row class = "p-3 mb-3">
            <b-col>
            <select-person
            @getPersonName="handleGetPerson">
            </select-person>
            </b-col>
        </b-row>
      </div>
      <b-card-text class = "card-item-title">{{$t('entityQueryByPerson.checkAndSearch')}}</b-card-text>
      <b-alert show variant="warning"  class = "px-3 py-2 mx-3" style = "width:66%">{{$t('entityQueryByPerson.checkRemind')}}</b-alert>
      <b-row class = "px-3 mb-3">
        <b-col>
        </b-col>
        <b-col cols="8">
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
        </b-col>
        <b-col cols="2" class = "p-3">
            <b-button href="#" variant="primary" style = "width:100%;margin-top:22px" :disabled="isInvalid"
              @click="handleSubmit"
            >Go</b-button>
        </b-col>
        <b-col>
        </b-col>
      </b-row>    
      <!--
      <template v-slot:footer>
        <em>Footer Slot</em>
      </template>
      -->
    </b-card>
  </div>
    <!-- 按人查詢頁的結果和其他不太一樣，單獨寫出來-->
    <div class="hello" v-if="Object.keys(this.personInfo).length!= 0">
    <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
            <h6 class="mb-0">{{$t('globalTerm.resultShow')}}</h6>
        </template>
        <div>
          <b-tabs content-class="mt-3">
            <!-- 人物基本信息 -->
            <b-tab :title="$t('entityQueryByPerson.result.basicInfo')" active>
              <h6 class="m-3">{{personInfo.basicInfo.cName}} {{personInfo.basicInfo.cNameChn}}</h6>
              <b-card>
                 <!-- 第一行：姓 姓的拼音 名 名的拼音 -->
                <b-row class = "px-3 mb-3">
                  <b-col>
                    {{$t('entityQueryByPerson.result.biSurnameCh')}}: {{personInfo.basicInfo.cSurnameChn}}
                  </b-col>
                  <b-col>
                    {{$t('entityQueryByPerson.result.biSurnameEn')}}: {{personInfo.basicInfo.cSurname}}
                  </b-col>
                  <b-col>
                    {{$t('entityQueryByPerson.result.biNameCh')}}: {{personInfo.basicInfo.cMingziChn}}
                  </b-col>
                  <b-col>
                    {{$t('entityQueryByPerson.result.biSurnameEn')}}: {{personInfo.basicInfo.cMingzi}}
                  </b-col>
                </b-row>
                <!-- 第二行：ID 性別 指數年 無 -->
                <b-row class = "px-3 mb-3">
                  <b-col>
                    {{$t('globalTerm.personId')}}: {{personInfo.basicInfo.cPersonId}}
                  </b-col>
                  <b-col>
                    {{$t('globalTerm.gen')}}: {{personGen(personInfo.basicInfo.cFemale)}}
                  </b-col>
                  <b-col>
                    {{$t('globalTerm.indexYear')}}: {{personInfo.basicInfo.cIndexYear}}
                  </b-col>
                  <b-col>
                  </b-col>
                </b-row>
                <!-- 第三行：注 -->
                <b-row class = "px-3 mb-3">
                  <b-col>
                  {{$t('globalTerm.notes')}}:<p>{{personInfo.basicInfo.cNotes}}</p>
                  </b-col>
                </b-row>
              </b-card>
            </b-tab>
             <!-- 生卒年月 -->
            <b-tab :title="$t('entityQueryByPerson.result.birthDeath')"> 
              <b-card>
                <!-- 第一行： 朝代 郡望 戶籍 種族 -->
                <b-row class = "px-3 mb-3">
                  <b-col>
                     {{$t('entityQueryByPerson.result.dynasty')}}: {{personInfo.birthDeathYears.cDynastyChn}}/ {{personInfo.birthDeathYears.cDynasty}}
                  </b-col>
                  <b-col>
                      {{$t('entityQueryByPerson.result.choronym')}}: {{personInfo.birthDeathYears.cChoronymChn}}/ {{personInfo.birthDeathYears.cChoronym}}
                  </b-col>
                  <b-col>
                    {{$t('entityQueryByPerson.result.householdStatus')}}: {{personInfo.birthDeathYears.cHouseholdStatusChn}}/ {{personInfo.birthDeathYears.cHouseholdStatus}}
                  </b-col>
                  <b-col>
                    {{$t('entityQueryByPerson.result.ethnicity')}}: {{personInfo.birthDeathYears.cEthnicityChn}}/ {{personInfo.birthDeathYears.cEthnicity}}
                  </b-col>
                </b-row>
                <!-- 第二行： 生卒年 -->
                <b-row class = "px-3 mb-3">
                  <b-col cols = 6>
                      <b-row class = "px-3">
                     {{$t('entityQueryByPerson.result.birthYear')}}: {{personInfo.birthDeathYears.cBirthYear}} 
                     <span v-if="isValidNum(personInfo.birthDeathYears.cByRange)">({{judgeRange(personInfo.birthDeathYears.cByRange)}})</span>
                      <b-button v-b-toggle.birthYearDetails size="sm" pill variant="outline-info"
                      style = "position:relative;bottom:5px;left:5px">
                        {{$t('globalTerm.details')}}
                        </b-button>
                      </b-row>
                      <b-collapse id = "birthYearDetails">
                        <b-row>
                          <b-col cols = 9>
                            <!-- intercalary: 閏-->
                            {{personInfo.birthDeathYears.cByNhChn}}<span v-if="personInfo.birthDeathYears.cByNhChn&&personInfo.birthDeathYears.cByNh">/ </span>{{personInfo.birthDeathYears.cByNh}}
                            <span v-if="isValidNum(personInfo.birthDeathYears.cByNhYear)">{{personInfo.birthDeathYears.cByNhYear}} {{$t('globalTerm.year')}} </span> 
                            <span v-if="personInfo.birthDeathYears.cByIntercalary==='true'">{{$t('globalTerm.intercalary')}} </span> 
                            <span v-if="isValidNum(personInfo.birthDeathYears.cByMonth)">{{personInfo.birthDeathYears.cByMonth}} {{$t('globalTerm.month')}} </span>
                            <span v-if="isValidNum(personInfo.birthDeathYears.cByDay)">{{personInfo.birthDeathYears.cByDay}} {{$t('globalTerm.day')}} </span>
                          </b-col>
                          <b-col cols = 3>
                            <span v-if="personInfo.birthDeathYears.cByDayGz">
                              {{personInfo.birthDeathYears.cByDayGz}}{{$t('globalTerm.ganzhi')}}
                            </span>
                          </b-col>
                        </b-row>
                    </b-collapse>
                  </b-col>
                  <b-col cols = 6>
                    <b-row class = "px-3">
                     {{$t('entityQueryByPerson.result.deathYear')}}: {{personInfo.birthDeathYears.cDeathYear}} 
                     <span v-if="isValidNum(personInfo.birthDeathYears.cDyRange)">({{judgeRange(personInfo.birthDeathYears.cDyRange)}})</span>
                      <b-button v-b-toggle.deathYearDetails size="sm" pill variant="outline-info" style = "position:relative;bottom:5px;left:5px">
                        {{$t('globalTerm.details')}}
                      </b-button>
                      </b-row>
                      <b-collapse id = "deathYearDetails">
                        <b-row class>
                          <b-col cols = 9>
                            <!-- intercalary: 閏-->
                            {{personInfo.birthDeathYears.cDyNhChn}}<span v-if="personInfo.birthDeathYears.cDyNhChn&&personInfo.birthDeathYears.cDyNh">/ </span>{{personInfo.birthDeathYears.cDyNh}}
                            <span v-if="isValidNum(personInfo.birthDeathYears.cDyNhYear)">{{personInfo.birthDeathYears.cDyNhYear}} {{$t('globalTerm.year')}} </span> 
                            <span v-if="personInfo.birthDeathYears.cDyIntercalary==='true'">{{$t('globalTerm.intercalary')}} </span> 
                            <span v-if="isValidNum(personInfo.birthDeathYears.cDyMonth)">{{personInfo.birthDeathYears.cDyMonth}} {{$t('globalTerm.month')}} </span>
                            <span v-if="isValidNum(personInfo.birthDeathYears.cDyDay)">{{personInfo.birthDeathYears.cDyDay}} {{$t('globalTerm.day')}} </span>
                          </b-col>
                          <b-col cols = 3>
                            <span v-if="personInfo.birthDeathYears.DyDayGz">
                              {{personInfo.birthDeathYears.cDyDayGz}}{{$t('globalTerm.ganzhi')}}
                            </span>
                          </b-col>
                        </b-row>
                    </b-collapse>
                  </b-col>
                </b-row>
                <!-- 第三行： 最早在世時間、最晚在世時間 -->
                <b-row class = "px-3 mb-3" v-if="personInfo.birthDeathYears.cFlEarlistYear||personInfo.birthDeathYears.cFlLatestYear">
                  <b-col cols = 6>
                      <b-row class = "px-3">
                     {{$t('entityQueryByPerson.result.earlistYear')}}: {{personInfo.birthDeathYears.cFlEarlistYear}} 
                      <b-button v-b-toggle.earlistYearDetails size="sm" pill variant="outline-info"
                      style = "position:relative;bottom:5px;left:5px">
                        {{$t('globalTerm.details')}}
                      </b-button>
                      </b-row>
                      <b-collapse id = "earlistYearDetails">
                        <b-row>
                          <b-col cols = 9>
                            {{personInfo.birthDeathYears.cFlEyNhChn}}<span v-if="personInfo.birthDeathYears.cFlEyNhChn&&personInfo.birthDeathYears.cFlEyNh">/ </span>{{personInfo.birthDeathYears.cFlEyNh}}
                            <span v-if="isValidNum(personInfo.birthDeathYears.cFlEyNhYear)">{{personInfo.birthDeathYears.cFlEyNhYear}} {{$t('globalTerm.year')}} </span> 
                          </b-col>
                          <b-col v-if="personInfo.birthDeathYears.cFlEyNotes">
                             {{$t('globalTerm.Notes')}}: {{personInfo.birthDeathYears.cFlEyNotes}}
                          </b-col>
                        </b-row>
                    </b-collapse>
                   </b-col>
                  <b-col cols = 6>
                      <b-row class = "px-3">
                     {{$t('entityQueryByPerson.result.latestYear')}}: {{personInfo.birthDeathYears.cFlLatestYear}} 
                      <b-button v-b-toggle.latestYearDetails size="sm" pill variant="outline-info"
                      style = "position:relative;bottom:5px;left:5px">
                        {{$t('globalTerm.details')}}
                      </b-button>
                      </b-row>
                      <b-collapse id = "latestYearDetails">
                        <b-row>
                          <b-col cols = 9>
                            <!-- intercalary: 閏-->
                            {{personInfo.birthDeathYears.cFlLyNhChn}}<span v-if="personInfo.birthDeathYears.cFlLyNhChn&&personInfo.birthDeathYears.cFlLyNh">/ </span>{{personInfo.birthDeathYears.cFlEyNh}}
                            <span v-if="isValidNum(personInfo.birthDeathYears.cFlLyNhYear)">{{personInfo.birthDeathYears.cFlLyNhYear}} {{$t('globalTerm.year')}} </span> 
                          </b-col>
                          <b-col v-if="personInfo.birthDeathYears.cFlLyNotes">
                             {{$t('globalTerm.Notes')}}: {{personInfo.birthDeathYears.cFlLyNotes}}
                          </b-col>
                        </b-row>
                    </b-collapse>
                  </b-col>
                </b-row>
                <!-- 第四行： 享年 -->
                 <b-row class = "px-3 mb-3">
                   <b-col cols = 6>
                    {{$t('globalTerm.deathAge')}}: {{personInfo.birthDeathYears.cDeathAge}}
                    <span v-if="isValidNum(personInfo.cDeathAgeRange)">{{$t('globalTerm.deathAgeRange')}}: {{personInfo.birthDeathYears.cDeathAgeRange}}</span>
                  </b-col>
                 </b-row>
              </b-card>                                
            </b-tab>
             <!-- 地址 -->
            <b-tab :title="$t('entityQueryByPerson.result.address')"> 
              <b-card v-for="(address,index) in personInfo.address">
                <!-- 第一行：地名 地名類型 遷徙順序 是否娘家-->
                 <b-row class = "px-3 mb-3">
                   <b-col>
                     {{$t('entityQueryByPerson.result.placeName')}}: {{address.placeNameChn}}/ {{address.placeName}}
                   </b-col>
                    <b-col>
                      {{$t('entityQueryByPerson.result.placeType')}}: {{address.typeChn}}/ {{address.type}}
                   </b-col>
                    <b-col>
                    {{$t('entityQueryByPerson.result.placeSeq')}}: {{address.sequence}}
                   </b-col>
                    <b-col>
                    {{$t('entityQueryByPerson.result.placeIsMaternal')}}: {{isMaternalAddress(address.isMaternal)}}
                   </b-col>
                 </b-row>
                 <!-- 第二行：起止時間-->
                 <b-row class = "px-3 mb-3">
                    <b-col cols = 6>
                      <b-row class = "px-3">
                        {{$t('globalTerm.fromYear')}}: {{address.pFromYear}} 
                        <span v-if="isValidNum(address.pFyRange)">({{judgeRange(address.pFyRange)}})</span>
                        <b-button v-b-toggle="'from-year-details-' + index" size="sm" pill variant="outline-info"
                          style = "position:relative;bottom:5px;left:5px">
                          {{$t('globalTerm.details')}}
                        </b-button>
                      </b-row>
                      <b-collapse :id ="fromYearDetails(index)">
                        <b-row>
                          <b-col cols = 9>
                            <!-- intercalary: 閏-->
                            {{address.pFyNhChn}}<span v-if="address.pFyNhChn&&address.pFyNh">/ </span>{{address.pFyNh}}
                            <span v-if="isValidNum(address.pFyNhYear)">{{address.pFyNhYear}} {{$t('globalTerm.year')}} </span> 
                            <span v-if="address.pFyIntercalary==='true'">{{$t('globalTerm.intercalary')}} </span> 
                            <span v-if="isValidNum(address.pFyMonth)">{{address.pFyMonth}} {{$t('globalTerm.month')}} </span>
                            <span v-if="isValidNum(address.pFyDay)">{{address.pFyDay}} {{$t('globalTerm.day')}} </span>
                          </b-col>
                          <b-col cols = 3>
                            <span v-if="address.pFyDayGz">
                              {{address.pFyDayGz}}{{$t('globalTerm.ganzhi')}}
                            </span>
                          </b-col>
                        </b-row>
                    </b-collapse>
                   </b-col>
                    <b-col cols = 6>
                    <b-row class = "px-3">
                     {{$t('globalTerm.toYear')}}: {{address.pToYear}} 
                     <span v-if="isValidNum(address.pTyRange)">({{judgeRange(address.pTyRange)}})</span>
                      <b-button  v-b-toggle="'to-year-details-' + index" size="sm" pill variant="outline-info" style = "position:relative;bottom:5px;left:5px">
                        {{$t('globalTerm.details')}}
                      </b-button>
                      </b-row>
                      <b-collapse :id ="toYearDetails(index)">
                        <b-row>
                          <b-col cols = 9>
                            <!-- intercalary: 閏-->
                            {{address.pTyNhChn}}<span v-if="address.pTyNhChn&&address.pTyNh">/ </span>{{address.pTyNh}}
                            <span v-if="isValidNum(address.pTyNhYear)">{{address.pTyNhYear}} {{$t('globalTerm.year')}} </span> 
                            <span v-if="address.pTyIntercalary==='true'">{{$t('globalTerm.intercalary')}} </span> 
                            <span v-if="isValidNum(address.pTyMonth)">{{address.pTyMonth}} {{$t('globalTerm.month')}} </span>
                            <span v-if="isValidNum(address.pTyDay)">{{address.pTyDay}} {{$t('globalTerm.day')}} </span>
                          </b-col>
                          <b-col cols = 3>
                            <span v-if="address.pFyDayGz">
                              {{address.pTyDayGz}}{{$t('globalTerm.ganzhi')}}
                            </span>
                          </b-col>
                        </b-row>
                    </b-collapse>
                   </b-col>
                 </b-row>
                  <!-- 第三行：來源 頁碼-->
                 <b-row class = "px-3 mb-3">
                   <b-col cols = 10>
                    {{$t('globalTerm.source')}}: {{address.pSourceChn}}/ {{address.pSource}}
                   </b-col>
                  <b-col cols = 2>
                    {{$t('globalTerm.pages')}}: {{address.psPages}}
                  </b-col>
                 </b-row>
                 <!-- 第四行：註 -->
                <b-row class = "px-3">
                  <b-col>
                  {{$t('globalTerm.notes')}}:<p>{{address.pNotes}}</p>
                  </b-col>
                </b-row>
              </b-card>                              
            </b-tab>
            
          </b-tabs>
        </div>
      <!--
      <template v-slot:footer>
        <em>Footer Slot</em>
      </template>
      -->
    </b-card>   
  </div>
</div>
</template>

<script>
import selectPerson from '@/components/utility/select-person.vue'
export default {
  name: 'entityQueryByPerson',
  components:
  {
      selectPerson
  },
  data () {
    return {
      /*表單數據放這裡*/
      formData:{
        personId:'',
        personNameEn:'',
        personNameCh:'',
        personIndexYear:''
      },
      //後端傳回來的數據放這裡
      personInfo:{},
      //這個是路由，待處理
      items: [
          {
            text: 'Admin',
            href: '#'
          },
          {
            text: 'Manage',
            href: '#'
          },
          {
            text: 'Library',
            active: true
          }
      ]
    }
  },
  methods:{
    //生成from-year-details 和 to-year-details 的id
    fromYearDetails(i){
      return "from-year-details-"+i
    },
    toYearDetails(i){
      return "to-year-details-"+i
    },
    //判斷年份範圍
    judgeRange(r){
      let n = parseInt(r, 10);
      if(r<0)return this.$t('globalTerm.before')
      else if(r>0) return this.$t('globalTerm.after')
    },
    //判斷數字是否有效（非空且不為0）
    isValidNum(n){
        if(n&&n.length != 0&&n!=='0')return true
        else return false 
    },
    personGen(isF){
      if(isF === "false")return this.$t('globalTerm.male');
      else if (isF === "true")return this.$t('globalTerm.female');
      else return ''
    },
    isMaternalAddress(add){
      if(add === "false")return this.$t('globalTerm.false');
      else if (add === "true")return this.$t('globalTerm.true');
      else return ''
    },
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
    //获取查询的人物
    handleGetPerson: function(selectedPerson){
      this.formData.personId = selectedPerson[0]['personId'];
      this.formData.personNameEn = selectedPerson[0]['personName'];
      this.formData.personNameCh = selectedPerson[0]['personNameCh'];
      this.formData.personIndexYear = selectedPerson[0]['indexYear'];
    },
    handleSubmit: function(){
      //這裏未來要寫前後端交互
      this.personInfo = {
        basicInfo:{
          cName:this.formData.personNameEn,
          cNameChn:this.formData.personNameCh,
          cPersonId:this.formData.personId,
          cSurname:"Zhu",
          cSurnameChn:"朱",
          cMingzi:"Youxiao",
          cMingziChn:"由校",
          cIndexYear:this.formData.personIndexYear,
          cFemale:"false",
          cNotes:"Zhu(1) Yoiuxiao [30164] Xizong or the Tianqi Emperor.See Documentation for Zhu(1) Yuanzhang [30149].",
        },
        birthDeathYears:{
          cDynasty:"Ming",
          cDynastyChn:"明",
          cChoronym:"[Unknown]",
          cChoronymChn:"【未詳】",
          cHouseholdStatus:"Unknown",
          cHouseholdStatusChn:"未詳",
          cEthnicity:"Unknown",
          cEthnicityChn:"未詳",
          cBirthYear:"1605",
          cByNh:"",
          cByNhChn:"萬曆",
          cByNhYear:"33",
          cByRange:"",
          cByIntercalary:"false",
          cByMonth:"",
          cByDay:"",
          cByDayGz:"",//干支
          cDyIntercalary:"false",
          cDyMonth:"",
          cDyDay:"",
          cDyDayGz:"",
          cDeathYear:"1627",
          cDyNh:"",
          cDyNhChn:"天啟",
          cDyNhYear:"7",
          cDyRange:"",
          cDeathAge:"23",
          cDeathAgeRange:"",
          cFlEarliestYear:"",//在世始年
          cFlEyNh:"Unknown",//年號
          cFlEyNhChn:"未詳",
          cFlEyNhYear:"",//多少年,
          cFlEyNotes:"",
          cFlLatestYear:"",//在世末年
          cFlLyNh:"Unknown",//年號
          cFlLyNhChn:"未詳",//年號
          cFlLyNhYear:"",//多少年,
          cFlLyNotes:"",   
        },
        address:[
          {
            placeName:"Daxing",
            placeNameChn:"大興",
            type:"Basic Affiliation",
            typeChn:"籍貫（基本地址）",
            isMaternal:"false",
            sequence:"0",
            pFromYear:"0",
            pFyRange:"-1",
            pFyNh:"unknown",
            pFyNhChn:"未詳",
            pFyNhYear:"1",
            pFyIntercalary:"true",
            pFyMonth:"1",
            pFyDay:"1",
            pFyDayGz:"",//干支
            pToYear:"0",
            pTyRange:"",
            pTyNh:"unknown",
            pTyNhChn:"未詳",
            pTyNhYear:"",
            pTyIntercalary:"false",
            pTyMonth:"",
            pTyDay:"",
            pTyDayGz:"",//干支
            pSource:"Renming quanwei ziliao (Zhongyang yanjiuyuan Lishi yuyan yanjiusuo)",
            pSourceChn:"人名權威資料（中央研究院歷史語言研究所）",
            psPages:"9537",
            pNotes:"北直隸·順天府（祖籍南直隸·鳳陽府）（中央研究院人名權威資料）。"
          },
          {
            placeName:"Daxing",
            placeNameChn:"大興",
            type:"Basic Affiliation",
            typeChn:"籍貫（基本地址）",
            isMaternal:"false",
            sequence:"0",
            pFromYear:"0",
            pFyRange:"-1",
            pFyNh:"unknown",
            pFyNhChn:"未詳",
            pFyNhYear:"1",
            pFyIntercalary:"true",
            pFyMonth:"1",
            pFyDay:"1",
            pFyDayGz:"",//干支
            pToYear:"0",
            pTyRange:"",
            pTyNh:"unknown",
            pTyNhChn:"未詳",
            pTyNhYear:"",
            pTyIntercalary:"false",
            pTyMonth:"",
            pTyDay:"",
            pTyDayGz:"",//干支
            pSource:"Renming quanwei ziliao (Zhongyang yanjiuyuan Lishi yuyan yanjiusuo)",
            pSourceChn:"人名權威資料（中央研究院歷史語言研究所）",
            psPages:"9537",
            pNotes:"北直隸·順天府（祖籍南直隸·鳳陽府）（中央研究院人名權威資料）。"
          }
        ],
        AltNames:[
          {
            name:"Datianchandaodunxiaoduyouzhangwenxiangwujingmuzhuangqinzhehuangdi",
            nameChn:"達天闡道敦孝篤友章文襄武靖穆莊勤悊皇帝",
            nType:"Posthumous Name",
            nTypeChn:"諡號",
            nSourceChn:"人名權威資料（中央研究院歷史語言研究所）",
            nsPages:"9537",
            nNotes:"參見《新校本明史》"
          },
          {
            name:"Datianchandaodunxiaoduyouzhangwenxiangwujingmuzhuangqinzhehuangdi",
            nameChn:"達天闡道敦孝篤友章文襄武靖穆莊勤哲皇帝",
            nType:"Posthumous Name",
            nTypeChn:"諡號",
            nSourceChn:"",
            nsPages:"",
            nNotes:""
          },
          {
            name:"Tianqi",
            nameChn:"天啓",
            nType:"Unknown",
            nTypeChn:"未詳",
            nSourceChn:"人名權威資料（中央研究院歷史語言研究所）",
            nsPages:"9537",
            nNotes:"參見《新校本明史》"
          },
          {
            name:"Xi Zong",
            nameChn:"熹宗",
            nType:"Unknown",
            nTypeChn:"未詳",
            nSourceChn:"人名權威資料（中央研究院歷史語言研究所）",
            nsPages:"9537",
            nNotes:"參見《新校本明史》"
          },
          {
            name:"Xi Zong",
            nameChn:"熹宗",
            nType:"Temple Name",
            nTypeChn:"廟號",
            nSourceChn:"",
            nsPages:"",
            nNotes:""
          },
          {
            name:"Zhe Di",
            nameChn:"悊帝",
            nType:"Unknown",
            nTypeChn:"未詳",
            nSourceChn:"",
            nsPages:"",
            nNotes:""
          }
        ],
        writings:[],
        postings:[],
        entry:[
          {
            entryName:"investiture as heir apparent",
            entryNameChn:"立儲",
            entryPlace:"",
            entryPlaceChn:"",
            entryYear:"1620",
            eyNh:"Unknown",
            eyNhChn:"未詳",
            eyNhYear:"0",
            eyRange:"",
            entryAge:"16",
            seqNo:"1",
            rank:"0",
            parentalStatus:"Unknown",
            parentalStatus:"未詳",
            //親屬信息，用於恩蔭
            kinship:"U",
            kinshipChn:"未詳",
            kinName:"Wei Xiang",
            kinNameChn:"未詳",
            association:"[Undefined]",
            associationChn:"未詳",
            associate:"Wei Xiang",
            associateChn:"未詳",
            firstPostingNote:"0000000",
            entrySource:"Weizhi",
            entrySourceChn:"未知",
            esPages:"",
            eNotes:""
          }
        ],
        events:[],
        status:[
          {
            statusName:"emperor",
            statusNameChn:"[皇帝]",
            sequence:"1",
            statusBeginYear:"0",
            sbyNh:"unknown",
            sbyNhChn:"未詳",
            sbyNhYear:"",
            sbyRange:"",
            statusEndYear:"0",
            seyNh:"unknown",
            seyNhChn:"未詳",
            seyNhYear:"",   
            seyRange:"",
            statusSource:"Weizhi",
            statusSourceChn:"未知",
            ssPages:"",
            sNotes:""
          }
        ],
        kinship:[
          {
            relation:"F",
            relationChn:"父",
            rPersonName:"Zhu Yijun",
            rPersonNameChn:"朱翊均",
            relationSource:"Weizhi",
            relationSourceChn:"未知",
            rsPages:"",
            rNotes:""
          },
          {
            relation:"W",
            relationChn:"妻",
            rPersonName:"Zhang Shi(Wife of Zhu Youjiao)",
            rPersonNameChn:"張氏(朱由校妻)",
            relationSource:"Ming Qing funv zhuzuo shujuku",
            relationSourceChn:"明清婦女著作數據庫",
            rsPages:"MQWW PoetID #3093",
            rNotes:""
          }
        ],
        associations:[],
        possessions:[],
        //sources 要做成個表！！！
        sources:[],
        institutions:[]
        
      }
    }
  },
  computed:{
    queryFormular(){
      return `person-id:'${this.formData.personId}';`
    },
    isInvalid(){
      return this.isNull('personId')==true
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
