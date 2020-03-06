<template>
    <div>
        <b-button  variant="outline-primary"  v-b-modal="'import-place-table'+name"
          class = "query-condition-button" size="sm">{{$t('globalTerm.import')}}
        </b-button>
      <b-modal
          scrollable
          :id="'import-place-table'+name" 
          title="Import Local Files" 
          size = "xl"
          v-model="show"
      >
            <b-row>
                <b-col :cols = 4 style = "text-align:right">
                    <b-card>
                       <input type="file" value="" ref="file" id="file" @change="fileSelect"> 
                    </b-card>    
                    <b-button variant="primary" @click="handleFileUpload"
                      :disabled="isBusy" style = "width:96px">
                        <span v-if="!isBusy">Go</span>
                        <b-spinner small v-if="isBusy"></b-spinner>
                    </b-button>       
                </b-col>
                <b-col :cols = 8>
                    <b-table 
                        :items= "items" 
                        :fields= "fields" 
                        sticky-header ="600px"
                        head-variant="light" 
                        ref="selectableTable"
                        selectable
                        select-mode="multi"
                        @row-selected="onRowSelected"
                        responsive="xl">
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
export default {
  name:'selectPlace',
  props:{
    'name':{
        default:''
    }
  },
  data () {
    return {
      file:undefined,
      isBusy:false,
      show:false,
      /*表格子數據放這裡*/
        fields: [
          {
            key: 'placeName',
            label:'Place Name',
            sortable: true
          },
          {
            key: 'placeNameCh',
            label:'地名',
            sortable: true
          },
          {
            key: 'firstYear',
            label: 'First Year',
            sortable: true,
          },
          {
            key: 'lastYear',
            label: 'Last Year',
            sortable: true,
          },
          {
            key: 'BelongsTo',
            label:'Belongs To',
            sortable: true,
          },
          {
            key: 'BelongsToCh',
            label:'属于',
            sortable: true
          }
        ],
        items: [

        ],
        //选中的人物出现在这里
        selectedPlace : [
        ]
    }
  },
  methods: {
      fileSelect(){
        let file = this.$refs.file.files[0];
        this.file = file;
      },
      handleFileUpload(){
        //console.log('begin upload')
        this.isBusy = true
        console.log(this.file)
        this.axios({
          url:'http://'+ this.$store.state.global.serverAddress + "/api/tools/handle_upload_file",
          method: "POST",　　　　//  这个地方注意
          data: {'user':this.$store.state.local.user.uid},
          file:this.file,
          processData:false,
          contentType:false,
          success:(response) => {
            console.log("upload_success_response:", response)
          }
        }).then(
          (r)=>{
            this.isBusy = false
          },
          (e)=>{
          alert('something went wrong...')
          this.isBusy = false
          }
        )
      },
      onRowSelected(items) {
        this.selectedPlace = items
      },
      haveSelected: function(type){
        //同步选中地点
        //console.log("成功");
        this.$emit('getPlaceName', this.selectedPlace);
       this.show = false
      },
      selectAllRows() {
        this.$refs.selectableTable.selectAllRows()
      },
      clearSelected() {
        this.$refs.selectableTable.clearSelected()
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