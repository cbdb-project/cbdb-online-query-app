<template>
    <div>
        <b-button   variant="outline-primary"  v-b-modal="'select-place-table'+name"
          class = "query-condition-button" size="sm">{{$t('globalTerm.selectFromDb')}}
        </b-button>
        <b-modal
          scrollable
          :id="'select-place-table'+name" 
          title="Select Place from Database" 
          size = "xl"
          v-model="show"
        >
            <b-row>
                <b-col :cols = 4 style = "text-align:right">
                    <b-card>
                        <b-form-group label-cols="4" label="Place Name" label-for="select-place-input-name">
                            <b-form-input id="select-place-input-name" v-model="formData.pName"></b-form-input>
                        </b-form-group>
                        <b-form-group label-cols="4" label="From" label-for="select-place-sy">
                            <b-form-input id="select-place-sy" v-model="formData.fromYear"></b-form-input>
                        </b-form-group>
                        <b-form-group label-cols="4" label="To" label-for="select-place-ty">
                            <b-form-input id="select-place-input-ty" v-model="formData.toYear"></b-form-input>
                        </b-form-group>
                          <b-button-group>
                            <b-button variant="primary" :disabled="isBusy">
                                <span v-if="!isBusyFind" @click="find">Find</span>
                                <b-spinner small v-else></b-spinner>
                            </b-button>   
                          </b-button-group> 
                    </b-card>   
                    <b-card>
                        <b-form-group>
                            <b-button variant="primary" :disabled="isBusy||selectedPlace.length!==1"
                            >
                                <span v-if="!isBusySupLoc" @click="getSuperiorLoc">Get Places Belong to</span>
                                <b-spinner small v-else></b-spinner>
                            </b-button>
                        </b-form-group>
                    </b-card>     
                </b-col>
                <b-col :cols = 8>
                    <b-form-group style = "text-align:right">
                      <b-button variant="outline-danger" @click="onClearTable" size='sm' class = "mx-3" style="position:absolute;left:0">Clear Table</b-button> 
                      <b-button-group> 
                        <b-button v-if="this.selectedPlace.length>0" @click="clearSelected" variant="outline-secondary" size='sm' ><span>Cancel Selected</span></b-button>
                        <b-button v-if="!(this.items.length===this.selectedPlace.length)" @click="selectAllRows" variant="outline-secondary" size='sm' ><span>Select All</span></b-button>
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
                            <b-spinner small v-if="this.isBusyLoad===true"></b-spinner>
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
import {capitalizeFirst,celarResultTable} from '@/components/utility/utility-functions.js'
export default {
  name:'selectPlace',
  props:{
    'name':{
        default:''
    }
  },
  data () {
    return {
        first:true,
        show:false,
        isBusy:false,
        isBusySupLoc:false,
        isBusyFind:false,
        isBusyLoad:false,
        formData:{
          pName:'',
          isApprox:1,
          fromYear:'',
          toYear:''
        },
        result:{
          id:undefined,
          start:undefined,
          end:undefined,
          total:undefined
        },
      /*表格子數據放這裡*/
        fields: [
          {
            key: 'pId',
            label:'ID',
            sortable: true
          },
          {
            key: 'pName',
            label:'Place Name',
            sortable: true
          },
          {
            key: 'pNameChn',
            label:'地名',
            sortable: true
          },
          {
            key: 'pStartTime',
            label: 'First Year',
            sortable: true,
          },
          {
            key: 'pEndTime',
            label: 'Last Year',
            sortable: true,
          },
          {
            key: 'pBName',
            label:'Belongs To',
            sortable: true,
          },
          {
            key: 'pBNameChn',
            label:'属于',
            sortable: true
          }
        ],
        items: [

        ],
        //选中的人物出现在这里
        selectedPlace : []
    }
  },
  methods: {
      close:function(){
        this.selectedPlace.splice(0,this.selectedPlace.length)
        this.show = false
      },
      onRowSelected(items) {
        this.selectedPlace = items
      },
      onClearTable(){
        celarResultTable(this)
      },
      haveSelected: function(){
        //同步选中地点
        console.log("选取成功");
        this.$emit('getPlaceName', {fields:this.fields,items:this.selectedPlace});
        this.selectedPlace.splice(0,this.selectedPlace.length)
        this.show = false
      },
      selectAllRows() {
        this.$refs.selectableTable.selectAllRows()
      },
      clearSelected() {
        this.$refs.selectableTable.clearSelected()
      },
      find(){
        let vm = this
        if(vm.isBusy===false){
          vm.isBusy=true
          vm.isBusyFind=true
          vm.formData.pName = capitalizeFirst(vm.formData.pName)
          let fy = this.formData.fromYear
          let ty = this.formData.toYear
          //自動填充
          if(fy!==''||ty!==''){
            if (fy==='')fy = '-200'
            if(ty==='')ty = (new Date()).getFullYear()
          }
          let query = `${vm.$store.state.global.apiAddress}place_list?name=${this.formData.pName}&accurate=${this.formData.isApprox}&startTime=${fy}&endTime=${ty}`
          console.log(query)
          vm.axios.get(`${query}&start=1&list=100`)
          .then((r)=>{
            console.log(r.data)
            vm.items = r.data.data
            vm.result.query = query
            vm.result.start = parseInt(r.data.start)
            vm.result.end = parseInt(r.data.end)
            vm.result.total = parseInt(r.data.total)
            vm.$refs.selectableTable.$el.scrollTop=0//弹回最上方
            },
            (e)=>{
              alert('Sorry, something went wrong...')
              console.log(e)
            }
          ).then(()=>{
            vm.isBusy=false
            vm.isBusyFind=false
          })
        }
      },
      getSuperiorLoc(){
        let vm = this
        if(vm.isBusy===false){
          vm.isBusy=true
          vm.isBusySupLoc=true
          let id = this.selectedPlace[0]['pId']
          let query = `${vm.$store.state.global.apiAddress}place_belongs_to?id=${id}`
          vm.axios.get(`${query}&start=1&list=100`)
          .then((r)=>{
            console.log(r.data)
            vm.items = r.data.data
            vm.result.query = query
            vm.result.start = parseInt(r.data.start)
            vm.result.end = parseInt(r.data.end)
            vm.result.total = parseInt(r.data.total)
            vm.$refs.selectableTable.$el.scrollTop=0//弹回最上方
            },
            (e)=>{
              alert('Sorry, something went wrong...')
              console.log(e)
            }
          )
          .then(
            ()=>{
            vm.isBusy=false
            vm.isBusySupLoc=false
            }
          )
        }
      },
      handleTableScroll(){
        let vm = this
        let st =  vm.$refs.selectableTable
        if(st.$el.scrollHeight - st.$el.scrollTop <= st.$el.clientHeight&&vm.isBusy===false)
          if(vm.result.end!==undefined&&vm.result.total!==undefined&&vm.result.end<vm.result.total){
            vm.isBusy=true
            vm.isBusyLoad=true
            vm.axios.get(vm.result.query+`&start=${vm.result.end+1}&list=100`)
            .then((r)=>{
              //console.log(r.data.data)
              r.data.data.forEach(i=>{vm.items.push(i)})
              vm.result.start = parseInt(r.data.start)
              vm.result.end = parseInt(r.data.end)
              //vm.result.total = parseInt(r.data.total)
              },
              (e)=>{
                alert('Sorry, something went wrong...')
              }
            )
            .then(()=>{
              vm.isBusy=false
              vm.isBusyLoad=false
            })
          }        
      },
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