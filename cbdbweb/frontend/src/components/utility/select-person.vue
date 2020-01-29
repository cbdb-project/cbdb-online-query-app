<template>
    <div>
        <b-button pill variant="outline-primary"  v-b-modal.select-person
        class = "query-condition-button" size="sm">{{$t('selectPerson.selectButton')}}</b-button>
        <b-modal 
          id="select-person" 
          title="Select People from Database" 
          size = "xl"
          v-model="show"
        >
            <b-row>
                <b-col :cols = 4 style = "text-align:right">
                  <b-card>
                    <b-form-group label-cols="4" :label="$t('selectPerson.personName')" label-for="select-person-input-name">
                        <b-form-input id="select-person-input-name" :placeholder="$t('globalTerm.cnOrPy')"></b-form-input>
                    </b-form-group>
                    <b-form-group>
                      <b-button variant="primary">Search</b-button>
                    </b-form-group>
                  </b-card>
                </b-col>
                <b-col :cols = 8>
                    <b-table 
                        :items= "items" 
                        :fields= "fields" 
                        sticky-header = "1000px"
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
  name:'selectPerson',
  props:['selectMode'],
  data () {
    return {
      show:false,
      /*表格子數據放這裡*/
        fields: [
          {
            key: 'personId',
            label:'ID',
            sortable: true
          },
          {
            key: 'personName',
            label:'Name',
            sortable: true
          },
          {
            key: 'personNameCh',
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
            key: 'selected',
            sortable: false,
          }
        ],
        items: [
          {personId:"1644",personName:"Zhu Youbao",personNameCh:"朱祐保",indexYear:"",female:"No"},
          {personId:"1645",personName:"Zhu Youbin",personNameCh:"朱祐檳",indexYear:"1538",female:"No"},
          {personId:"1646",personName:"Zhu Youceng",personNameCh:"朱右曾",indexYear:"1858",female:"No"},
          {personId:"1647",personName:"Zhu Youchen&#38;1",personNameCh:"朱幼成",indexYear:"1283",female:"No"},
          {personId:"1648",personName:"Zhu Youdao",personNameCh:"朱由道",indexYear:"1225",female:"No"},
          {personId:"1649",personName:"Zhu Youde",personNameCh:"朱有德",indexYear:"",female:"No"},
          {personId:"1650",personName:"Zhu Youdun",personNameCh:"朱有燉",indexYear:"",female:"No"},
          {personId:"1651",personName:"Zhu Youfu",personNameCh:"朱友輔",indexYear:"",female:"No"},
          {personId:"1652",personName:"Zhu Duokui",personNameCh:"朱多煃",indexYear:"",female:"No"},
          {personId:"1653",personName:"Zhu Duokun",personNameCh:"Zhu Duokun",indexYear:"",female:"No"},
          {personId:"1654",personName:"Zhu Duoliang",personNameCh:"朱多",indexYear:"1607",female:"No"},
          {personId:"1655",personName:"Zhu Duopu",personNameCh:"Zhu Duopu",indexYear:"1418",female:"No"},
          {personId:"1656",personName:"Zhu Duoyun",personNameCh:"朱多熅",indexYear:"",female:"No"},
          {personId:"1657",personName:"Zhu Duozheng",personNameCh:"朱多炡",indexYear:"1589",female:"No"},
          {personId:"30164",personName:"Zhu YouXiao",personNameCh:"朱由校",indexYear:"1627",female:"No"},
        ],
        //选中的人物出现在这里
        selectedPerson : []
    }
  },
  methods: {
      onRowSelected(items) {
        this.selectedPerson = items
      },
      haveSelected: function(){
        //同步选中人物
        console.log("成功");
        this.$emit('getPersonName', this.selectedPerson);
        this.show = false;
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
  width:224px;
  margin-left:6px;
  margin-right:6px;
  /* 和表單中的輸入框對齊 */
}
</style>