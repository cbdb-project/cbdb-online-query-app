<template>
  <div>
    <b-button
      v-if="selectFromDb"
      variant="outline-primary"
      v-b-modal.select-relationship-table
      class="query-condition-button"
      size="sm"
      >{{ $t("globalTerm.selectFromDb") }}</b-button
    >
    <b-modal
      id="select-relationship-table"
      title="Select Associations"
      size="xl"
      v-model="show"
    >
      <b-row>
        <b-col :cols="4" style="text-align:right">
          <b-card>
            <div style="height:400px; overflow:auto">
              <tree-table
                listName="社會關係類目表"
                ref="recTree"
                :list.sync="treeDataSource"
                @handlerExpand="handlerExpand"
                @actionFunc="actionFunc"
              ></tree-table>
            </div>
          </b-card>
        </b-col>
        <b-col :cols="8">
          <b-form-group style="text-align:right">
            <b-button
              variant="outline-danger"
              @click="onClearTable"
              size="sm"
              class="mx-3"
              style="position:absolute;left:0"
              >Clear Table</b-button
            >
            <b-button-group>
              <b-button
                v-if="this.selectedRelation.length > 0"
                @click="clearSelected"
                variant="outline-secondary"
                size="sm"
                ><span>Cancel Selected</span></b-button
              >
              <b-button
                v-if="!(this.items.length === this.selectedRelation.length)"
                @click="selectAllRows"
                variant="outline-secondary"
                size="sm"
                ><span>Select All</span></b-button
              >
            </b-button-group>
          </b-form-group>
          <b-table
            :items="items"
            :fields="fields"
            sticky-header="600px"
            head-variant="light"
            ref="selectableTable"
            selectable
            select-mode="multi"
            @row-selected="onRowSelected"
            responsive="sm"
          >
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
import dataJson from "@/assets/relationDataNetwork.json";
import treeTable from "../treeTable/tree-table.vue";
import {
  getListById,
  appendListById,
  clearResultTable,
  getListByName,
  returnRelation,
  relationGetter
} from "@/components/utility/utility-functions.js";
export default {
  name: "selectRelationship",
  props: {
    selectFromDb: {
      default: true
    }
  },
  data() {
    return {
      show: false,
      isBusy: false,
      isBusyFind: false,
      isBusyLoad: false,
      treeDataSource: dataJson,
      /*表格子數據放這裡*/
      fields: [
        {
          key: "aId",
          label: "社會關係代碼",
          sortable: true
        },
        {
          key: "aNameChn",
          label: "社會關係名",
          sortable: true
        }
      ],
      //rId 相當於 C_ASSOC_CODE
      items: [],
      //选中的关系出现在这里
      selectedRelation: []
    };
  },
  components: {
    treeTable
  },
  methods: {
    close: function() {
      this.selectedRelation.splice(0, this.selectedRelation.length);
      this.show = false;
    },
    onRowSelected(items) {
      this.selectedRelation = items;
    },
    onClearTable() {
      clearResultTable(this);
    },
    selectAllRows() {
      this.$refs.selectableTable.selectAllRows();
    },
    clearSelected() {
      this.$refs.selectableTable.clearSelected();
    },
    handlerExpand(m) {
      console.log("展开/收缩");
      m.isExpand = !m.isExpand;
    },
    actionFunc(m) {
      returnRelation(m.Id, this);
    },
    handleTableScroll() {
      appendListById("get_assoc", this);
    },
    haveSelected: function() {
      //同步选中入仕途径
      console.log("选取成功");
      this.$emit("getRelation", {
        fields: this.fields,
        items: this.selectedRelation
      });
      this.close();
    },
    find() {
      getListByName("find_assoc", [this.formData.aName], this);
    }
  }
};
</script>

<style scoped>
.query-condition-button {
  width: 128px;
  margin: 6px 0;
}
</style>
