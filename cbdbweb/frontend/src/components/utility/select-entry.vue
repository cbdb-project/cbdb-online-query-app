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
                            <b-form-input id="select-entry-input-name"></b-form-input>
                        </b-form-group>
                        <b-form-group>
                            <b-button variant="primary">Find</b-button>
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
                      <b-button variant="outline-danger" @click="items=[]" size='sm' class = "mx-3" style="position:absolute;left:0">Clear Table</b-button> 
                      <b-button-group> 
                        <b-button v-if="this.selectedEntry.length>0" @click="clearSelected" variant="outline-secondary" size='sm' ><span>Cancel Selected</span></b-button>
                        <b-button v-if="!(this.items.length===this.selectedEntry.length)" @click="selectAllRows" variant="outline-secondary" size='sm' ><span>Select All</span></b-button>
                      </b-button-group>      
                    </b-form-group>
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
                        <b-spinner small v-if="this.isLoading===true"></b-spinner>
                    </b-col>
                </b-row>
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
        props:{
        'selectFromDb':{
            default:true
        }
    },
        data() {
            return {
                end:100,
                start:0,
                offset:10,
                show:false,
                first:true,
                isLoading:false,
                treeDataSource: dataJson,
                /*表格子數據放這裡*/
                fields: [
                    {
                        key:'eId',
                        label:'ID',
                        sortable:true
                    },
                    {
                        key: 'entryName',
                        label:'Method of Entry',
                        sortable: true
                    },
                    {
                        key: 'entryNameCh',
                        label:'入仕法',
                        sortable: true
                    }
                ],
                items: [
                    {eId:"4567",entryName:"[Missing Data]",entryNameCh:"[Missing Data]"},
                    {eId:"4568",entryName:"not available/applicable",entryNameCh:"未知"},
                    {eId:"4569",entryName:"abdication of previous emperor",entryNameCh:"前帝遜位"},
                    {eId:"4568",entryName:"To be Deleted: betrothal",entryNameCh:"臨時保留，待考。"},
                    {eId:"4569",entryName:"promotion from clerical positions",entryNameCh:"胥吏出職"},
                    {eId:"4570",entryName:"purchase",entryNameCh:"進納補官"},
                    {eId:"4571",entryName:"yin privilege: Grand Sacrifice",entryNameCh:"恩蔭: 大禮蔭補"},
                    {eId:"4572",ntryName:"deposed previous emperor",entryNameCh:"廢前帝自立"},
                    {eId:"4573",entryName:"direct appointment to painting academy",entryNameCh:"畫院待詔"},
                    {eId:"4574",entryName:"imperial summons",entryNameCh:"徵辟"},
                    {eId:"4575",entryName:"direct recruitment into military service",entryNameCh:"募入軍伍"},
                    {eId:"4576",entryName:"[Missing Data]",entryNameCh:"[Missing Data]"},
                    {eId:"4577",entryName:"[Missing Data]",entryNameCh:"[Missing Data]"},
                    {eId:"4578",entryName:"[Missing Data]",entryNameCh:"[Missing Data]"},
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
        async loadMore(){
            if(this.end-this.start>0&&this.isLoading===false){
            this.isLoading =true
            var vm = this
            var cb = ()=>{
            //console.log('rrr')
            let offset = vm.end-vm.start>vm.offset?vm.offset:vm.end-vm.start
            for(let i=0; i<offset; i++)
                vm.items.push({eId:"4578",entryName:"[Missing Data]",entryNameCh:"[Missing Data]"})
            vm.start+=offset
            this.isLoading = false
            }
            await setTimeout(cb,1000)
            }
        }
      },
        watch:{
        //DOM elements first time rendered
            show:function(){
                if(this.first===true){
                this.first=false
                let st =  this.$refs.selectableTable
                // 监听这个dom的scroll事件
                st.$el.addEventListener('scroll', () => {
                console.log(`${st.$el.scrollHeight} ${st.$el.scrollTop} ${st.$el.clientHeight}`)
                if(st.$el.scrollHeight - st.$el.scrollTop <= st.$el.clientHeight){
                    //console.log('eeeee')
                    this.loadMore()
                        }
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