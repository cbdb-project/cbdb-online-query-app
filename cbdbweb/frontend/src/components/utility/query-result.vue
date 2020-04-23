<template>
      <div ref="wrapper">
          <b-row class = "pb-3">
            <b-col>
            <b-button @click="exportData" variant="light">
              <a id="export"></a>Export<span v-if="this.selected.length>0">&nbsp;Selected</span>
            </b-button>
            </b-col>
            <b-col>
              <b-button-group style = "position:absolute;right:1em"> 
                <b-button v-if="this.selected.length>0" @click="clearSelected" variant="outline-secondary" size='sm' ><span>Cancel Selected</span></b-button>
                <b-button v-if="!(this.items.length===this.selected.length)" @click="selectAllRows" variant="outline-secondary" size='sm' ><span>Select All</span></b-button>
              </b-button-group>   
            </b-col>
          </b-row>
          <b-table 
            :items= "items" 
            :fields= "fields" 
            sticky-header 
            head-variant="light"
            :id="'res-'+this.name"             
            :ref="'selectableTable-'+this.name"
            selectable
            responsive
            select-mode="multi"
            :current-page="currentPage"
            :per-page="offset"
            @row-clicked="onRowSelected">
            <template v-slot:head()="scope">
              <div class="text-nowrap">
                Heading {{ scope.label }}
              </div>
            </template>
            <template v-slot:cell(NameChn)="data">
              <span>{{data.value}}</span>
              <span v-if="getSelected.indexOf(data.value)!==-1">{{data.selectRow()}}</span>
            </template>
          </b-table>
          <b-row>
            <b-col style="text-align:center">
              <b-pagination
                v-model="currentPage"
                :total-rows="end"
                :per-page="offset"
                align="fill"
                size="sm"
               ></b-pagination>
            </b-col>
          </b-row>
      </div>
      <!--
      <template v-slot:footer>
        <em>Footer Slot</em>
      </template>
      -->
</template>

<script>
import resultData from '@/assets/geodata.json'
export default {
  name: 'queryResult',
  props:{
    'name':{
        default:''
    },
    'start':{
        default:0
    },
    'offset':{
        default:50
    },
    'end':{
        default:500
    }
  },
  data () {
    return {
      currentPage:1,
      startIdx:this.start,
      isLoading:false,
      /*表格子數據放這裡*/
        fields: [
          {
            key: '\ufeffName',
            label:'Name',
            sortable: true
          },
          {
            key: 'NameChn',
            label:'姓名',
            stickyColumn: true, isRowHeader: true, 
            variant: 'light',
            sortable: true
          },
          {
            key: 'IndexYear',
            label: 'Index Year 指數年',
            sortable: true,
          },
          {
            key: 'Sex',
            label:'Gender 性別',
            sortable: true
          },
          {
            key: 'AddrID',
            label: 'Address ID',
            sortable: true,
          },
          {
            key: 'AddrName',
            label:'Address Name',
            sortable: true
          },
          {
            key: 'AddrChn',
            label: '地名(人)',
            sortable: true,
          },
          {
            key: 'X',
            label:'Longitude 經度',
            sortable: true
          },
          {
            key: 'Y',
            label:'Latitude 緯度',
            sortable: true
          },
          {
            key: 'AddrChn',
            label: '地名(人)',
            sortable: true,
          }
        ],
        items: resultData,
        selected:[]
    }
  },
  methods: {
    onRowSelected(item,index,event) {
      let self = this
      let i = self.getSelected.indexOf(item['NameChn'])
      if(i===-1){
        self.selected.push(item)
      }
      else{
        self.selected.splice(i,1);
      }
      console.log(self.selected)
    },
    selectAllRows() {
      this.$refs['selectableTable-'+this.name].selectAllRows()
      this.selected=this.items.map(i=>i)
    },
    clearSelected() {
      this.$refs['selectableTable-'+this.name].clearSelected()
      this.selected.splice(0,this.selected.length);
    },
    exportData(){
      let str = ''
      for(let i = 0; i<this.fields.length; i++)
        str += (this.fields[i].key+'    ')
      str += '\n'
      for(let i = 0; i<this.items.length; i++){
        for(let k in this.items[i]){
          str += (this.items[i][k] + '    ')
        }
        str += '\n'
      }
      var blob = new Blob([str]);
      var link = document.getElementById('export')
      link.download = "export_utf8"
      link.href = URL.createObjectURL(blob);
      link.click()
    },
  async loadMore(){
    let st = this.$refs['selectableTable-'+this.name]
    if(st.$el.scrollHeight - st.$el.scrollTop <= st.$el.clientHeight)
      if(this.end-this.startIdx>0&&this.isLoading===false){
        this.isLoading =true
        var vm = this
        var cb = ()=>{
        //console.log('rrr')
        let offset = vm.end-vm.startIdx>vm.offset?vm.offset:vm.end-vm.startIdx
        for(let i=0; i<offset; i++)vm.items.push( {"\ufeffName": "You Jianyan", "NameChn": "游簡言", "Sex": "M", "IndexYear": " 969", "AddrID": " 16027", "AddrName": "Jian'an", "AddrChn": "建安", "X": " 118.323784", "Y": " 27.038864", "xy_count": " 2"})
        vm.startIdx+=offset
        this.isLoading = false
        }
        await setTimeout(cb,1000)
      }
      else if(this.startIdx>=this.end) this.$refs['selectableTable-'+this.name].$el.removeEventListener('scroll',this.loadMore) 
    }
  },
  computed:{
    getSelected(){
      return this.selected.map(i=>i['NameChn'])
    }
  },
  mounted(){
    //this.$refs['selectableTable-'+this.name].$el.addEventListener('scroll',this.loadMore, false)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.user-input-label{
 text-align:left;
 width:100%
}
.query-condition-button{
  width:224px;
  margin:6px 0;
}
.card-item-body{
  text-align:center;
  margin: 6px 0;
}
.bread-crumb{
  width:30%;
  background-color: transparent
}
.card-item-title{
  font-weight: bold;
}
</style>
