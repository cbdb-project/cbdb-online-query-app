<template>
  <div class="hello">
    <b-card header-tag="header" footer-tag="footer">
        <template v-slot:header>
            <h6 class="mb-0">RESULTS</h6>
        </template>
        <div>
          <b-table 
            :items= "items" 
            :fields= "fields" 
            sticky-header 
            head-variant="light" 
            ref="selectableTable"
            selectable
            :select-mode="selectMode"
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
        </div>

      <!--
      <template v-slot:footer>
        <em>Footer Slot</em>
      </template>
      -->
    </b-card>   
  </div>
</template>

<script>
export default {
  name: 'queryResult',
  data () {
    return {
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
        ]
    }
  },
  computed:{
    user(){
      return this.$store.state.user
    },
    queryFormular(){
      return `office-ch-name:'同安縣主簿',person-ch-place:'泉州府',index-year:'${this.formData.indexYear}';`
    }
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
.hello{
  margin:24px 0;
  text-align: left;
}
.card-item-title{
  font-weight: bold;
}
</style>
