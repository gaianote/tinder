<template>
  <div>
    <el-row>
      <el-button size="mini">默认按钮</el-button>
      <el-button size="mini" @click="deleteAllFlow">clear</el-button>
      <el-button size="mini">delete</el-button>

      <el-switch
        size="mini"
        active-text="代理本机"
        v-model="clientProxyStatus"
        active-color="#13ce66"
        inactive-color="#ff4949"
        @change="changeClientStatus"
      >
      </el-switch>
      <el-switch
        size="mini"
        active-text="Mock"
        v-model="clientProxyStatus"
        active-color="#13ce66"
        inactive-color="#ff4949"
      >
      </el-switch>
      <MapRemote />
    </el-row>
    <el-table size="mini" :data="tableData" style="width: 100%">
      <el-table-column type="selection" width="55"> </el-table-column>
      <el-table-column prop="method" label="method" width="80">
      </el-table-column>
      <el-table-column prop="status" label="status" width="80">
      </el-table-column>
      <el-table-column prop="url" label="url" width="500"> </el-table-column>
      <el-table-column prop="start" label="start" width="180">
      </el-table-column>
      <el-table-column prop="duration" label="duration" width="100">
      </el-table-column>
      <el-table-column prop="size" label="size" width="100"> </el-table-column>
      <el-table-column type="expand">
        <template slot-scope="props">
          <el-row :gutter="20">
            <el-col :span="10">
              <Code
                title="Request"
                class="res-code-mirror"
                v-model="props.row.request"
              ></Code>
            </el-col>
            <el-col :span="14">
              <Code
                title="Response"
                class="res-code-mirror"
                v-model="props.row.response"
              ></Code>
            </el-col>
          </el-row>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import Code from "@/components/Code";
import MapRemote from "@/pages/mapRemote";
// import getFlowList from "@/api/flow";
import * as api from "@/api";

export default {
  components: {
    Code,
    MapRemote,
  },
  data() {
    return {
      clientProxyStatus: false,
      tableData: [],
      dialogTableVisible: false,
    };
  },
  methods: {
    async deleteAllFlow() {
      await api.deleteAllFlow();
      this.tableData = [];
    },
    toggal() {
      this.shown = !this.shown;
      this.isAddingNewLabel = false;
    },
    async changeClientStatus() {
      // 打开/关闭 本机代理 功能
      if (this.clientProxyStatus == false) {
        await api.closeClientProxy();
      } else {
        await api.openClientProxy();
      }
    },
  },
  async mounted() {
    let res = await api.getFlowList(1, 20);
    this.tableData = res.data.result;
    let proxyRes = await api.getClientProxy();
    if (proxyRes.data.result == true) {
      this.clientProxyStatus = true;
    }
  },
};
</script>
