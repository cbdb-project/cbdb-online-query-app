<template>
  <div class="hello">
    <!--
    <h1>{{ user.name }}：</h1>
    <h2>歡迎使用 CBDB Web 查詢系統</h2>
    <ul>
      <li>
        <a
          href="https://vuejs.org"
          target="_blank"
        >
          Core Docs
        </a>
      </li>
      <li>
        <a
          href="https://forum.vuejs.org"
          target="_blank"
        >
          Forum
        </a>
      </li>
      <li>
        <a
          href="https://chat.vuejs.org"
          target="_blank"
        >
          Community Chat
        </a>
      </li>
      <li>
        <a
          href="https://twitter.com/vuejs"
          target="_blank"
        >
          Twitter
        </a>
      </li>
      <br>
      <li>
        <a
          href="http://vuejs-templates.github.io/webpack/"
          target="_blank"
        >
          Docs for This Template
        </a>
      </li>
    </ul>
    <h2>這是首頁</h2>
    <ul>
      <li>
        <a
          href="http://router.vuejs.org/"
          target="_blank"
        >
          vue-router
        </a>
      </li>
      <li>
        <a
          href="http://vuex.vuejs.org/"
          target="_blank"
        >
          vuex
        </a>
      </li>
      <li>
        <a
          href="http://vue-loader.vuejs.org/"
          target="_blank"
        >
          vue-loader
        </a>
      </li>
      <li>
        <a
          href="https://github.com/vuejs/awesome-vue"
          target="_blank"
        >
          awesome-vue
        </a>
      </li>
    </ul>
    -->
    <h1>欢迎使用 中國歷代人物傳記查询</h1>
    <b-card header-tag="header" footer-tag="footer">
      <template v-slot:header>
        <h6 class="mb-0">人物信息</h6>
      </template>
    <b-card-text  class = "card-item-title">
    </b-card-text>
    <div>
    <div class  = "card-item-body px-3" v-if = "personInfo">
        <h2 v-if="personInfo.BasicInfo">
          {{personInfo.BasicInfo.ChName}}
        </h2>
        <b-row>
          <b-col >ID:<b>{{formData.personId}}</b></b-col>
          <b-col v-if="personInfo.PersonAliases">
            {{personAliasType(personInfo.PersonAliases.Alias)}}:<b>
              {{personAliasName(personInfo.PersonAliases.Alias)}} 
            </b></b-col>
        </b-row>
        <b-row>
          
          <b-col>指数年：<b>
            {{personInfo.BasicInfo.IndexYear}}
          </b></b-col>
          <b-col>朝代：<b>
            {{personInfo.BasicInfo.Dynasty}}
          </b></b-col>
        </b-row>
        <b-row>
          <b-col>性别：<b>
            {{personGen(personInfo.BasicInfo.Gender)}}
          </b></b-col>
          <b-col v-if="personInfo.PersonAddresses.Address">籍贯：<b>
            {{Address(personInfo.PersonAddresses.Address)}}
          </b></b-col>
        </b-row>
        <b-row>
          <b-col v-if="personInfo.PersonSources.Source">来源：<b>
            {{personInfo.PersonSources.Source.Source}}
          </b></b-col>
        </b-row>
      </div>
        <b-row>
          <b-button href="#" variant="primary" 
              style = "width:100%;margin-top:16px"
              @click="fresh">换一换</b-button>
        </b-row>
    </div>
    </b-card>
  </div>
</template>

<script>
import {isNull} from '@/components/utility/utility-functions.js'
import selectPerson from '@/components/utility/select-person.vue'
export default {
  name: 'HelloWorld',
  data () {
    return {
      isBusy: false,
      formData:{
        personId:'' , 
      },
      personInfo:{
      }
    }
  },
  mounted: function(){ 
      this.formData.personId = Math.floor(Math.random()*30000);
      this.isBusy = true;
      this.axios.get('https://cbdb.fas.harvard.edu/cbdbapi/person.php?id='+this.formData.personId +'&o=json')
      .then((r)=>
        { 
          this.personInfo = r.data.Package.PersonAuthority.PersonInfo.Person
          this.isBusy = false
          if(this.personInfo === "" || this.personInfo === undefined || this.personInfo.BasicInfo === undefined ){
            this.fresh();
          }
        },
        (e)=>{
          alert('something went wrong...')
          this.isBusy = false
        })
    },
  methods:{
    personGen(isF){
      if(isF === 0||isF === '0')return this.$t('globalTerm.male');
      else if (isF === 1||isF === '1')return this.$t('globalTerm.female');
      else return ''
    },
    Address(add){
      if(add === '') return '未详';
      else if(Array.isArray(add))return add[0].AddrName;
      else return add.AddrName; 
    },
    personAliasType(alias){

        if(alias === '')return '字';
        else if(Array.isArray(alias))return alias[0].AliasType;
        else return alias.AliasType;
    },
    personAliasName(alias){
      if(alias === '')return '未详';
      else if(Array.isArray(alias))return alias[0].AliasName;
      else return alias.AliasName;
    },
    fresh() {
      //提交表单的时候先清空原有數據
      this.personInfo = {};
      //加了async修饰符res变成结果？
      //const res = this.waitForServer(this.formData)
      this.formData.personId = Math.floor(Math.random()*30000);
      this.isBusy = true;
      console.log("1");
      this.axios.get('https://cbdb.fas.harvard.edu/cbdbapi/person.php?id='+this.formData.personId +'&o=json')
      .then((r)=>
        { 
          console.log("2")
          this.personInfo = r.data.Package.PersonAuthority.PersonInfo.Person
          this.isBusy = false
          if(this.personInfo === "" || this.personInfo === undefined || this.personInfo.BasicInfo === undefined ){
            this.fresh();
          }
        },
        (e)=>{
          alert('something went wrong...')
          this.isBusy = false
        })
  },
  },
  computed:{
    user(){
      return this.$store.state.local.user
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.col{
  text-align:left;
  margin:10px;
}
.hello{
  margin-top:24px;
}
h1, h2, h6 {
  text-align:left;
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}

</style>