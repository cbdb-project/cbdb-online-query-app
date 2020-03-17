<template>
        <div ref="wrapper">
          <b-row class = "pb-3 px-3" style = "text-align:right">
            <b-col>
            <b-button @click="exportData" variant="light">
              <a id="export"></a>Export
            </b-button>
            </b-col>
          </b-row>
          <b-table 
            :items= "items" 
            :fields= "fields" 
            sticky-header 
            head-variant="light"
            id="res"             
            ref="selectableTable"
            selectable
            select-mode="multi"
            @row-selected="onRowSelected"
            responsive>
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
        </div>

      <!--
      <template v-slot:footer>
        <em>Footer Slot</em>
      </template>
      -->
</template>

<script>
export default {
  name: 'queryResult',
  props:{
    'start':{
        default:0
    },
    'offset':{
        default:20
    },
    'end':{
        default:100
    }
  },
  data () {
    return {
      isLoading:false,
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
        ]
    }
  },
  methods: {
    onRowSelected(items) {
      this.selected = items
    },
    selectAllRows() {
      this.$refs.selectableTable.selectAllRows()
    },
    clearSelected() {
      this.$refs.selectableTable.clearSelected()
    },
    exportData(){
      let str = ''
      for(let i = 0; i<this.fields.length; i++)
        str += (this.fields[i].key+' ')
      str += '\n'
      for(let i = 0; i<this.items.length; i++){
        for(let k in this.items[i]){
          str += (this.items[i][k] + ' ')
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
    if(this.end-this.start>0){
      this.isLoading =true
      var vm = this
      var cb = ()=>{
      console.log('rrr')
      let offset = vm.end-vm.start>vm.offset?vm.offset:vm.end-vm.start
      for(let i=0; i<offset; i++)vm.items.push( {name:'Liu Jun',nameCh:'劉俊',indexYear:'1086',female:false,placeType:'籍貫',personPlace:'Nan Yang',personPlaceCh:'南陽'})
      vm.start+=offset
      this.isLoading = false
      }
      await setTimeout(cb,1000)
    }
  }
  },
  mounted(){
    let st =  this.$refs.selectableTable
    // 监听这个dom的scroll事件
    st.$el.addEventListener('scroll', () => {
    if(st.$el.scrollHeight - st.$el.scrollTop <= st.$el.clientHeight)
    this.loadMore()
    //console.log('rrrrrrrr')
    }, false)
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
