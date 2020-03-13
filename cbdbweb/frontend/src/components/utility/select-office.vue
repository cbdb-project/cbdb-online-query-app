<template>
    <div>
      <b-button-group>
        <b-button v-if="selectFromDb"  variant="outline-primary"  v-b-modal.select-office-table
            class = "query-condition-button" size="sm">{{$t('globalTerm.selectFromDb')}}
        </b-button>
        <b-button v-if="importList"  variant="outline-primary"  
            class = "query-condition-button" size="sm">{{$t('globalTerm.import')}}
        </b-button>
      </b-button-group>
        <b-modal 
          scrollable
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
                      <b-button variant="primary">Find</b-button>
                    </b-form-group>
                  </b-card>
                  <b-card>
                    <div style="height:310px; overflow:scroll">
                        <tree-table listName="官职类目表" ref="recTree" :list.sync="treeDataSource"  @handlerExpand="handlerExpand" @actionFunc="actionFunc"></tree-table>
                    </div>
                  </b-card>
                </b-col>
                <b-col :cols=8>
                    <b-form-group style = "text-align:right">
                      <b-button variant="outline-danger" @click="items=[]" size='sm' class = "mx-3" style="position:absolute;left:0">Clear Table</b-button> 
                      <b-button-group> 
                        <b-button v-if="selectedOffice.length>0" @click="clearSelected" variant="outline-secondary" size='sm' ><span>Cancel Selected</span></b-button>
                        <b-button v-if="!(items.length===selectedOffice.length)" @click="selectAllRows" variant="outline-secondary" size='sm' ><span>Select All</span></b-button>
                      </b-button-group>      
                    </b-form-group>
                    <b-table 
                        :items= "items" 
                        :fields= "fields"
                        sticky-header = "470px"
                        head-variant="light" 
                        id = "st"
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
        default:false
      }
    },
    data() {
        return {
          show:false,
          first:true,
          treeDataSource: {},
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
          ],
          items: [
            {pId:'1234',officeName:"Supervisor (Hucker)",officeNameCh:"提舉"},
            {pId:'1235',officeName:"Investigations Office of the State Finance Commission",officeNameCh:"三司推勘院"},
            {pId:'1236',officeName:"Comptroller",officeNameCh:"催欠司"},
            {pId:'1237',officeName:"General Comptroller‘s Office of the State Finance Commission (Hucker)",officeNameCh:"三司都勾院"},
            {pId:'1238',officeName:"General Deficits Monitoring Office of the State Finance Commission (Hucker)",officeNameCh:"三司都理欠司"},
            {pId:'1239',officeName:"General Accounting Office of the State Finance Commission (Hucker)",officeNameCh:"三司都磨勘司"},
            {pId:'1240',officeName:"Recorder of the Directorate of Waterways (Hucker)　",officeNameCh:"都水監主簿"},
            {pId:'1241',officeName:"Institute of General Accounts",officeNameCh:"三司度支勾院"},
            {pId:'1242',officeName:"Certificate Validation Office of the Bureau of General Accounts (Hucker)",officeNameCh:"度支憑由司"},
            {pId:'1243',officeName:"Judge of the Bureau of General Accounts (Hucker)",officeNameCh:"度支推官"},
          ],
          //选中的人物出现在这里
          selectedOffice : []
        }
    },
    components: {
        treeTable
    },
    methods: {
        // 模拟後台加載職官樹
        loadOfficeTree(){
          if(localStorage.officeTree!=undefined)this.treeDataSource = JSON.parse(localStorage.officeTree)
          else{
            let getOfficeTree = new Promise(function(resolve){
              setTimeout(()=>{resolve(dataJson)},3000)
            })
            getOfficeTree.then(resolve => {this.treeDataSource = resolve;localStorage.officeTree = JSON.stringify(resolve)})
          }
        },
        onRowSelected(items) {
          //用户选中列表中的条目后，同步到selectedOffice中
          this.selectedOffice = items
        },
        haveSelected: function(){
          //同步选中官职给父组件（页面）
          this.$emit('getOfficeName', {fields:this.fields,items:this.selectedOffice});
          this.show = false;
        },
        selectAllRows() {
            this.$refs.selectableTable.selectAllRows()
        },
        clearSelected() {
            this.$refs.selectableTable.clearSelected()
        },
        handlerExpand(m) {
            //console.log(m.Id+'展开/收缩')  
            m.isExpand = !m.isExpand
        },
        actionFunc(m){
            console.log(m.Id)
            this.axios.get('api'+m.Id)
            .then((r)=>{
              this.items = r.data
              },
              (e)=>{
                alert('Sorry, something went wrong...')
              }
            )
        },
        handleTableScroll(e){
          //let table = document.getElementById('select-office-table')
          //let st = table.scrollTop
          //console.log(st)
        }
    },
    created(){
      this.loadOfficeTree();
    },
    watch:{
      //DOM elements first time rendered
      show:function(){
        if(this.first===true){
        this.first=false
        let st =  this.$refs.selectableTable
        // 监听这个dom的scroll事件
        st.$el.addEventListener('scroll', () => {
          if(st.$el.scrollHeight - st.$el.scrollTop <= st.$el.clientHeight)
            console.log('ooooo')
        }, false)
        }
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