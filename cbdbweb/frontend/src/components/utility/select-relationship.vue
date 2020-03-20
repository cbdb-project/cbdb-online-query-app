<template>
    <div>
        <b-button v-if="selectFromDb" variant="outline-primary"  v-b-modal.select-relationship-table
        class = "query-condition-button" size="sm">{{$t('globalTerm.selectFromDb')}}</b-button>
        <b-modal id="select-relationship-table" title="BootstrapVue" size="xl">
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
                        <tree-table listName="社会关系类目表" ref="recTree" :list.sync="treeDataSource" @actionFunc="actionFunc" @deleteFunc="deleteFunc" @handlerExpand="handlerExpand" @orderByFunc="orderByFunc"></tree-table>
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
        treeDataSource: dataJson,
        /*表格子數據放這裡*/
        fields: [
          {
            key: 'name',
            label:'Name',
            sortable: true
          },
          {
            key: 'nameCh',
            label:'姓名',
            sortable: true
          },
          {
            key: 'indexYear',
            label: 'Index Year',
            sortable: true,
          },
          {
            key: 'female',
            label:'Female',
            sortable: true
          },
          {
            key: 'placeType',
            label:'地名類',
            sortable: true
          },
          {
            key: 'personPlace',
            label: 'Place(Person)',
            sortable: true,
          },
          {
            key: 'personPlaceCh',
            label: '地名(人)',
            sortable: true,
          },
            {
            key: 'selected',
            sortable: false,
          }
        ],
        items: [
          {name:'Liu Jun',nameCh:'劉俊',indexYear:'1086',female:false,placeType:'籍貫',personPlace:'Nan Yang',personPlaceCh:'南陽'},
          {name:'Jiang Can',nameCh:'蔣璨',indexYear:'1114',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'},        
          {name:'Jiang Can',nameCh:'蔣璨',indexYear:'1114',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'},       
          {name:'Jiang Can',nameCh:'蔣璨',indexYear:'1114',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
          {name:'Jiang Can',nameCh:'蔣璨',indexYear:'1114',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
          {name:'Jiang Can',nameCh:'蔣璨',indexYear:'1114',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
          {name:'Jiang Can',nameCh:'蔣璨',indexYear:'1114',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
          {name:'Jiang Can',nameCh:'蔣璨',indexYear:'1114',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
          {name:'Jiang Can',nameCh:'蔣璨',indexYear:'1114',female:false,placeType:'籍貫',personPlace:'Yi Xing',personPlaceCh:'宜興'}, 
        ],
        //选中的人物出现在这里
        selected : []
        }
    },
    components: {
        treeTable
    },
    methods: {
        onRowSelected(items) {
            this.selected = items
            //要把选中的结果传递给调用的父组件
            console.log(this.selected)
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