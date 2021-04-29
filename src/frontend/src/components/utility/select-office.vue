<template>
  <div>
    <b-button-group>
      <b-button
        v-if="selectFromDb"
        variant="outline-primary"
        v-b-modal.select-office-table
        class="query-condition-button"
        size="sm"
        >{{ $t("globalTerm.selectFromDb") }}
      </b-button>
      <b-button
        v-if="importList"
        variant="outline-primary"
        class="query-condition-button"
        size="sm"
        >{{ $t("globalTerm.import") }}
      </b-button>
    </b-button-group>
    <b-modal
      scrollable
      id="select-office-table"
      title="Select Office from Database"
      size="xl"
      v-model="show"
    >
      <b-row>
        <b-col :cols="4" style="text-align:right">
          <b-card>
            <b-form-group
              label-cols="4"
              :label="$t('selectOffice.officeName')"
              label-for="select-office-input-ch-name"
            >
              <b-form-input
                id="select-office-input-ch-name"
                v-model="formData.pName"
              ></b-form-input>
            </b-form-group>
            <b-form-group>
              <b-button
                variant="primary"
                :disabled="isBusy || formData.pName === ''"
                @click="find"
              >
                <b-spinner small v-if="isBusyFind"> </b-spinner>
                <span v-else>Find</span>
              </b-button>
            </b-form-group>
          </b-card>
          <b-card>
            <div style="height:310px; overflow:scroll">
              <tree-table
                listName="官职类目表"
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
                v-if="this.selectedOffice.length > 0"
                @click="clearSelected"
                variant="outline-secondary"
                size="sm"
                ><span>Cancel Selected</span></b-button
              >
              <b-button
                v-if="!(this.items.length === this.selectedOffice.length)"
                @click="selectAllRows"
                variant="outline-secondary"
                size="sm"
                ><span>Select All</span></b-button
              >
            </b-button-group>
          </b-form-group>
          <b-row
            v-if="
              this.result.total !== undefined && this.result.end !== undefined
            "
          >
            <b-col>
              <b-link disabled>{{ result.end }}</b-link
              ><span style="color:#4D4D4D">&nbsp;of&nbsp;</span>
              <b-link disabled>{{ result.total }}</b-link
              ><span style="color:#4D4D4D">&nbsp;records are shown.</span>
            </b-col>
          </b-row>
          <b-table
            :items="items"
            :fields="fields"
            sticky-header="470px"
            head-variant="light"
            id="st"
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
          <b-row style="text-align:center"
            ><b-col><b-spinner small v-if="isBusyLoad"></b-spinner></b-col
          ></b-row>
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
import dataJson from "@/assets/officeData.json";
import treeTable from "../treeTable/tree-table.vue";
import {
  getListById,
  appendListById,
  clearResultTable,
  getListByName
} from "@/components/utility/utility-functions.js";
export default {
  name: "selectOffice",
  props: {
    selectFromDb: {
      default: true
    },
    importList: {
      default: false
    }
  },
  data() {
    return {
      show: false,
      isBusy: false,
      isBusyFind: false,
      isBusyLoad: false,
      formData: {
        pName: "",
        accurate: 0
      },
      treeDataSource: {},
      result: {
        id: undefined,
        start: undefined,
        end: undefined,
        total: undefined
      },
      /*表格子數據放這裡*/
      fields: [
        {
          key: "pId",
          label: "Office ID",
          sortable: true
        },
        {
          key: "pName",
          label: "Office Name",
          sortable: true
        },
        {
          key: "pNameChn",
          label: "官職名稱",
          sortable: true
        }
      ],
      items: [],
      //选中的人物出现在这里
      selectedOffice: []
    };
  },
  components: {
    treeTable
  },
  methods: {
    close: function() {
      this.selectedOffice.splice(0, this.selectedOffice.length);
      this.show = false;
    },
    //加載職官樹
    loadOfficeTree() {
      if (localStorage.officeTree != undefined)
        this.treeDataSource = JSON.parse(localStorage.officeTree);
      else {
        this.treeDataSource = dataJson;
        localStorage.officeTree = JSON.stringify(dataJson);
      }
    },
    onRowSelected(items) {
      //用户选中列表中的条目后，同步到selectedOffice中
      this.selectedOffice = items;
    },
    onClearTable() {
      clearResultTable(this);
    },
    haveSelected: function() {
      //同步选中官职给父组件（页面）
      this.$emit("getOfficeName", {
        fields: this.fields,
        items: this.selectedOffice
      });
      this.selectedOffice.splice(0, this.selectedOffice.length);
      this.show = false;
    },
    selectAllRows() {
      this.$refs.selectableTable.selectAllRows();
    },
    clearSelected() {
      this.$refs.selectableTable.clearSelected();
    },
    handlerExpand(m) {
      //console.log(m.Id+'展开/收缩')
      m.isExpand = !m.isExpand;
    },
    //按id查询职官
    actionFunc(m) {
      getListById("post_list", m.Id, this);
    },
    handleTableScroll() {
      appendListById("post_list", this);
    },
    find() {
      getListByName(
        "office_list_by_name",
        [this.formData.pName, this.formData.accurate],
        this
      );
    }
  },
  watch: {
    //DOM elements first time rendered
    show: function() {
      let st = this.$refs.selectableTable;
      if (this.show === true) {
        st.$el.addEventListener("scroll", this.handleTableScroll, false);
      }
      //DOM 实例已经销毁了
      //else st.$el.removeListener('scroll',this.handleTableScroll)
    }
  },
  created() {
    this.loadOfficeTree();
  }
};
</script>

<style scoped>
.query-condition-button {
  width: 128px;
  margin: 6px 0;
}
</style>
