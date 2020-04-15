<template>
    <div>
        <b-button v-if="selectFromDb" variant="outline-primary"  v-b-modal.select-relationship-table
        class = "query-condition-button" size="sm">{{$t('globalTerm.selectFromDb')}}</b-button>
        <b-modal 
            id="select-relationship-table" 
            title="Select Associations" 
            size="xl"
            v-model="show"
            >
            <b-row>
                <b-col :cols = 4 style = "text-align:right">
                  <b-card>
                    <b-form-group label-cols="4" :label="$t('selectRelationship.association')" label-for="select-relation-input">
                        <b-form-input id="select-relation-input"></b-form-input>
                    </b-form-group>
                    <b-form-group>
                      <b-button variant="primary">Search</b-button>
                    </b-form-group>
                  </b-card>
                  <b-card>
                    <div style="height:400px; overflow:auto">
                        <tree-table listName="社会关系类目表" ref="recTree" :list.sync="treeDataSource"></tree-table>
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
              <b-button size="xl" variant="secondary" @click="close">
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
import dataJson from '@/assets/relationData.json'
import treeTable from '../treeTable/tree-table.vue'
export default {
    name:'selectRelationship',
    props:{
        'selectFromDb':{
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
            key: 'rId',
            label:'Assoc. Code',
            sortable: true
          },
          {
            key: 'rName',
            label:'Assoc. Name',
            sortable: true
          },
          {
            key: 'rNameCh',
            label: '社會關係名',
            sortable: true,
          }
        ],
        //rId 相當於 C_ASSOC_CODE
        items: [
          {rId:'-1',rName:'[Missing Data]',rNameCh:'[缺乏信息]'},
          {rId:'0',rName:'[Undefined]',rNameCh:'[未詳]'},
          {rId:'1',rName:'Listed in Yuanyou colition register',rNameCh:'入元祐黨籍者'},   
          {rId:'2',rName:'Yuanfu colition member (元符黨)',rNameCh:'元符上書入籍'},      
        ],
        //选中的关系出现在这里
        selectedRelation : []
        }
    },
    components: {
        treeTable
    },
    methods: {
        close:function(){
            this.selectedRelation.splice(0,this.selectedRelation.length)
            this.show = false;
        },
        onRowSelected(items) {
            this.selectedRelation = items
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
        },
        haveSelected: function(){
            //同步选中入仕途径
            console.log("选取成功");
            this.$emit('getRelation', {fields:this.fields,items:this.selectedRelation});
            this.close()
          },
    } 
}
</script>

<style scoped>
.query-condition-button{
  width:128px;
  margin:6px 0;
}
</style>