<template>
  <div>
    <el-row>
      <el-button size="mini">默认按钮</el-button>
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
      <el-table-column width="70" label="Enable">
        <template slot-scope="scope">
          <el-checkbox
            v-model="scope.row.enable"
            @change="upDateMockRule(scope.row)"
          ></el-checkbox>
        </template>
      </el-table-column>
      <el-table-column prop="rule" label="rule" width="500"> </el-table-column>
      <el-table-column prop="describe" label="describe" width="300">
      </el-table-column>
      <el-table-column prop="group_name" label="group_name" width="100">
      </el-table-column>

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
      <el-table-column label="操作" width="200">
        <template slot-scope="scope">
          <el-button @click="handleClick(scope.row)" type="text" size="small"
            >Request</el-button
          >
          <el-button @click="handleClick(scope.row)" type="text" size="small"
            >Response</el-button
          >
          <el-button
            type="text"
            size="small"
            @click="saveMockRuleDialog(scope.row)"
            >Save</el-button
          >
        </template>
      </el-table-column>
    </el-table>
    <!-- mock 规则弹窗 -->
    <el-dialog title="MockRules" :visible.sync="dialogFormVisible">
      <el-form>
        <el-form-item label="GroupName" label-width="120px">
          <el-input v-model="group_name"></el-input>
        </el-form-item>
        <el-form-item label="Describe" label-width="120px">
          <el-input v-model="describe"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false" size="mini"
          >取 消</el-button
        >
        <el-button type="primary" @click="confirmRule" size="mini"
          >确 定</el-button
        >
      </div>
    </el-dialog>
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
      group_name: "",
      describe: "",
      mockRules: "",
      clientProxyStatus: false,
      tableData: [],
      dialogFormVisible: false,
      row: "",
    };
  },
  methods: {
    async upDateMockRule(row) {
      await api.updateMockRule({
        rid: row.rid,
        enable: row.enable,
      });
    },
    async deleteAllFlow() {
      await api.deleteAllFlow();
      this.tableData = [];
    },
    saveMockRuleDialog(row) {
      this.row = row;
      this.dialogFormVisible = true;
      console.log(row);
    },
    async confirmRule() {
      await api.addMockRule({
        rule: this.row.url,
        request: this.row.request,
        response: this.row.response,
        group_name: this.group_name,
        describe: this.describe,
        enable: false,
      });
      this.dialogFormVisible = false;
    },
    handleClick() {
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
    let res = await api.getMockRules();
    this.tableData = res.data.result;
    let proxyRes = await api.getClientProxy();
    if (proxyRes.data.result == true) {
      this.clientProxyStatus = true;
    }
  },
};
</script>
