<template>
    <div>
      <b-button-group>
        <b-button v-if="selectFromDb"  variant="outline-primary"  v-b-modal.select-office-table
            class = "query-condition-button" size="sm">{{$t('globalTerm.selectFromDb')}}
        </b-button>
        <b-button v-if="importList"  variant="outline-primary"  
            class = "query-condition-button" size="sm">{{$t('selectOffice.selectButton')}}
        </b-button>
      </b-button-group>
        <b-modal 
          id="select-office-table" 
          title="Select Office from Database" 
          size = "xl"
          v-model="show"  
        >
            <b-row>
                <b-col :cols = 4 style = "text-align:right">
                  <b-card>
                    <b-form-group label-cols="4" :label="$t('selectOffice.officeName')" label-for="select-office-input-ch-name">
                        <b-form-input id="select-office-input-ch-name"></b-form-input>
                    </b-form-group>
                    <b-form-group>
                      <b-button variant="primary">Search</b-button>
                    </b-form-group>
                  </b-card>
                  <b-card>
                    <div style="height:400px; overflow:auto">
                        <tree-table listName="官职类目表" ref="recTree" :list.sync="treeDataSource" @actionFunc="actionFunc" @deleteFunc="deleteFunc" @handlerExpand="handlerExpand" @orderByFunc="orderByFunc"></tree-table>
                    </div>
                  </b-card>
                </b-col>
                <b-col :cols=8 >
                    <b-table 
                        :items= "items" 
                        :fields= "fields" 
                        sticky-header = "600px"
                        head-variant="light" 
                        ref="selectableTable"
                        selectable
                        select-mode="multi"
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
              <b-button size="xl" variant="secondary" @click="show=false">
                Cancel
              </b-button>
              <b-button size="xl" variant="primary" @click="haveSelected">
                Select
              </b-button>
            </template>
        </b-modal>
    </div>
</template>

<script>
import dataJson from '../views/officeData.json'
import treeTable from '../treeTable/tree-table.vue'
export default {
    name:'selectOffice',
    props:{
      'selectFromDb':{
        default:true
      },
      'importList':{
        default:true
      }
    },
    data() {
        return {
          show:false,
          treeDataSource: dataJson,
          /*表格子數據放這裡*/
          fields: [
            {
              key: 'officeName',
              label:'Office Name',
              sortable: true
            },
            {
              key: 'officeNameCh',
              label:'官名',
              sortable: true
            },
            {
              key: 'selected',
              sortable: false,
            }
          ],
          items: [
            {officeName:"Supervisor (Hucker)",officeNameCh:"提舉"},
            {officeName:"Investigations Office of the State Finance Commission",officeNameCh:"三司推勘院"},
            {officeName:"Comptroller",officeNameCh:"催欠司"},
            {officeName:"General Comptroller‘s Office of the State Finance Commission (Hucker)",officeNameCh:"三司都勾院"},
            {officeName:"General Deficits Monitoring Office of the State Finance Commission (Hucker)",officeNameCh:"三司都理欠司"},
            {officeName:"General Accounting Office of the State Finance Commission (Hucker)",officeNameCh:"三司都磨勘司"},
            {officeName:"Recorder of the Directorate of Waterways (Hucker)　",officeNameCh:"都水監主簿"},
            {officeName:"Institute of General Accounts",officeNameCh:"三司度支勾院"},
            {officeName:"Certificate Validation Office of the Bureau of General Accounts (Hucker)",officeNameCh:"度支憑由司"},
            {officeName:"Judge of the Bureau of General Accounts (Hucker)",officeNameCh:"度支推官"},
          ],
          //选中的人物出现在这里
          selectedOffice : []
        }
    },
    components: {
        treeTable
    },
    methods: {
        onRowSelected(items) {
          //用户选中列表中的条目后，同步到selectedOffice中
          this.selectedOffice = items
        },
        haveSelected: function(){
          //同步选中官职给父组件（页面）
          console.log("成功");
          this.$emit('getOfficeName', this.selectedOffice);
          this.show = false;
        },
        selectAllRows() {
            this.$refs.selectableTable.selectAllRows()
        },
        clearSelected() {
            this.$refs.selectableTable.clearSelected()
        },
        handlerExpand(m) {
            console.log('展开/收缩')
            m.isExpand = !m.isExpand
        }
    }
}
</script>

<style scoped>
.query-condition-button{
  width:128px;
  margin:6px 0;
}
</style>