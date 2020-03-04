<template>
    <div>
        <b-button   variant="outline-primary"  v-b-modal.select-place-table
          class = "query-condition-button" size="sm">{{$t('globalTerm.selectFromDb')}}
        </b-button>
        <b-modal
          scrollable
          id="select-place-table" 
          title="Select Place from Database" 
          size = "xl"
          v-model="show"
        >
            <b-row>
                <b-col :cols = 4 style = "text-align:right">
                    <b-form-group>
                      <b-button variant="outline-danger">Clear Table</b-button>      
                    </b-form-group>
                    <b-card>
                        <b-form-group label-cols="4" label="Place Name" label-for="select-place-input-en-name">
                            <b-form-input id="select-place-input-en-name"></b-form-input>
                        </b-form-group>
                        <b-form-group label-cols="4" label="From" label-for="select-place-input-ch-name">
                            <b-form-input id="select-place-input-ch-name"></b-form-input>
                        </b-form-group>
                        <b-form-group label-cols="4" label="To" label-for="select-place-input-ch-name">
                            <b-form-input id="select-place-input-ch-name"></b-form-input>
                        </b-form-group>
                          <b-button-group>
                            <b-button variant="primary">Find</b-button>   
                          </b-button-group> 
                    </b-card>   
                    <b-card>
                        <b-form-group>
                            <b-button variant="primary">Select Places Belonging To</b-button>
                        </b-form-group>
                    </b-card>     
                </b-col>
                <b-col :cols = 8>
                    <b-card style = "text-align:right">
                        <b-form inline >
                            <label for="select-place-input-name" style="min-width:60px">Name</label>
                            <b-form-input id="select-place-input-name"></b-form-input>
                            <b-button variant="outline-info">Search within table</b-button>
                        </b-form>
                    </b-card>
                    <b-table 
                        :items= "items" 
                        :fields= "fields" 
                        sticky-header = "1000px"
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
export default {
  name:'selectPlace',
  data () {
    return {
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
          {placeName:"",placeNameCh:"普洱道",firstYear:"1914",lastYear:"1928",BelongsTo:"",BelongsToCh:"雲南省諸道區"},
          {placeName:"",placeNameCh:"陝西道",firstYear:"1913",lastYear:"1913",BelongsTo:"",BelongsToCh:"陝西省諸道區"},
          {placeName:"",placeNameCh:"鬱江道",firstYear:"1913",lastYear:"1913",BelongsTo:"",BelongsToCh:"廣西省諸道區"},
          {placeName:"",placeNameCh:"黑龍江省諸道區",firstYear:"1911",lastYear:"1948",BelongsTo:"Heilongjiang Sheng",BelongsToCh:"黑龍江省"},
          {placeName:"",placeNameCh:"蒼梧道",firstYear:"1914",lastYear:"1926",BelongsTo:"",BelongsToCh:"廣西省諸道區"},
          {placeName:"",placeNameCh:"邕南道",firstYear:"1913",lastYear:"1913",BelongsTo:"",BelongsToCh:"廣西省諸道區"},
          {placeName:"",placeNameCh:"濟西道",firstYear:"1913",lastYear:"1913",BelongsTo:"",BelongsToCh:"山東省諸道區"},
          {placeName:"",placeNameCh:"南寧道",firstYear:"1914",lastYear:"1926",BelongsTo:"",BelongsToCh:"廣西省諸道區"},
          {placeName:"",placeNameCh:"岱南道",firstYear:"1913",lastYear:"1913",BelongsTo:"",BelongsToCh:"山東省諸道區"},
          {placeName:"",placeNameCh:"鎮南道",firstYear:"1913",lastYear:"1926",BelongsTo:"",BelongsToCh:"廣西省諸道區"},
          {placeName:"",placeNameCh:"田南道",firstYear:"1913",lastYear:"1926",BelongsTo:"",BelongsToCh:"廣西省諸道區"},
        ],
        //选中的人物出现在这里
        selectedPlace : []
    }
  },
  methods: {
      onRowSelected(items) {
        this.selectedPlace = items
      },
      haveSelected: function(){
        //同步选中地点
        console.log("选取成功");
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