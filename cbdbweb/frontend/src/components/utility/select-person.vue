<template>
    <div>
      <b-button-group>      
        <b-button  v-if="selectFromDb===true" variant="outline-primary"  v-b-modal.select-person
        class = "query-condition-button" size="sm">{{$t('globalTerm.selectFromDb')}}</b-button>
        <b-button  v-if="importList===true" variant="outline-primary"  v-b-modal.select-person
        class = "query-condition-button" size="sm">{{$t('globalTerm.import')}}</b-button>
      </b-button-group>
        <b-modal 
          id="select-person" 
          title="Select People from Database" 
          size = "xl"
          v-model="show"
          scrollable
        >
            <b-row>
                <b-col :cols = 5 style = "text-align:right">
                  <b-card>
                    <b-form-group label-cols="4" :label="$t('selectPerson.personName')" label-for="select-person-input-name">
                        <b-form-input id="select-person-input-name" :placeholder="$t('globalTerm.cnOrPy')" v-model="formData.personName"></b-form-input>
                    </b-form-group>
                     <a v-b-tooltip.hover  :title="isInvalid?$t('globalTerm.invalidInput'):''">
                      <b-button variant="primary" @click="searchPerson(formData.personName)"
                      :disabled="isInvalid||isBusy" style = "width:96px">
                        <span v-if="!isBusy">Go</span>
                        <b-spinner small v-if="isBusy"></b-spinner>
                      </b-button>
                     </a>
                  </b-card>
                </b-col>
                <b-col :cols = 7>
                    <b-table 
                        :items= "items" 
                        :fields= "fields" 
                        sticky-header = "1000px"
                        head-variant="light" 
                        ref="selectableTable"
                        selectable
                        :select-mode="selectMode"
                        @row-selected="onRowSelected"
                        responsive="sm">
                        <template v-slot:cell(selected)="{ rowSelected }">
                            <template v-if="rowSelected">
                            <span aria-hidden="true">&check;</span>
                            <span class="sr-only">Selected</span>
                            </template>
                            <template v-else>
                            <span aria-hidden="true">&nbsp;</span>
                            <span class="sr-only">Not selected</span>
                            </template>
                        </template>
                    </b-table>
                </b-col>
            </b-row>
            <template v-slot:modal-footer>
              <b-button size="xl" variant="secondary" @click="close">
                Cancel
              </b-button>
              <b-button size="xl" variant="primary" :disabled="selectedPerson.length===0" @click="haveSelected">
                Select
              </b-button>
            </template>
        </b-modal>
    </div>
</template>

<script>
import dataJson from '@/assets/person_list_dev.json'
import {isNull} from '@/components/utility/utility-functions.js'
export default {
    name:'selectPerson',
    props:{
      'selectMode':{
        default:'multi'
      },
      'selectFromDb':{
        default:true
      },
      'importList':{
        default:true
      }
    },
  data () {
    return {
      show:false,
      isBusy: false,
      formData:{
        personName:''
      },
      /*表格子數據放這裡*/
        fields: [
          {
            key: 'personId',
            label:'ID',
            sortable: true
          },
          {
            key: 'personName',
            label:'Name',
            sortable: true
          },
          {
            key: 'personNameCh',
            label:'姓名',
            sortable: true
          },
          {
            key: 'indexYear',
            label: 'Index Year',
            sortable: true,
          }
        ],
        items: [],
        //选中的人物出现在这里
        selectedPerson : []
    }
  },
  methods: {
      close:function(){
        this.selectedPerson.splice(0,this.selectedPerson.length)
        this.show = false;
      },
      searchPerson(personName){
        this.items = []//清空已有数据
        this.isBusy=true
        this.axios.get('https://cbdb.fas.harvard.edu/cbdbapi/person.php?name='+ encodeURI(this.formData.personName) +'&o=json')
        .then((r)=>
          {
            console.log(r.data.Package.PersonAuthority.PersonInfo.Person)
            let pList = r.data.Package.PersonAuthority.PersonInfo.Person
            if(pList instanceof Array){
              this.items = pList.map(item=>
              ({'personId':item.BasicInfo.PersonId,'personName':item.BasicInfo.EngName,'personNameCh':item.BasicInfo.ChName,'indexYear':item.BasicInfo.IndexYear}))
            }
            else{
              this.items.push({'personId':pList.BasicInfo.PersonId,'personName':pList.BasicInfo.EngName,'personNameCh':pList.BasicInfo.ChName,'indexYear':pList.BasicInfo.IndexYear})
            }
            this.isBusy = false
          },
          (e)=>{
            alert('something went wrong...')
            this.isBusy = false
          }
        )
      },
      onRowSelected(items) {
        this.selectedPerson = items
      },
      haveSelected: function(){
        //同步选中人物
        console.log("成功");
        this.$emit('getPersonName', {fields:this.fields,items:this.selectedPerson});
        this.selectedPerson.splice(0,this.selectedPerson.length)
        this.show = false;
      },
      selectAllRows() {
        this.$refs.selectableTable.selectAllRows()
      },
      clearSelected() {
        this.$refs.selectableTable.clearSelected()
      }
  },
  computed:{
    isInvalid(){
      return isNull(this.formData.personName)
    }
  }
}
</script>

<style scoped>
.query-condition-button{
  width:128px;
  margin:6px 0;
  /* 和表單中的輸入框對齊 */
}
</style>