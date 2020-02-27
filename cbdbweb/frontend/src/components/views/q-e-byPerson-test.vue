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
        <b-row class = "p-3 my-3">
          <b-col cols="10" style = "text-align:left">
            <b-card-text class = "card-item-title">{{$t('globalTerm.person')}}</b-card-text>    
            <b-card>
              <b-row>
                <b-col>
                  {{$t('entityQueryByPerson.personId')}}: <b>{{formData.personId}}</b>
                </b-col>
                <b-col>
                  {{$t('entityQueryByPerson.personNameCh')}}:  <b>{{formData.personNameCh}}</b>
                </b-col>
                <b-col>
                    {{$t('entityQueryByPerson.personNameEn')}}: <b>{{formData.personNameEn}}</b>
                </b-col>
              </b-row>
            </b-card>
          </b-col>
          <b-col cols="2">
            <select-person @getPersonName="handleGetPerson" selectMode='single' importList="false" style="margin-top:50px">
            </select-person>
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
      <!--
      <template v-slot:footer>
        <em>Footer Slot</em>
      </template>
      -->
    </b-card>
  </div>
    <!-- 按人查詢頁的結果和其他不太一樣，單獨寫出來-->
    <div class="hello" v-if="Object.keys(this.personInfo).length!= 0" ref="res">
    <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
            <h6 class="mb-0">{{$t('globalTerm.resultShow')}}</h6>
        </template>
        <div>
          <h6 class="m-3">[{{personInfo.c_personid}}] {{personInfo.c_name}} {{personInfo.c_name_chn}}</h6>
          <b-tabs content-class="mt-3">
            <!-- 人物基本信息 -->
            <b-tab :title="$t('entityQueryByPerson.result.basicInfo')" :active="activeTab==='baseInfo'?true:false" @click="activeTab='baseInfo'">
              <b-card>
                 <!-- 第一行：姓 姓的拼音 名 名的拼音 -->
                <b-row class = "px-3 mb-3">
                  <b-col>
                    {{$t('entityQueryByPerson.result.biSurnameCh')}}: {{personInfo.c_surname_chn}}
                  </b-col>
                  <b-col>
                    {{$t('entityQueryByPerson.result.biSurnameEn')}}: {{personInfo.c_surname}}
                  </b-col>
                  <b-col>
                    {{$t('entityQueryByPerson.result.biNameCh')}}: {{personInfo.c_mingzi_chn}}
                  </b-col>
                  <b-col>
                    {{$t('entityQueryByPerson.result.biSurnameEn')}}: {{personInfo.c_mingzi}}
                  </b-col>
                </b-row>
                
                <!-- 第二行：ID 性別 指數年 無 -->
                <b-row class = "px-3 mb-3">
                  <b-col>
                    {{$t('globalTerm.personId')}}: {{personInfo.c_personid}}
                  </b-col>
                  <b-col>
                    {{$t('globalTerm.gen')}}: {{personGen(personInfo.c_female)}}
                  </b-col>
                  <b-col>
                    {{$t('globalTerm.indexYear')}}: {{personInfo.c_index_year}}
                  </b-col>
                  <b-col>
                  </b-col>
                </b-row>
                <!-- 第三行：注 -->
                <b-row class = "px-3 mb-3">
                  <b-col>
                  {{$t('globalTerm.notes')}}:<p>{{personInfo.c_notes}}</p>
                  </b-col>
                </b-row>
              </b-card>
            </b-tab>
            <!-- 別名 --> 
             <!-- 生卒年月 -->
            <!-- 地址 -->
            <!-- 著述 -->               
            <!-- 職官 -->
            <!-- 入仕 -->  
            <!-- 親屬關係 --> 
            <!-- 社會關係 --> 
            <!-- 地位 -->                                   
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
import {isNull} from '@/components/utility/utility-functions.js'
import selectPerson from '@/components/utility/select-person.vue'
//開發用的假數據
import dataJson from '@/assets/sample.json'
import showYear from'@/components/utility/show-year.vue'
import showSource from '@/components/utility/show-source.vue'
export default {
  name: 'entityQueryByPerson',
  components:
  {
    selectPerson,
    showYear,
    showSource
  },
  data () {
    return {
      //控制加載標誌的出現
      isBusy: false,
      /*表單數據放這裡*/
      formData:{
        personId:'',
        personNameEn:'',
        personNameCh:'',
        personIndexYear:''
      },
      //後端傳回來的數據放這裡
      personInfo:{

      },
      //控制当前显示哪个 tab
      activeTab:'baseInfo',
      tabIsloading:false
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
      if(isF === 0)return this.$t('globalTerm.male');
      else if (isF === 1)return this.$t('globalTerm.female');
      else return ''
    },
    //判斷是否
    isOrNot(str){
      if(str === "false")return this.$t('globalTerm.false');
      else if (str === "true")return this.$t('globalTerm.true');
      else return ''
    },
    isNull:isNull,
    //获取查询的人物
    handleGetPerson: function(selectedPerson){
      this.formData.personId = selectedPerson[0]['personId'];
      this.formData.personNameEn = selectedPerson[0]['personName'];
      this.formData.personNameCh = selectedPerson[0]['personNameCh'];
      this.formData.personIndexYear = selectedPerson[0]['indexYear'];
    },
    //To Do
    async handleSubmit(){
      //提交表单的时候先清空原有數據
      this.personInfo = {}
      this.isBusy = true;
      //加了async修饰符res变成结果？
      //const res = this.waitForServer(this.formData)
      this.axios.get('http://162.105.134.121/basicinformation/'+this.formData.personId)
      .then((r)=>
        { console.log(r.data)
          this.personInfo = r.data
          this.isBusy = false
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
          if(success)resolve({status:'200',data:dataJson})
          else reject({status:'404'})
        },100)
      })
    },
    //To Do
    loadMore(api,type,page){
        return new Promise(function(resolve){
        setTimeout(()=>{resolve('loaded')},100)
      })
    },
    //To Do
    handleScroll(){
      if (!this.$refs.res) return
      console.log(Object.keys(this.personInfo).length == 0)
      let heightTop = document.documentElement.scrollTop || document.body.scrollTop;
      let bottomOfWindow = document.documentElement.offsetHeight -heightTop - window.innerHeight <= 0
      if (bottomOfWindow && this.tabIsloading == false) {
        this.tabIsloading = true 
        let res = this.loadMore('https://randomuser.me/api/',this.activeTab,undefined)
        res.then(response => {
          //To Do
          for(let i = 0; i<5;i++)
            this.personInfo.address.push({
              "placeName":"Daxing",
              "placeNameChn":"大興",
              "type":"Basic Affiliation",
              "typeChn":"籍貫（基本地址）",
              "isMaternal":"false",
              "sequence":"0",
              "pFromYear":"0",
              "pFyRange":"-1",
              "pFyNh":"unknown",
              "pFyNhChn":"未詳",
              "pFyNhYear":"1",
              "pFyIntercalary":"true",
              "pFyMonth":"1",
              "pFyDay":"1",
              "pFyDayGz":"",
              "pToYear":"0",
              "pTyRange":"",
              "pTyNh":"unknown",
              "pTyNhChn":"未詳",
              "pTyNhYear":"",
              "pTyIntercalary":"false",
              "pTyMonth":"",
              "pTyDay":"",
              "pTyDayGz":"",
              "pSource":"Renming quanwei ziliao (Zhongyang yanjiuyuan Lishi yuyan yanjiusuo)",
              "pSourceChn":"人名權威資料（中央研究院歷史語言研究所）",
              "psPages":"9537",
              "pNotes":"北直隸·順天府（祖籍南直隸·鳳陽府）（中央研究院人名權威資料）。"
            })      
          this.tabIsloading = false   
        })      
      }    
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll,true)
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
