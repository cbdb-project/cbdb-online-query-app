<template>
    <div>
        <b-button v-if="selectFromDb===true" variant="outline-primary"  v-b-modal.select-entry-table
        class = "query-condition-button" size="sm">{{$t('globalTerm.selectFromDb')}}</b-button>
        <b-modal 
            scrollable
            id="select-entry-table" 
            title="Select Entry from Database" 
            size = "xl"
            v-model = "show"
        >
            <b-row>
                <b-col :cols = 4 style = "text-align:right">
                    <b-card>
                        <b-form-group label-cols="4" label="Entry Name" label-for="select-entry-input-en-name">
                            <b-form-input id="select-entry-input-name" v-model= "formData.eName"></b-form-input>
                        </b-form-group>
                        <b-form-group>
                            <b-button variant="primary" :disabled="isBusy||formData.eName===''" @click="find">
                                <span v-if="!isBusyFind">Find</span>
                                <b-spinner small v-else></b-spinner>
                            </b-button>
                        </b-form-group>
                    </b-card>
                    <b-card>
                        <div style="height:310px; overflow:scroll">
                            <tree-table listName="入仕途径类目表" ref="recTree" :list.sync="treeDataSource"  @handlerExpand="handlerExpand" @actionFunc="actionFunc"></tree-table>
                        </div>
                    </b-card>
                </b-col>
                <b-col :cols=8 >
                    <b-form-group style = "text-align:right">
                      <b-button variant="outline-danger" @click="onClearTable" size='sm' class = "mx-3" style="position:absolute;left:0">Clear Table</b-button> 
                      <b-button-group> 
                        <b-button v-if="this.selectedEntry.length>0" @click="clearSelected" variant="outline-secondary" size='sm' ><span>Cancel Selected</span></b-button>
                        <b-button v-if="!(this.items.length===this.selectedEntry.length)" @click="selectAllRows" variant="outline-secondary" size='sm' ><span>Select All</span></b-button>
                      </b-button-group>      
                    </b-form-group>
                    <b-row v-if="this.result.total!==undefined&&this.result.end!==undefined">
                      <b-col>
                        <b-link disabled>{{result.end}}</b-link><span style="color:#4D4D4D">&nbsp;of&nbsp;</span>
                        <b-link disabled>{{result.total}}</b-link><span style="color:#4D4D4D">&nbsp;records are shown.</span>
                      </b-col>
                    </b-row>
                    <b-table 
                        :items= "items" 
                        :fields= "fields" 
                        sticky-header = "470px"
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
                <b-row>
                    <b-col style="text-align:center">
                        <b-spinner small v-if="isBusyLoad"></b-spinner>
                    </b-col>
                </b-row>
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
    import dataJson from '@/assets/entryData.json'
    import treeTable from '../treeTable/tree-table.vue'
    import {getListById,appendListById,celarResultTable,getListByName} from '@/components/utility/utility-functions.js'
    export default {
        name:'selectEntry',
        props:{
        'selectFromDb':{
            default:true
        }
    },
    data() {
            return {
                show:false,
                isBusy:false,
                isBusyFind:false,
                isBusyLoad:false,
                treeDataSource: {},
                result:{
                    query:undefined,
                    start:undefined,
                    end:undefined,
                    total:undefined
                },
                treeDataSource: dataJson,
                formData:{eName:'',accurate:0},
                /*表格子數據放這裡*/
                fields: [
                    {
                        key:'eId',
                        label:'ID',
                        sortable:true
                    },
                    {
                        key: 'eName',
                        label:'Method of Entry',
                        sortable: true
                    },
                    {
                        key: 'eNameChn',
                        label:'入仕法',
                        sortable: true
                    }
                ],
                items:[],
                //选中的人物出现在这里
                selectedEntry : []
            }
        },
        components: {
            treeTable
        },
        methods: {
            close:function(){
                this.selectedEntry.splice(0,this.selectedEntry.length)
                this.show = false;
            },
            onRowSelected(items) {
                this.selectedEntry = items
            },
            onClearTable(){
                celarResultTable(this)
            },
            haveSelected: function(){
                //同步选中入仕途径
                this.$emit('getEntryName', {fields:this.fields,items:this.selectedEntry});
                this.selectedEntry.splice(0,this.selectedEntry.length)
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
            //按id查询入仕途径
            actionFunc(m){
                getListById('entry_list',m.Id,this)
            },
            handleTableScroll(){
                appendListById('entry_list',this)
            },
            find(){
                getListByName('entry_list_by_name',[this.formData.eName,this.formData.accurate],this)
            }
      },
        watch:{
        //DOM elements first time rendered
            show:function(){
                let st =  this.$refs.selectableTable
                if(this.show===true){
                st.$el.addEventListener('scroll',this.handleTableScroll, false)
                }
                //DOM 实例已经销毁了
                //else st.$el.removeListener('scroll',this.handleTableScroll)
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