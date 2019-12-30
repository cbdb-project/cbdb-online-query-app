<template>
  <div class="hello">
    <b-breadcrumb :items="items" class = "bread-crumb"></b-breadcrumb>
    <b-card header-tag="header" footer-tag="footer">
      <template v-slot:header>
        <h6 class="mb-0">QUERY INPUT</h6>
      </template>
      <b-card-text class = "card-item-title">Query Condition Options</b-card-text>             
      <div class = "card-item-body">
        <b-row>
          <b-col><select-person></select-person></b-col>
          <b-col><select-place></select-place></b-col>
          <b-col><select-entry></select-entry></b-col>
        </b-row>
        <b-row>
          <b-col><select-office></select-office></b-col>
          <b-col><select-time></select-time></b-col>
          <b-col><select-relationship></select-relationship></b-col>
        </b-row>
      </div>
      <b-card-text class = "card-item-title">User Input</b-card-text>             
      <div class  = "card-item-body px-3">
        <b-row class = "px-3 mb-3">
          <b-col>
            <label for="office-en-name" class = "user-input-label">官職名-英文:</label>
            <b-form-input id="office-en-name" v-model="formData.officeEnName" placeholder="Enter your name"></b-form-input>
            </b-col>
          <b-col>
             <label for="office-ch-name" class = "user-input-label">官職名-中文:</label>
             <b-form-input id="office-ch-name" v-model="formData.officeChName" placeholder="Enter your name"></b-form-input>
           </b-col>
        </b-row>
        <b-row class = "px-3 mb-3">
          <b-col>
            <label for="office-en-type" class = "user-input-label">官職類型-英文:</label>
            <b-form-input id="office-en-type" v-model="formData.officeEnType" placeholder="Enter your name"></b-form-input>
            </b-col>
          <b-col>
             <label for="office-ch-type" class = "user-input-label">官職類型-中文:</label>
             <b-form-input id="office-ch-type" v-model="formData.officeChType" placeholder="Enter your name"></b-form-input>
           </b-col>
        </b-row>
        <b-row class = "px-3 mb-3">
          <b-col>
            <label for="office-en-place" class = "user-input-label">官職地點-英文:</label>
            <b-form-input id="office-en-place" v-model="formData.officeEnPlace" placeholder="Enter your name"></b-form-input>
            </b-col>
          <b-col>
             <label for="office-ch-place" class = "user-input-label">官職地點-中文:</label>
             <b-form-input id="office-ch-place" v-model="formData.officeChPlace" placeholder="Enter your name"></b-form-input>
           </b-col>
        </b-row>
        <b-row class = "px-3 mb-3">
          <b-col>
            <label for="person-en-place" class = "user-input-label">人物地點-英文:</label>
            <b-form-input id="person-en-place" v-model="formData.personEnPlace" placeholder="Enter your name"></b-form-input>
            </b-col>
          <b-col>
             <label for="person-ch-place" class = "user-input-label">人物地點-中文:</label>
             <b-form-input id="person-ch-place" v-model="formData.personChPlace" placeholder="Enter your name"></b-form-input>
           </b-col>
        </b-row>
        <b-row class = "px-3 mb-3">
          <b-col>
            <label for="start-time" class = "user-input-label">開始時間:</label>
            <b-form-input id="start-time" v-model="formData.startTime" placeholder="Enter your name"></b-form-input>
            </b-col>
          <b-col>
             <label for="end-time" class = "user-input-label">結束時間:</label>
             <b-form-input id="end-time" v-model="formData.endTime" placeholder="Enter your name"></b-form-input>
           </b-col>
           <b-col>
            <b-form-checkbox id="checkbox-1" v-model= "formData.indexYear" name="checkbox-1"
              value="t" unchecked-value="f" style = "margin:38px 0;text-align:left">
                使用指數年
            </b-form-checkbox>
           </b-col>
           <b-col></b-col>
        </b-row>
      </div>
      <b-card-text class = "card-item-title">Check and Search</b-card-text>
      <b-row class = "px-3 mb-3">
        <b-col cols="10">
          <b-alert show variant="warning" style = "width:40%" class = "px-3 py-2 mb-2">茲生成查詢式如下，請於檢索前核查確認</b-alert>
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
            <b-button href="#" variant="primary" style = "width:100%;margin-top:70px">Go</b-button>
        </b-col>
      </b-row>    
      <!--
      <template v-slot:footer>
        <em>Footer Slot</em>
      </template>
      -->
    </b-card>
    <query-result></query-result>   
  </div>
</template>

<script>
import queryResult from './query-result.vue'
import selectPerson from './select-person.vue'
import selectEntry from './select-entry.vue'
import selectOffice from './select-office.vue'
import selectTime from './select-time.vue'
import selectPlace from './select-place.vue'
import selectRelationship from './select-relationship.vue'
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
      },
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
  computed:{
    user(){
      return this.$store.state.user
    },
    queryFormular(){
      return `office-ch-name:'${this.formData.officeChName}',office-en-name:'${this.formData.officeEnName}',office-ch-type:'${this.formData.officeChType}',office-en-type:'${this.formData.officeEnType}',office-ch-place:'${this.formData.officeChPlace}',office-en-place:'${this.formData.officeEnPlace}',person-ch-place:'${this.formData.personChPlace}',person-en-place:'${this.formData.personEnPlace}',start-time:'${this.formData.startTime}',end-time:'${this.formData.endTime}'index-year:'${this.formData.indexYear}';`
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
