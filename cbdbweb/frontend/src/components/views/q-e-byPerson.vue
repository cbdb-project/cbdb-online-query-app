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
        <b-row class = "px-3 mb-3">
          <b-col>
            <label for="person-en-name" class = "user-input-label">{{$t('entityQueryByPerson.personNameEn')}}:</label>
            <b-form-input id="person-en-name" v-model="formData.personEnName" placeholder="Enter your name"></b-form-input>
            </b-col>
          <b-col>
             <label for="person-ch-name" class = "user-input-label">{{$t('entityQueryByPerson.personNameCh')}}:</label>
             <b-form-input id="person-ch-name" v-model="formData.personChName" placeholder="Enter your name"></b-form-input>
           </b-col>
            <b-col><select-person
            @getPersonName="handleGetPerson"></select-person></b-col>
        </b-row>
      </div>
      <b-card-text class = "card-item-title">{{$t('entityQueryByPerson.checkAndSearch')}}</b-card-text>
      <b-row class = "px-3 mb-3">
        <b-col cols="10">
          <b-alert show variant="warning" style = "width:66%" class = "px-3 py-2 mb-2">{{$t('entityQueryByPerson.checkRemind')}}</b-alert>
          <b-form-textarea
                id="advanced-search"
                v-model= "queryFormular"
                placeholder=""
                rows="3"
                max-rows="6"
                disabled
              ></b-form-textarea>
        </b-col>
        <b-col cols="2">
            <b-button href="#" variant="primary" style = "width:100%;margin-top:70px" :disabled="isInvalid">Go</b-button>
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
        <b-card-text class = "card-item-title">{{$t('entityQueryByPerson.result.basicInfo')}}</b-card-text> 
      <div class  = "card-item-body px-3">
        <b-row class = "px-3 mb-3">
          <b-col>

          </b-col>
          <b-col>

          </b-col>
          <b-col>

          </b-col>
        </b-row>
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
        personEnName:'',
        personChName:'',
      },
      //後端傳回來的數據放這裡
      personInfo:{
        birthDeathYears:{
          cSurname:"Zhu",
          cSurnameChn:"朱",
          cMingzi:"Youxiao",
          cMingziChn:"由校",
          cIndexYear:"1627",
          cFemale:"false",
          cEthnicityCode:"0",
          cBirthyear:"1605",
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
          cDeathYear:"1104",
          cDyNh:"",
          cDyNhChn:"天啟",
          cDyNhYear:"7",
          cDyRange:"",
          cDeathAge:"23",
          cDeathAgeRange:"",
          cFlEarliestYear:"",//?
          cFlEyNh:"",//年號
          cFlEyNhYear:"",//多少年,
          cFlEyNotes:"",
          cFlLatestYear:"",//?
          cFlLyNh:"",//年號
          cFlLyNhYear:"",//多少年,
          cFlLyNotes:"",   
          cNotes:"Zhu(1) Yoiuxiao [30164] Xizong or the Tianqi Emperor.See Documentation for Zhu(1) Yuanzhang [30149]."
        },
        Address:[
          {
            placeName:"Daxing",
            placeNameChn:"大興",
            type:"Basic Affiliation",
            typeChn:"籍貫（基本地址）",
            isMaternal:"false",
            sequence:"0",
            pFromYear:"0",
            pFyRange:"",
            pFyNh:"unknown",
            pFyNhChn:"未詳",
            pFyNhYear:"",
            pFyIntercalary:"false",
            pFyMonth:"",
            pFyDay:"",
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
            pSPages:"9537",
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
            nSPages:"9537",
            nNotes:"參見《新校本明史》"
          },
          {
            name:"Datianchandaodunxiaoduyouzhangwenxiangwujingmuzhuangqinzhehuangdi",
            nameChn:"達天闡道敦孝篤友章文襄武靖穆莊勤哲皇帝",
            nType:"Posthumous Name",
            nTypeChn:"諡號",
            nSourceChn:"",
            nSPages:"",
            nNotes:""
          },
          {
            name:"Tianqi",
            nameChn:"天啓",
            nType:"Unknown",
            nTypeChn:"未詳",
            nSourceChn:"人名權威資料（中央研究院歷史語言研究所）",
            nSPages:"9537",
            nNotes:"參見《新校本明史》"
          },
          {
            name:"Xi Zong",
            nameChn:"熹宗",
            nType:"Unknown",
            nTypeChn:"未詳",
            nSourceChn:"人名權威資料（中央研究院歷史語言研究所）",
            nSPages:"9537",
            nNotes:"參見《新校本明史》"
          },
          {
            name:"Xi Zong",
            nameChn:"熹宗",
            nType:"Temple Name",
            nTypeChn:"廟號",
            nSourceChn:"",
            nSPages:"",
            nNotes:""
          },
          {
            name:"Zhe Di",
            nameChn:"悊帝",
            nType:"Unknown",
            nTypeChn:"未詳",
            nSourceChn:"",
            nSPages:"",
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
        
      },
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
      this.formData.personEnName = selectedPerson[0]['personName'];
      this.formData.personChName = selectedPerson[0]['personNameCh'];
    }
  },
  computed:{
    queryFormular(){
      return `person-ch-name:'${this.formData.personChName}',person-en-name:'${this.formData.personEnName}';`
    },
    isInvalid(){
      return this.isNull('personEnName')==true && this.isNull('personChName')==true
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
