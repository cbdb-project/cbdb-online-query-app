<template>
  <div>
    <b-button
      variant="outline-primary"
      v-b-modal="'import-place-table' + name"
      class="query-condition-button"
      size="sm"
      >{{ $t("globalTerm.import") }}
    </b-button>
    <b-modal
      scrollable
      :id="'import-place-table' + name"
      title="Import Local Files"
      size="xl"
      v-model="show"
    >
      <b-row>
        <b-col :cols="4" style="text-align:right">
          <b-card>
            <input
              type="file"
              value=""
              ref="file"
              id="file"
              @change="fileSelect"
            />
          </b-card>
          <b-button
            variant="primary"
            @click="handleFileUpload"
            :disabled="isBusy"
            style="width:96px"
          >
            <span v-if="!isBusy">Go</span>
            <b-spinner small v-if="isBusy"></b-spinner>
          </b-button>
        </b-col>
        <b-col :cols="8">
          <b-table
            :items="items"
            :fields="fields"
            sticky-header="600px"
            head-variant="light"
            ref="selectableTable"
            selectable
            select-mode="multi"
            @row-selected="onRowSelected"
            responsive="xl"
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
        <b-button size="xl" variant="secondary" @click="show = false">
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
  name: "selectPlace",
  props: {
    name: {
      default: ""
    }
  },
  data() {
    return {
      file: undefined,
      isBusy: false,
      show: false,
      /*表格子數據放這裡*/
      fields: [
        {
          key: "pName",
          label: "Place Name",
          sortable: true
        },
        {
          key: "pNameChn",
          label: "地名",
          sortable: true
        },
        {
          key: "pStartTime",
          label: "First Year",
          sortable: true
        },
        {
          key: "pEndTime",
          label: "Last Year",
          sortable: true
        },
        {
          key: "pBName",
          label: "Belongs To",
          sortable: true
        },
        {
          key: "pBNameChn",
          label: "属于",
          sortable: true
        }
      ],
      items: [
        {
          pId: 20,
          pName: "Guangdong Sheng",
          pNameChn: "\u5ee3\u6771\u7701",
          pStartTime: 1949,
          pEndTime: 2005,
          pBName: "People's Republic of China",
          pBNameChn: "\u4e2d\u83ef\u4eba\u6c11\u5171\u548c\u570b"
        },
        {
          pId: 6060,
          pName: "Guangdong Buzhengsi",
          pNameChn: "\u5ee3\u6771\u5e03\u653f\u53f8",
          pStartTime: 1368,
          pEndTime: 1643,
          pBName: "Jiangxi zongzhi",
          pBNameChn: "\u6c5f\u897f\u7e3d\u5236"
        },
        {
          pId: 8384,
          pName: "Guangdong Sheng",
          pNameChn: "\u5ee3\u6771\u7701",
          pStartTime: 1820,
          pEndTime: 1911,
          pBName: "Qing Dynasty",
          pBNameChn: "\u6e05\u671d"
        },
        {
          pId: 21023,
          pName: "Guangdong sheng",
          pNameChn: "\u5ee3\u6771\u7701",
          pStartTime: 1912,
          pEndTime: 1949,
          pBName: "Republic of China",
          pBNameChn: "\u4e2d\u83ef\u6c11\u570b"
        },
        {
          pId: 21217,
          pName: "Guangdong Sheng Zhudaoqu",
          pNameChn: "\u5ee3\u6771\u7701\u8af8\u9053\u5340",
          pStartTime: 1911,
          pEndTime: 1948,
          pBName: "Guangdong sheng",
          pBNameChn: "\u5ee3\u6771\u7701"
        },
        {
          pId: 211033,
          pName: "Guangdongdao xuanweisi",
          pNameChn: "\u5ee3\u6771\u9053\u5ba3\u6170\u53f8",
          pStartTime: 1278,
          pEndTime: 1367,
          pBName: "Jiangxi xingzhongshusheng",
          pBNameChn: "\u6c5f\u897f\u884c\u4e2d\u66f8\u7701"
        },
        {
          pId: 220038,
          pName: "Haibeiguangdong lianfangsi Dao",
          pNameChn: "\u6d77\u5317\u5ee3\u6771\u5ec9\u8a2a\u53f8\u9053",
          pStartTime: 1291,
          pEndTime: 1367,
          pBName: "Jiangnan zhudao xing yushitai",
          pBNameChn: "\u6c5f\u5357\u8af8\u9053\u884c\u5fa1\u53f2\u81fa"
        },
        {
          pId: 300494,
          pName: "Guangdong Duzhihuishisi",
          pNameChn: "\u5ee3\u6771\u90fd\u6307\u63ee\u4f7f\u53f8",
          pStartTime: 1375,
          pEndTime: 1643,
          pBName: "Qianjun Dudufu",
          pBNameChn: "\u524d\u8ecd\u90fd\u7763\u5e9c"
        },
        {
          pId: 302060,
          pName: "Guangdong xunfu",
          pNameChn: "\u5ee3\u6771\u5de1\u64ab",
          pStartTime: 1436,
          pEndTime: 1569,
          pBName: "Ming Dynasty",
          pBNameChn: "\u660e\u671d"
        },
        {
          pId: 302264,
          pName: "Guangdong wei",
          pNameChn: "\u5ee3\u6771\u885b",
          pStartTime: 1368,
          pEndTime: 1374,
          pBName: "Guangdong duwei",
          pBNameChn: "\u5ee3\u6771\u90fd\u885b"
        },
        {
          pId: 302265,
          pName: "Guangdong duwei",
          pNameChn: "\u5ee3\u6771\u90fd\u885b",
          pStartTime: 1372,
          pEndTime: 1374,
          pBName: "Ming Dynasty",
          pBNameChn: "\u660e\u671d"
        },
        {
          pId: 303317,
          pName: "Guangdong Jianchadao",
          pNameChn: "\u5ee3\u6771\u76e3\u5bdf\u9053",
          pStartTime: 1368,
          pEndTime: 1643,
          pBName: "Guangdong Zhudao",
          pBNameChn: "\u5ee3\u6771\u8af8\u9053"
        },
        {
          pId: 303325,
          pName: "Guangdong Zhudao",
          pNameChn: "\u5ee3\u6771\u8af8\u9053",
          pStartTime: 1368,
          pEndTime: 1643,
          pBName: "Anding Wei",
          pBNameChn: "\u5b89\u5b9a\u885b"
        }
      ],
      //选中的人物出现在这里
      selectedPlace: []
    };
  },
  methods: {
    fileSelect() {
      let file = this.$refs.file.files[0];
      this.file = file;
    },
    handleFileUpload() {
      //console.log('begin upload')
      this.isBusy = true;
      console.log(this.file);
      this.axios({
        url:
          "http://" +
          this.$store.state.global.serverAddress +
          "/api/tools/handle_upload_file",
        method: "POST", //  这个地方注意
        data: { user: this.$store.state.local.user.uid },
        file: this.file,
        processData: false,
        contentType: false,
        success: response => {
          console.log("upload_success_response:", response);
        }
      }).then(
        r => {
          this.isBusy = false;
        },
        e => {
          alert("something went wrong...");
          this.isBusy = false;
        }
      );
    },
    onRowSelected(items) {
      this.selectedPlace = items;
    },
    haveSelected: function(type) {
      //同步选中地点
      this.$emit("getPlaceName", this.selectedPlace);
      this.show = false;
    },
    selectAllRows() {
      this.$refs.selectableTable.selectAllRows();
    },
    clearSelected() {
      this.$refs.selectableTable.clearSelected();
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
