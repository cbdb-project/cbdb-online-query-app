<template>
    <div>
        <b-button pill variant="outline-primary"  v-b-modal.select-entry-table
        class = "query-condition-button" size="sm">{{$t('selectEntry.selectButton')}}</b-button>
        <b-modal 
            id="select-entry-table" 
            title="Select Entry from Database" 
            size = "xl"
            v-model = "show"
        >
            <b-row>
                <b-col :cols = 4 style = "text-align:right">
                    <b-card>
                        <b-form-group label-cols="4" label="Entry English Name" label-for="select-entry-input-en-name">
                            <b-form-input id="select-entry-input-en-name"></b-form-input>
                        </b-form-group>
                        <b-form-group label-cols="4" label="入仕途径-中文" label-for="select-entry-input-ch-name">
                            <b-form-input id="select-entry-input-ch-name"></b-form-input>
                        </b-form-group>
                        <b-form-group>
                            <b-button variant="primary">Search</b-button>
                        </b-form-group>
                    </b-card>
                    <b-card>
                        <div style="height:400px; overflow:auto">
                            <tree-table listName="入仕途径类目表" ref="recTree" :list.sync="treeDataSource" @actionFunc="actionFunc" @deleteFunc="deleteFunc" @handlerExpand="handlerExpand" @orderByFunc="orderByFunc"></tree-table>
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
    import dataJson from '../views/entryData.json'
    import treeTable from '../treeTable/tree-table.vue'
    export default {
        name:'selectEntry',
        data() {
            return {
                show:false,
                treeDataSource: dataJson,
                /*表格子數據放這裡*/
                fields: [
                    {
                        key: 'entryName',
                        label:'Method of Entry',
                        sortable: true
                    },
                    {
                        key: 'entryNameCh',
                        label:'入仕法',
                        sortable: true
                    },
                    {
                        key: 'selected',
                        sortable: false,
                    }
                ],
                items: [
                    {entryName:"[Missing Data]",entryNameCh:"[Missing Data]"},
                    {entryName:"not available/applicable",entryNameCh:"未知"},
                    {entryName:"abdication of previous emperor",entryNameCh:"前帝遜位"},
                    {entryName:"To be Deleted: betrothal",entryNameCh:"臨時保留，待考。"},
                    {entryName:"promotion from clerical positions",entryNameCh:"胥吏出職"},
                    {entryName:"purchase",entryNameCh:"進納補官"},
                    {entryName:"yin privilege: Grand Sacrifice",entryNameCh:"恩蔭: 大禮蔭補"},
                    {entryName:"deposed previous emperor",entryNameCh:"廢前帝自立"},
                    {entryName:"direct appointment to painting academy",entryNameCh:"畫院待詔"},
                    {entryName:"imperial summons",entryNameCh:"徵辟"},
                    {entryName:"direct recruitment into military service",entryNameCh:"募入軍伍"}
                ],
                //选中的人物出现在这里
                selectedEntry : []
            }
        },
        components: {
            treeTable
        },
        methods: {
            onRowSelected(items) {
                this.selectedEntry = items
                //要把选中的结果传递给调用的父组件
                console.log(this.selectedEntry)
            },
            haveSelected: function(){
                //同步选中入仕途径
                console.log("成功");
                this.$emit('getEntryName', this.selectedEntry);
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
    width:224px;
    margin:6px 0;
    }
</style>