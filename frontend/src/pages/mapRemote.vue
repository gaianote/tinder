<template>
  <!-- Table -->
  <span>
    <el-button type="text" @click="dialogTableVisible = true"
      >MapRemote</el-button
    >

    <el-dialog title="MapRemote" :visible.sync="dialogTableVisible">
      <el-table
        :data="mapRules"
        size="mini"
        ref="multipleTable"
        tooltip-effect="dark"
        @selection-change="handleSelectionChange"
      >
        <el-table-column width="70" label="Enable">
          <template slot-scope="scope">
            <el-checkbox
              v-model="scope.row.enable"
              @change="enableMapRule(scope.row)"
            ></el-checkbox>
          </template>
        </el-table-column>
        <el-table-column
          label="MapFrom"
          width="200"
          prop="map_from"
        ></el-table-column>
        <el-table-column
          label="MapTo"
          width="200"
          prop="map_to"
        ></el-table-column>
        <el-table-column prop="Oprate" label="Oprate">
          <template slot-scope="scope">
            <el-button
              type="text"
              size="small"
              @click="eidtRulesDialog(scope.row)"
              >编辑</el-button
            >
            <el-button @click="deleteRule(scope.row)" type="text" size="small"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogTableVisible = false" size="mini"
          >取 消</el-button
        >
        <el-button type="primary" @click="addRulesDialog" size="mini"
          >新增</el-button
        >
      </div>
    </el-dialog>

    <el-dialog title="MapRules" :visible.sync="dialogFormVisible">
      <el-form>
        <el-form-item label="MapFrom" :label-width="formLabelWidth">
          <el-input v-model="map_from" width="120"></el-input>
        </el-form-item>
        <el-form-item label="MapTo" :label-width="formLabelWidth">
          <el-input v-model="map_to"></el-input>
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
  </span>
</template>

<script>
import * as api from "@/api";

export default {
  data() {
    return {
      mapRules: [
        {
          rid: "243u294u3u482848",
          enable: true,
          map_from: "https://thor.weidian.com",
          map_to: "https://thor.daily.weidian.com",
        },
      ],

      props: ["dialogTableVisible", "dialogFormVisible"],
      dialogTableVisible: false,
      dialogFormVisible: false,
      map_from: "",
      map_to: "",
      map_rid: "",
      map_enable: false,
      formLabelWidth: "120px",
    };
  },
  methods: {
    async getMapRemoteRules() {
      let res = await api.getMapRemoteRules();
      this.mapRules = res.data.result;
    },
    addRulesDialog() {
      this.map_from = "";
      this.map_to = "";
      this.map_rid = "";
      this.dialogFormVisible = true;
    },
    eidtRulesDialog(row) {
      this.map_from = row.map_from;
      this.map_to = row.map_to;
      this.map_rid = row.rid;
      this.map_enable = row.enable;
      this.dialogFormVisible = true;
    },
    async confirmRule() {
      console.log(this.map_rid);
      if (!this.map_rid) {
        await this.addRule();
      } else {
        await this.updateMapRule();
      }
    },
    async addRule() {
      let rules = {
        enable: false,
        map_from: this.map_from,
        map_to: this.map_to,
      };
      await api.addMapRule(rules);
      //添加映射规则
      this.mapRules.push(rules);
      await this.getMapRemoteRules();
      this.dialogFormVisible = false;
    },
    async enableMapRule(row) {
      this.map_from = row.map_from;
      this.map_to = row.map_to;
      this.map_rid = row.rid;
      this.map_enable = row.enable;
      await this.updateMapRule();
    },
    async updateMapRule() {
      let rules = {
        enable: this.map_enable,
        map_from: this.map_from,
        map_to: this.map_to,
        rid: this.map_rid,
      };
      console.log(rules);
      await api.updateMapRule(rules);
      //添加映射规则
      await this.getMapRemoteRules();
      this.dialogFormVisible = false;
    },
    async deleteRule(row) {
      await api.deleteMapRule(row.rid);
      let index = this.mapRules.findIndex((item) => item.rid === row.rid);
      if (index != -1) {
        this.mapRules.splice(index, 1);
      }
    },
    handleClick(row) {
      console.log(row);
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
      console.log(val);
    },
    toggleSelection(rows) {
      if (rows) {
        rows.forEach((row) => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
  },
  mounted() {
    this.getMapRemoteRules();
  },
};
</script>
