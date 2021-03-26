<template>
    <div>
      <b-button-group>      
        <b-button  v-if="selectFromDb===true" variant="outline-primary"  v-b-modal.select-person
        class = "query-condition-button" size="sm">{{$t('globalTerm.selectFromDb')}}</b-button>
        <b-button  v-if="importList===true" variant="outline-primary"  v-b-modal.import-person
        class = "query-condition-button" size="sm">{{$t('globalTerm.import')}}</b-button>
      </b-button-group>
      <!-- Select People  -->
      <b-modal 
          id="select-person" 
          title="Select People from Database" 
          size = "xl"
          v-model="showSelect"
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
                        <span v-if="!isBusy">{{$t('globalTerm.search')}}</span>
                        <b-spinner small v-if="isBusy"></b-spinner>
                      </b-button>
                     </a>
                  </b-card>
                </b-col>
                <b-col :cols = 7>
                    <b-form-group style = "text-align:right">
                      <b-button variant="outline-danger" @click="onClearTable" size='sm' class = "mx-3" style="position:absolute;left:0">Clear Table</b-button> 
                      <b-button-group> 
                        <b-button v-if="this.selectedPerson.length>0" @click="clearSelected" variant="outline-secondary" size='sm' ><span>Cancel Selected</span></b-button>
                        <b-button v-if="!(this.items.length===this.selectedPerson.length)" @click="selectAllRows" variant="outline-secondary" size='sm' ><span>Select All</span></b-button>
                      </b-button-group>      
                    </b-form-group>
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
      <!-- Import People -->
      <b-modal 
          id="import-person" 
          title="Import People List" 
          size = "xl"
          v-model="showImport"
          scrollable
        >
            <b-row>
                <b-col :cols = 5 style = "text-align:right">
                  <b-card>
                    <div style = "text-align:left">
                      <div class="mt-3">
                       利用已有檢索結果
                      </div>
                    </div>
                    <b-button class="mt-3"
                    variant="primary" @click="importPerson"
                      :disabled="!(localPL&&localPL.length)" style = "width:96px">
                        <span>{{$t('globalTerm.parse')}}</span>
                    </b-button>                    
                  </b-card>
                  <b-card>
                    <div style = "text-align:left">
                      <b-form-file
                        ref = "upload"
                        v-model="file1"
                        :state="Boolean(file1)"
                        :placeholder="this.$t('selectPerson.importPersonPlaceholder')"
                        :drop-placeholder="this.$t('selectPerson.dropFileHere')"
                        :browse-text="this.$t('selectPerson.browseText')"
                        accept=".json"
                      ></b-form-file>
                      <div class="mt-3">
                        Selected file: {{ file1 ? file1.name : '' }}
                      </div>
                    </div>
                    <b-button class="mt-3"
                    variant="primary" @click="parsePerson"
                      :disabled="isInvalidFile||isBusy" style = "width:96px">
                        <span v-if="!isBusy">{{$t('globalTerm.parse')}}</span>
                        <b-spinner small v-if="isBusy"></b-spinner>
                    </b-button>                    
                  </b-card>
                  <b-alert
                  style = "text-align:left"
                  class = "mt-3"
                  show>
                    {{$t('selectPerson.warning')}}
                  </b-alert>
                </b-col>
                <b-col :cols = 7>
                    <b-form-group style = "text-align:right">
                      <b-button variant="outline-danger" @click="onClearTable" size='sm' class = "mx-3" style="position:absolute;left:0">Clear Table</b-button> 
                      <b-button-group> 
                        <b-button v-if="this.selectedPerson.length>0" @click="clearSelected" variant="outline-secondary" size='sm' ><span>Cancel Selected</span></b-button>
                        <b-button v-if="!(this.items.length===this.selectedPerson.length)" @click="selectAllRows" variant="outline-secondary" size='sm' ><span>Select All</span></b-button>
                      </b-button-group>      
                    </b-form-group>
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
import {
  isNull
} from '@/components/utility/utility-functions.js'
export default {
  name: 'selectPerson',
  props: {
    'selectMode': {
      default: 'multi'
    },
    'selectFromDb': {
      default: true
    },
    'importList': {
      default: true
    }
  },
  data() {
    return {
      localPL: localStorage.autoSavedPL,
      showSelect: false,
      showImport:false,
      isBusy: false,
      file1:undefined,
      formData: {
        personName: ''
      },
      /*表格子數據放這裡*/
      fields: [{
          key: 'personId',
          label: 'ID',
          sortable: true
        },
        {
          key: 'personName',
          label: 'Name',
          sortable: true
        },
        {
          key: 'personNameCh',
          label: '姓名',
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
      selectedPerson: []
    }
  },
  methods: {
    close: function() {
      this.selectedPerson.splice(0, this.selectedPerson.length)
      this.showSelect = false;
      this.showImport = false;
    },
    searchPerson(personName) {
      this.items = [] //清空已有数据
      this.isBusy = true
      this.axios.get('https://cbdb.fas.harvard.edu/cbdbapi/person.php?name=' + encodeURI(this.formData.personName) + '&o=json')
        .then((r) => {
            console.log(r.data.Package.PersonAuthority.PersonInfo.Person)
            let pList = r.data.Package.PersonAuthority.PersonInfo.Person
            if (pList instanceof Array) {
              this.items = pList.map(item =>
                ({
                  'personId': item.BasicInfo.PersonId,
                  'personName': item.BasicInfo.EngName,
                  'personNameCh': item.BasicInfo.ChName,
                  'indexYear': item.BasicInfo.IndexYear
                }))
            } else {
              this.items.push({
                'personId': pList.BasicInfo.PersonId,
                'personName': pList.BasicInfo.EngName,
                'personNameCh': pList.BasicInfo.ChName,
                'indexYear': pList.BasicInfo.IndexYear
              })
            }
            this.isBusy = false
          },
          (e) => {
            alert('something went wrong...')
            this.isBusy = false
          }
        )
    },
    onRowSelected(items) {
      this.selectedPerson = items
    },
    onClearTable() {
      clearResultTable(this)
    },
    haveSelected: function() {
      //同步选中人物
      //console.log("1");
      this.$emit('getPersonName', {
        fields: this.fields,
        items: this.selectedPerson
      });
      //console.log("2")
      this.selectedPerson.splice(0, this.selectedPerson.length)
      this.close();
    },
    selectAllRows() {
      this.$refs.selectableTable.selectAllRows()
    },
    clearSelected() {
      this.$refs.selectableTable.clearSelected()
    },
    parsePerson:function(){
      let reader = new FileReader();   //先new 一个读文件的对象 FileReader
      let vm = this;
      if (typeof FileReader === "undefined") {  //用来判断你的浏览器是否支持 FileReader
          alert(vm.$t('selectPerson.browserNotSupportFileReader'));
          return;
      }
      reader.onload = function (event) {
        let res = JSON.parse(event.target.result)
        if(!res['creator'] || res['creator']!='cbdb-online-query-app')
        {
          alert(vm.$t('selectPerson.cannotParse'));
          return;
        }
        vm.items = res.data;
      };
      reader.readAsText(this.file1);
      return;
    },
    importPerson:function(){
      this.items = JSON.parse(this.localPL).data;
    }
  },
  computed: {
    isInvalid() {
      return isNull(this.formData.personName)
    },
    isInvalidFile(){
      return this.file1?false:true;
    }
  },
  mounted() {

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