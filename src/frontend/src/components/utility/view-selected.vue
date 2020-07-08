<template>
    <span>
        <b-button variant="outline-info" v-b-modal="'view-selected-'+this.name" 
            class="query-condition-button ml-3" size="sm">
            View selected
            <b-badge variant="info">{{items.length}}</b-badge>
        </b-button>
    <b-modal
        scrollable
        :id="'view-selected-'+this.name"
        title = "View Selected"
        size = "xl"
        v-model="show"
    >
        <b-row>
            <b-col >
                <b-form-group style = "text-align:right">
                      <b-button variant="outline-danger" @click="dropAllItems" size='sm' class = "mx-3" style="position:absolute;left:0">Drop All</b-button>
                      <b-button variant="outline-danger" @click="dropSelectedItems" size='sm' class = "mx-3" style="position:absolute;left:120px">Drop Selected</b-button>  
                      <b-button-group> 
                        <b-button v-if="selected.length>0" @click="clearSelected" variant="outline-secondary" size='sm' ><span>Cancel Selection</span></b-button>
                        <b-button v-if="!(items.length===selected.length)" @click="selectAllRows" variant="outline-secondary" size='sm' ><span>Select All</span></b-button>
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
            </b-col>            
        </b-row>
            <template v-slot:modal-footer>
              <b-button v-if="false">
                Cancel
              </b-button>
              <b-button v-if="false">
                Select
              </b-button>
            </template>
    </b-modal>
    </span>
</template>

<script>
export default {
  name:'viewSelected',
  props:{
    'name':{
        default:''
    },
    'fields':{
        default:[]
    },
    'items':{
        default:[]
    }
  },
  data () {
    return {
        show:false,
        selected : []
    }
  },
  methods: {
      dropSelectedItems(){
        this.items = this.items.filter(i => this.selected.indexOf(i)===-1)
        this.selected.splice(0,this.selected.length);
      },
      dropAllItems(){
        this.items.splice(0,this.items.length);
      },
      onRowSelected(items) {
        this.selected = items
        console.log(this.name)
      },
      haveSelected: function(){ 
          console.log(this.name)
      },
      selectAllRows() {
        this.$refs.selectableTable.selectAllRows()
      },
      clearSelected() {
        this.$refs.selectableTable.clearSelected()
      }
  },
  watch:{
      items(newVal){
          this.$emit('update:items',newVal)
          console.log(newVal)
      }
  }
}
</script>